import pandas as pd
import numpy as np
import os as os

SGB_ana = [5870, 4690, 4874, 23995, 9220, 9223, 9224, 9225, 9226, 9227, 9228, 4593]
SGB_aero = [552, 554, 11225, 32271, 32272, 89658, 33387, 21529, 21530, 28362, 84664, 84665, 84666, 84667, 84668, 24204, 56675]

def phenotrex_traitar_comparison2(phenotrex, traitar):
    print("\ncomputing a comparison between phenotrex and traitar outputs ...\n")

    phenotrex = phenotrex.reset_index()
    traitar = traitar.reset_index()

    counter_ana = 0
    counter_aero = 0
    phe_ana_true = 0
    phe_aero_true = 0
    tra_ana_true = 0
    tra_aero_true = 0
    phe_ana_false = 0
    phe_aero_false = 0
    tra_ana_false = 0
    tra_aero_false = 0

    for index_phe, row_phe in phenotrex.iterrows():
        for index_tra, row_tra in traitar.iterrows():
            if row_phe["SGB"] == row_tra["SGB"]:
                SGB = row_phe["SGB"]

                if SGB in SGB_ana:  
                    counter_ana += 1
                    if row_phe["Anaerobe"] == "YES":    phe_ana_true += 1
                    else:                               phe_ana_false += 1
                    if row_tra["Anaerobe"] == "YES":    tra_ana_true += 1
                    else:                               tra_ana_false += 1

                elif SGB in SGB_aero: 
                    counter_aero += 1
                    if row_phe["Aerobe"] == "YES":      phe_aero_true += 1
                    else:                               phe_aero_false += 1
                    if row_tra["Aerobe"] == "YES":      tra_aero_true += 1
                    else:                               tra_aero_false += 1
                
            counter = counter_ana + counter_aero

    print("PHENOTERX aero_true_prediction:\t", phe_aero_true/counter_aero, "\t\t ana_true_pred:\t", phe_ana_true/counter_ana)
    print("TRAITAR aero_true_prediction:\t", tra_aero_true/counter_aero, "\t\t ana_true_pred:\t", tra_ana_true/counter_ana)

def phenotrex_traitar_comparison(phenotrex, traitar):
    print("\ncomputing a comparison between phenotrex and traitar outputs ...\n")

    phenotrex = phenotrex.reset_index()
    traitar = traitar.reset_index()
    counter_ana = 0
    counter_aero = 0
    agree = 0
    disagree = 0

    phe_rigth_ana = 0
    phe_rigth_aero = 0
    phe_false_ana = 0
    phe_false_aero = 0

    tra_rigth_ana = 0
    tra_rigth_aero = 0
    tra_false_ana = 0
    tra_false_aero = 0

    facultative_cases = 0
    
    for index_phe, row_phe in phenotrex.iterrows():
        for index_tra, row_tra in traitar.iterrows():
            if row_phe["SGB"] == row_tra["SGB"]:
                SGB = row_phe["SGB"]
                #print(row_phe["Trait present"])
                #print("pos:", row_tra["Gram positive"], "- neg:", row_tra["Gram negative"])
                #found a match between the outputs
                #getting nothing because I have float values for phenotrex and "YES"/"NO" fro traitar

                if row_phe["Aerobe"] == row_tra["Aerobe"]:                      agree += 1 
                else:                                                           disagree += 1 
                if row_phe["Anaerobe"] == row_tra["Anaerobe"]:                  agree += 1 
                else:                                                           disagree += 1
                if row_phe["Aerobe"] == row_phe["Anaerobe"] == row_tra["Facultative"]:  
                                                                                facultative_cases += 1

                if SGB in SGB_ana:      #ANAEROBIC -> ana = true, aero = false
                    if row_phe["Anaerobe"] == "YES":        phe_rigth_ana += 1  #TRUE prediction
                    else:                                   phe_false_ana += 1  #FALSE prediction
                    if row_phe["Aerobe"] == "NO":           phe_rigth_aero += 1 #TRUE prediction
                    else:                                   phe_false_aero += 1 #FALSE prediction
                    
                    if row_tra["Anaerobe"] == "YES":        tra_rigth_ana += 1  #TRUE pred
                    else:                                   tra_false_ana += 1  #FALSE pred
                    if row_tra["Aerobe"] == "NO":           tra_rigth_aero += 1 #TRUE pred
                    else:                                   tra_false_aero += 1 #FALSE pred
                    counter_ana += 1

                elif SGB in SGB_aero:
                    if row_phe["Aerobe"] == "YES":          phe_rigth_aero += 1
                    else:                                   phe_false_aero += 1
                    if row_phe["Anaerobe"] == "NO":         phe_rigth_ana += 1
                    else:                                   phe_false_ana += 1

                    if row_tra["Aerobe"] == "YES":          tra_rigth_aero += 1
                    else:                                   tra_false_aero += 1
                    if row_tra["Anaerobe"] == "NO":         tra_rigth_ana += 1
                    else:                                   tra_false_ana += 1
                    counter_aero += 1
                
                counter = counter_ana + counter_aero
    
    print("PHENOTREX ANA: right:\t", phe_rigth_ana/counter, "\t false:", phe_false_ana/counter)
    print("PHENOTREX AERO: right:\t", phe_rigth_aero/counter, "\t false:", phe_false_aero/counter)

    print("TRAITAR ANA: right:\t", tra_rigth_ana/counter, "\tfalse:", tra_false_ana/counter)
    print("TRAITAR AERO: right:\t", tra_rigth_aero/counter, "\t false:", tra_false_aero/counter)
    
    '''
    print("traitar predicted true anaerobe trait in", tra_rigth_ana/counter_ana, "%", "of the cases")
    print("traitar predicted true aerobe trait in", tra_rigth_aero/counter_aero, "%", "of the cases")
    print("phenotrex's anaerobe predictions are true for", phe_rigth_ana/counter_ana)
    print("phenotrex's aerobe predictions are true for", phe_rigth_aero/counter_aero)
    print("phenotrex predicts anaerobe and aerobe when traitar predicts facultative in", facultative_cases/(counter_ana + counter_aero), "even if no SGB was annotated as facultative in the DB")
    print("agreement:", agree/(agree+disagree), "\tdisagreement:", disagree/(agree+disagree)) 
    '''
