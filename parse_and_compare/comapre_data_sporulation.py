import pandas as pd
import numpy as np
import os as os

SGB_never = [10373, 10371, 10379, 10385, 81597, 10341, 81587]
SGB_always = [16445, 34046, 23707, 8401, 8402, 30079]

def phenotrex_traitar_comparison(phenotrex, traitar):
    print("computing a comparison between phenotrex and traitar outputs ...")

    phenotrex = phenotrex.reset_index()
    traitar = traitar.reset_index()
    counter_never = 0
    counter_always = 0
    phe_rigth_never = 0
    phe_rigth_always = 0
    tra_rigth_never = 0
    tra_rigth_always = 0
    agree = 0
    disagree = 0
    always_confidence_correct = 0
    always_confidence_wrong = 0
    never_confidence_wrong = 0
    never_confidence_correct = 0
    
    for index_phe, row_phe in phenotrex.iterrows():
        for index_tra, row_tra in traitar.iterrows():
            if row_phe["SGB"] == row_tra["SGB"]:
                SGB = row_phe["SGB"]
                #print(row_phe["Trait present"])
                #print("pos:", row_tra["Gram positive"], "- neg:", row_tra["Gram negative"])
                #found a match between the outputs
                #getting nothing because I have float values for phenotrex and "YES"/"NO" fro traitar
                if row_phe["Trait present"] == row_tra["Spore formation"]:  agree += 1 
                else:                                                       disagree += 1

                if SGB in SGB_always:
                    if row_phe["Trait present"] == "YES":                   
                        phe_rigth_always += 1
                        always_confidence_correct += row_phe["Confidence"]
                    else:
                        always_confidence_wrong += row_phe["Confidence"]
                    if row_tra["Spore formation"] == "YES":                 tra_rigth_always += 1
                    counter_always += 1
                    #always_confidence += row_phe["Confidence"]
                elif SGB in SGB_never:
                    if row_phe["Trait present"] == "NO":                    
                        phe_rigth_never += 1
                        never_confidence_correct += row_phe["Confidence"]
                    else: 
                        never_confidence_wrong += row_phe["Confidence"]
                    if row_tra["Spore formation"] == "NO":                  tra_rigth_never += 1
                    counter_never += 1
                    #never_confidence += row_phe["Confidence"]
    
    print("traitar predicted true positive trait in", tra_rigth_always/counter_always, "%", "of the cases")
    print("traitar predicted true negative trait in", tra_rigth_never/counter_never, "%", "of the cases")
    print("phenotrex's positive predictions are true for", phe_rigth_always/counter_always)
    print("phenotrex's negative predictions are true for", phe_rigth_never/counter_never)
    
    print("agreement:", agree/(agree+disagree), "\tdisagreement:", disagree/(agree+disagree)) 
    #print("\talways avg confidence:", always_confidence/counter_always, "\n\tnever avg confidence:", never_confidence/counter_never)
    try: 
        print("\tcorrect always prediction avg confidence: ", always_confidence_correct/phe_rigth_always)
    except :
        print("divirion per 0 case 1")

    try:    
        print("\twrong always prediction avg confidence: ", always_confidence_wrong/(len(SGB_always) - phe_rigth_always))
    except :
        print("divirion per 0 case 2")

    try:
        print("\tcorrect never prediction avg confidence: ", never_confidence_correct/phe_rigth_never)
    except :
        print("divirion per 0 case 3")

    try:
        print("\tworng never prediction avg confidence: ", never_confidence_wrong/(len(SGB_never) - phe_rigth_never))
    except :
        print("divirion per 0 case 4")
#------------------MAIN-----------------------------
def main():
    #this is the core of the code
    print("---------STARTING data comparison for SPORULATION------------")

    #----------------reading parsed data---------------------------
    phenotrex=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_sporulation_validation.npy', index_col=0)
    traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_sporulation_validation.npy', index_col=0)
    
    #---------------print parsed data-----------------------------
    #print(phenotrex)
    #print(traitar)
    
    #--------------comparison-------------------------------------
    phenotrex_traitar_comparison(phenotrex, traitar)

if __name__ == "__main__":
    main()