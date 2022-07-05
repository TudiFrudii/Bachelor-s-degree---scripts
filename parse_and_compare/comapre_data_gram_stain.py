import pandas as pd
import numpy as np
import os as os

SGB_neg = [9858, 13135, 13140, 32684, 5736, 13618, 10906]
SGB_pos = [8509, 34732, 17172, 34780, 34381]

def phenotrex_traitar_comparison(phenotrex, traitar):
    print("computing a comparison between phenotrex and traitar outputs ...")

    phenotrex = phenotrex.reset_index()
    traitar = traitar.reset_index()
    counter_pos = 0
    counter_neg = 0
    phe_rigth_pos = 0
    phe_rigth_neg = 0
    tra_rigth_pos = 0
    tra_rigth_neg = 0
    agree = 0
    disagree = 0
    pos_confidence = 0
    neg_confidence = 0
    
    for index_phe, row_phe in phenotrex.iterrows():
        for index_tra, row_tra in traitar.iterrows():
            if row_phe["SGB"] == row_tra["SGB"]:
                SGB = row_phe["SGB"]
                #print(row_phe["Trait present"])
                #print("pos:", row_tra["Gram positive"], "- neg:", row_tra["Gram negative"])
                #found a match between the outputs
                #getting nothing because I have float values for phenotrex and "YES"/"NO" fro traitar
                if row_phe["Trait present"] == row_tra["Gram positive"]:   agree += 1 
                else:                                                   disagree += 1 
                if row_phe["Trait present"] != row_tra["Gram negative"]:   agree += 1 
                else:                                                   disagree += 1

                if SGB in SGB_pos:
                    if row_phe["Trait present"] == "YES":                   phe_rigth_pos += 1
                    if row_tra["Gram positive"] == "YES":                   tra_rigth_pos += 1
                    counter_pos += 1
                    pos_confidence += row_phe["Confidence"]
                elif SGB in SGB_neg:
                    if row_phe["Trait present"] == "NO":                    phe_rigth_neg += 1
                    if row_tra["Gram negative"] == "YES":                   tra_rigth_neg += 1
                    counter_neg += 1
                    neg_confidence += row_phe["Confidence"]
    
    print("traitar predicted true positive trait in", tra_rigth_pos/counter_pos, "%", "of the cases")
    print("traitar predicted true negative trait in", tra_rigth_neg/counter_neg, "%", "of the cases")
    print("phenotrex's positive predictions are true for", phe_rigth_pos/counter_pos)
    print("phenotrex's negative predictions are true for", phe_rigth_neg/counter_neg)

    print("agreement:", agree/(agree+disagree), "\tdisagreement:", disagree/(agree+disagree))
    
    print("agreement:", agree/(agree+disagree), "\tdisagreement:", disagree/(agree+disagree)) 
    print("\tpos avg confidence:", pos_confidence/counter_pos, "\n\tneg avg confidence:", neg_confidence/counter_neg)

#------------------MAIN-----------------------------
def main():
    #this is the core of the code
    print("---------STARTING data comparison for GRAM STAIN------------")

    #----------------reading parsed data---------------------------
    phenotrex=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_gram_stain_validation.npy', index_col=0)
    traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_gram_stain_validation.npy', index_col=0)
    
    #---------------print parsed data-----------------------------
    #print(phenotrex)
    #print(traitar)
    
    #--------------comparison-------------------------------------
    phenotrex_traitar_comparison(phenotrex, traitar)

if __name__ == "__main__":
    main()