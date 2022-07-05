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

# -------------TRAITAR_PARSING-----------------------
def traitar_parsing():

    traiatar_dir = '//wsl.localhost/Ubuntu/home/vitt\\validation_sets\\morphology_validation'
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
            temp_d = {"SGB": SGB, "Bacillus or coccobacillus": "NO", "Coccus": "NO", "Coccus—clusters or groups predominate" : "NO", "Coccus—pairs or chains predominate" : "NO"}

            # PROCESSING
            for row in temp["sample"]:
                if row == "Bacillus or coccobacillus":               temp_d["Bacillus or coccobacillus"] = "YES"
                if row == "Coccus":                                 temp_d["Coccus"] = "YES"
                if row == "Coccus—clusters or groups predominate":  temp_d["Coccus—clusters or groups predominate"] = "YES"
                if row == "Coccus—pairs or chains predominate":     temp_d["Coccus—pairs or chains predominate"] = "YES"
                
            row_list.append(temp_d)

    traitar = pd.DataFrame(row_list)
    print(traitar)
    traitar.to_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_morphology_validation.npy')

# ------------------MAIN-----------------------------

def main():
    print("---------STARTING data parsing------------")
    # -----------------running parsing operations-------------------
    traitar_parsing()

    # ----------------reading parsed data---------------------------
    #traitar=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/traitar_summary.npy', index_col=0)

    # ---------------print parsed data-----------------------------
    # print(traitar)


if __name__ == "__main__":
    main()
