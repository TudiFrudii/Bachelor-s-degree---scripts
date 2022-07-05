import fnmatch
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

# ------------------MP3_PARSING----------------------
def MP3_parsing():
    directory = '//wsl.localhost/Ubuntu/home/vitt/validation_sets/pathogenicity_validation/dataset/aa_files'
    print("main directory is", directory)

    row_list = []

    for root, subfolders, files in os.walk(directory):
        for file in files:
            SGB = file
            file = os.path.join(root, file)
            #print(SGB)
            if fnmatch.fnmatch(file, '*_50.fasta.Hybrid.summary*'):
                #print("FOUND:", file)
                temp = pd.read_csv(file, skiprows=1, delimiter='=')
                row_list.append({"SGB": (SGB).split(
                    "_")[0], "Non-Pathogenic": temp.iloc[0][1], "Pathogenic": temp.iloc[1][1]})

    mp3 = pd.DataFrame(row_list)
    #print("===")
    print(mp3)
    mp3.to_csv('//wsl.localhost/Ubuntu/home/vitt/mp3_pathogenicity_validation.npy')

# -------------PATHOFACT_PARSING---------------------
def pathofact_parsing():
    # what I am interested in are:
    # toxin report:
    # /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/DataSets/SGB_decompress/{SGB_id}/outputs/PathoFact_intermediate/TOXIN/HMM_toxin/{file.fna_id}.Input_HMM_R.csv
    #    -> count  number of line read => number of toxines detected
    # /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/DataSets/SGB_decompress/{SGB_id}/outputs/PathoFact_intermediate/VIRULENCE/classifier_virulence/{file.fna_id}_classifier_results_formatted.tsv
    #    -> define positive and degative outcomes
    # /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/DataSets/SGB_decompress/{SGB_id}/outputs/PathoFact_intermediate/PathoFact_intermediate/AMR/RGI_results/{file.fna_id}.RGI.txt
    # /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/DataSets/SGB_decompress/{SGB_id}/outputs/PathoFact_intermediate/PathoFact_intermediate/AMR/deepARG_results/{file.fna_id}.out.mapping.ARG
    #    -> count and compare AMR

    directory = '//wsl.localhost/Ubuntu/home/vitt/validation_sets/pathogenicity_validation/dataset/nt_files'
    print("main directory is", directory)

    # SGB, FILE.fna, number_of_toxines, number of Non_patho, Number Patho, number ARG genes
    # ID SONO SBAGLIATE, ho scritto i taxon, rifare
    row_list = []

    for main_dir in os.listdir(directory):
        trait = main_dir
        main_dir = os.path.join(directory, main_dir)
        #print(trait)
        for second_dir in os.listdir(main_dir):
            TAXON = second_dir
            second_dir = os.path.join(main_dir, TAXON)
            # print(TAXON)
            for third_dir in os.listdir(second_dir):
                SGB = third_dir
                third_dir = os.path.join(second_dir, SGB)
                #print(SGB)
                row_list.append(
                    {"SGB": SGB, "Toxines": 0, "Non-Pathogenic": 0, "Pathogenic": 0, "Total": 0})

    for main_dir in os.listdir(directory):
        trait = main_dir
        main_dir = os.path.join(directory, main_dir)
        # print(trait)
        for second_dir in os.listdir(main_dir):
            TAXON = second_dir
            second_dir = os.path.join(main_dir, TAXON)
            # print(TAXON)
            for third_dir in os.listdir(second_dir):
                SGB = third_dir
                third_dir = os.path.join(second_dir, SGB)
                # print(SGB)
                # cerco i file che mi interessano per ogni SGB dir
                for root, subfolders, files in os.walk(third_dir):
                    for file in files:
                        file = os.path.join(root, file)
                        if file.endswith("_classifier_results_formatted.tsv"):
                            # VIRULENCE_FILE
                            #print("{} \t\t this is a virulence file".format(SGB))
                            virulence = pd.read_csv(
                                file, delimiter="\t", index_col=0, header=None)
                            for item in row_list:
                                if (item["SGB"] == SGB):
                                    item["Pathogenic"] += virulence[1].str.count(
                                        "pathogenic").sum()
                                    item["Non-Pathogenic"] += virulence[1].str.count(
                                        "negative").sum()

                        if file.endswith(".Input_HMM_R.csv"):
                            # TOXIN_FILE
                            #print("{} \t\t this is a toxin file".format(SGB))
                            toxin = pd.read_csv(file)
                            # updating values in list of dictionaries
                            #row_list[SGB]['Toxines'] += len(toxin)
                            for item in row_list:
                                if (item["SGB"] == SGB):
                                    item["Toxines"] += len(toxin)
    for item in row_list:
        item["Total"] = item["Pathogenic"] + item["Toxines"]

    # print(row_list)
    pathofact = pd.DataFrame(row_list)
    print(pathofact)
    pathofact.to_csv('//wsl.localhost/Ubuntu/home/vitt/pathofact_pathogenicity_validation.npy')

# ------------------MAIN-----------------------------


def main():
    # this is the core of the code
    print("---------STARTING data parsing------------")

    # -----------------running parsing operations-------------------
    MP3_parsing()
    pathofact_parsing()

    # ----------------reading parsed data---------------------------
    #mp3=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/mp3_summary.npy', index_col=0)
    #pathofact=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/pathofact_summary.npy', index_col=0)

    # ---------------print parsed data-----------------------------
    # print(mp3)
    # print(pathofact)


if __name__ == "__main__":
    main()
