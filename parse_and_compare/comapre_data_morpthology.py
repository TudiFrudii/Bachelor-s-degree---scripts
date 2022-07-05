import pandas as pd
import numpy as np
import os as os

SGB_coccoids = [16630,16673,16963,5566,28790,5580,5590,28728,28730]
SGB_rods = [16086,34249,34270,34260,8583,8584,30401]
SGB_bacilli = [14809,14810,14811,33563,74488]

def phenotrex_traitar_comparison(traitar):
    print("computing a comparison for traitar outputs ...")

    traitar = traitar.reset_index()
    counter_cocccus = 0
    counter_bacilli = 0
    counter_rods = 0
    '''
    tra_rigth_coccus = 0
    tra_rigth_bacilli = 0
    tra_rigth_rods = 0
    '''

    cocci_classifier_cocci = 0
    cocci_classifier_rods = 0
    rods_classifier_rods = 0
    rods_classifier_cocci = 0

    for index_tra, row_tra in traitar.iterrows():
        SGB = row_tra["SGB"]

        if SGB in SGB_coccoids:
            if row_tra["Bacillus or coccobacillus"] == "NO":                            rods_classifier_cocci += 1
            if row_tra["Coccus"] == "YES":                                              cocci_classifier_cocci += 1
            counter_cocccus += 1
        elif SGB in SGB_bacilli:
            if row_tra["Bacillus or coccobacillus"] == "YES":                           rods_classifier_rods += 1
            if row_tra["Coccus"] == "NO":                                               cocci_classifier_rods += 1
            counter_bacilli += 1
        
    print("coccus: \n\t cocci classifier accuracy:", cocci_classifier_cocci/counter_cocccus, "\trods classifier accuracy:", rods_classifier_cocci/counter_cocccus)
    
    print("rods: \n\t cocci classifier accuracy:", cocci_classifier_rods/counter_bacilli, "\trods classifier accuracy:", rods_classifier_rods/counter_bacilli)

    '''
    for index_tra, row_tra in traitar.iterrows():
        SGB = row_tra["SGB"]

        if SGB in SGB_coccoids:
            if row_tra["Bacillus or coccobacillus"] == "NO":                            tra_rigth_coccus += 1
            if row_tra["Coccus"] == "YES":                                              tra_rigth_coccus += 1
            counter_cocccus += 1
        elif SGB in SGB_bacilli:
            if row_tra["Bacillus or coccobacillus"] == "YES":                           tra_rigth_bacilli += 1
            if row_tra["Coccus"] == "NO":                                               tra_rigth_bacilli += 1
            counter_bacilli += 1
        elif SGB in SGB_rods:
            #if row_tra["Bacillus or coccobacillus"] == "NO":                            tra_rigth_rods += 1
            #if row_tra["Coccus"] == "NO":                                               tra_rigth_rods += 1
            counter_rods += 1
    print("percentage of coccus prediction accuracy:", tra_rigth_coccus / (2 * counter_cocccus))
    print("percentage of bacilli prediction accuracy:", tra_rigth_bacilli / (2 * counter_bacilli))
    print("percentage of rods prediction accuracy:", tra_rigth_rods / (2 * counter_rods))
    print("percentage of coccus prediction accuracy:", tra_rigth_coccus / (counter_cocccus))
    print("percentage of bacilli prediction accuracy:", tra_rigth_bacilli / (counter_bacilli))
    print("percentage of rods prediction accuracy:", tra_rigth_rods / (counter_rods))
    '''

    
#------------------MAIN-----------------------------
def main():
    #this is the core of the code
    print("---------STARTING data comparison for MORPHOLOGY------------")

    #----------------reading parsed data---------------------------
    traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_morphology_validation.npy', index_col=0)
    
    #---------------print parsed data-----------------------------
    #print(traitar)
    
    #--------------comparison-------------------------------------
    phenotrex_traitar_comparison(traitar)

if __name__ == "__main__":
    main()