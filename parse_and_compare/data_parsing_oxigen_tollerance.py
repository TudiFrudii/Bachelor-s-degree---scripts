from genericpath import isfile
from logging.config import fileConfig
from operator import index
from traceback import print_tb
from xmlrpc.client import TRANSPORT_ERROR
import pandas as pd
import numpy as np
import os as os
from regex import I
from scipy.fft import set_global_backend
from sklearn.utils import indexable
import fnmatch

# ------------PHENOTREX_PARSING----------------------
def phenotrex_parsing():
    phenotrex_dir = '//wsl.localhost/Ubuntu/home/vitt\\validation_sets\\oxigen_tollerance_validation\\phenotrex_outputs'
    print("main directory is: ", phenotrex_dir)

    row_list = []

    for trait_dir in os.listdir(phenotrex_dir):
        #POS/NEG dir
        print("considering", trait_dir)
        trait_dir = os.path.join(phenotrex_dir, trait_dir)

        for main_dir in os.listdir(trait_dir):
            # qui so gia' di che SGB si parlacd 
            SGB = main_dir
            main_dir = os.path.join(trait_dir, main_dir)
            temp = {"SGB" : SGB, "Anaerobe" : "NO", "confidence_ana" : 0, "Aerobe": "NO", "confidence_aero" : 0}
            
            for second_dir in os.listdir(main_dir):
                second_dir = os.path.join(main_dir, second_dir)

                for file in os.listdir(second_dir):
                    oxigen_tollerance = file.split(".")[0]
                    if fnmatch.fnmatch(file, '*Aerobe*') or fnmatch.fnmatch(file, '*Anaerobe*'):
                        file = os.path.join(second_dir, file)
                        reading = pd.read_csv(file, skiprows=1, delimiter="\t")
                        temp[oxigen_tollerance] = reading["Trait present"][0]
                        if oxigen_tollerance == "Anaerobe":
                            temp["confidence_ana"] = reading["Confidence"][0]
                        else: 
                            temp["confidence_aero"] = reading["Confidence"][0]
                    
            row_list.append(temp)

            '''
            if fnmatch.fnmatch(file, '*Aerobe*') or fnmatch.fnmatch(file, '*Anaerobe*'):
                print("FOUND:", file)
                try:
                    temp = pd.read_csv(file, skiprows=1, delimiter="\t")
                    row_list.append({"SGB": (temp["Identifier"][0]).split("_")[0], "Trait": trait, "Trait present": temp["Trait present"][0], "Confidence": temp["Confidence"][0]})
                except:
                    print("error for file:", file)
            '''

    phenotrex_SGB = pd.DataFrame(row_list)
    print(phenotrex_SGB)
    #phenotrex_SGB.to_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_oxigen_tollerance_validation.npy')
    #phenotrex_SGB.to_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_oxigen_tollerance_summary_validation.npy')
    
# -------------TRAITAR_PARSING-----------------------
def traitar_parsing():

    traiatar_dir = '//wsl.localhost/Ubuntu/home/vitt\\validation_sets\\oxigen_tollerance_validation\\traitar_outputs'
    # this function is upposed to parse the output of traitar classifier\
    print("main directory is: ", traiatar_dir)
    row_list = []

    '''
    for root, subfolders, files in os.walk(phenotrex_dir):
            for file in files:
    '''

    for subset_dir in os.listdir(traiatar_dir):
        #POS/NEG dir
        print("considering", subset_dir)
        subset_dir = os.path.join(traiatar_dir, subset_dir)

        for main_dir in os.listdir(subset_dir):
            # qui so gia' di che SGB si parlacd 
            SGB = main_dir
            main_dir = os.path.join(subset_dir, main_dir)
            out_file = os.path.join(
                main_dir, 'traitar\\phenotype_prediction\\predictions_flat_majority-votes_combined.txt')
            # print(out_file)
            temp = pd.read_csv(out_file,  delimiter='\t')
            temp_d = {"SGB": SGB, "Anaerobe": "NO", "Aerobe": "NO", "Facultative" : "NO"}

            # PROCESSING
            for row in temp["sample"]:
                if row == "Anaerobe":
                    temp_d["Anaerobe"] = "YES"
                if row == "Aerobe":
                    temp_d["Aerobe"] = "YES"
                if row == "Facultative":
                    temp_d["Facultative"] = "YES"
                
            row_list.append(temp_d)

    traitar = pd.DataFrame(row_list)
    print(traitar)
    traitar.to_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_oxigen_tollerance_validation.npy')

# ------------------MAIN-----------------------------


def main():
    print("---------STARTING data parsing------------")
    # -----------------running parsing operations-------------------
    phenotrex_parsing()
    #traitar_parsing()

    # ----------------reading parsed data---------------------------
    #phenotrex=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/phenotrex_summary.npy', index_col=0)
    #traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_summary.npy', index_col=0)

    # ---------------print parsed data-----------------------------
    # print(phenotrex)
    # print(traitar)


if __name__ == "__main__":
    main()