def finding_threshold(phenotrex, SGB_subsample):
    print("\n... looking for a threshold for phenotrex confidence ...\n")
    
    phenotrex = phenotrex.reset_index()
    aero_pos = 0
    aero_neg = 0
    ana_pos = 0
    ana_neg = 0 
    c1 = 0
    c2 = 0
    c3 = 0 
    c4 = 0
    
    for index_phe, row_phe in phenotrex.iterrows():
        SGB = row_phe["SGB"]
        if SGB in SGB_subsample: 
            if row_phe["Aerobe"] == "YES" : 
                aero_pos += row_phe["confidence_aero"]
                c1 += 1
            if row_phe["Aerobe"] == "NO":
                aero_neg =+ row_phe["confidence_aero"]
                c2 += 1
            if row_phe["Anaerobe"] == "YES":
                ana_pos += row_phe["confidence_ana"]
                c3 += 1
            if row_phe["Anaerobe"] == "NO":
                ana_neg += row_phe["confidence_ana"]
                c4 += 1     
    
    
    if SGB_subsample == SGB_ana:
        print("===> for ANAEROBIC SUBSAMPLE")
    else:
        print("===> for AEROBIC SUBSAMPLE")

    try:       print("predicted positive aerobe trait with avg confidence ", aero_pos/c1) 
    except:    print("error for case 1")
    try: print("predicted false aerobe trait with avg confidence ", aero_neg/c2)
    except:    print("error for case 2")
    try: print("predicted positive anaerobe trait with avg confidence ", ana_pos/c3)
    except:    print("error for case 3")
    try: print("predicted negative anaerobe trait with avg confidence ", ana_neg/c4)
    except:    print("error for case 4")


#------------------MAIN-----------------------------
def main():
    #this is the core of the code
    print("---------STARTING data comparison for OXIGEN TOLLERANCE------------")

    #----------------reading parsed data---------------------------
    #phenotrex=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_oxigen_tollerance_validation.npy', index_col=0)
    phenotrex=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_oxigen_tollerance_summary_validation.npy', index_col=0)
    traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_oxigen_tollerance_validation.npy', index_col=0)
    
    #---------------print parsed data-----------------------------
    print(phenotrex)
    print(traitar)
    
    #--------------comparison-------------------------------------
    phenotrex_traitar_comparison(phenotrex, traitar)
    #phenotrex_traitar_comparison2(phenotrex, traitar)
    #finding_threshold(phenotrex, SGB_aero)
    #finding_threshold(phenotrex, SGB_ana)

if __name__ == "__main__":
    main()