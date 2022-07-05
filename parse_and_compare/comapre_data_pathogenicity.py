import pandas as pd
import numpy as np
import os as os
import matplotlib.pyplot as plt

SGB_pos = [30530,15127, 10083, 7968, 19395, 13582, 9963]
SGB_neg = [25181, 87490, 4925, 30826, 12968]

#----------------MP3-PATHOFACT_MODIFIED_COMPARISON--------------
def MP3_pathofact_comparison2(mp3, pathofact):
    print("computing a comparison between MP3 and pathofact outputs ...")
    # given the fact that both MP3 and pathofact give as output the number of pathogenic and non pathogenic
    # proteins that are detected in a .fa file, I compare the ratio of the two outputs
    
    mp3 = mp3.reset_index()
    pathofact = pathofact.reset_index()
    match_counter = 0           #number of comparable object
    pos_glob_difference = 0
    neg_glob_difference = 0
    mp3_pos_tops = 0            #number of times that mp3 predicts more pathogenic protein that pathofact
    mp3_neg_tops = 0            #number of times that mp3 predicts more non-pathogenic protein that pathofact
    patho_cumulative_pos_patho = 0
    patho_cumulative_neg_patho = 0
    mp3_cumulative_pos_patho = 0
    mp3_cumulative_neg_patho = 0
    patho_cumulative_pos_non = 0
    patho_cumulative_neg_non = 0
    mp3_cumulative_pos_non = 0
    mp3_cumulative_neg_non = 0
    pos_counter = 0
    neg_counter = 0

    for index_mp3, row_mp3 in mp3.iterrows():
        for index_patho, row_patho in pathofact.iterrows():
            if row_patho["SGB"] == row_mp3["SGB"]:
                SGB = row_patho["SGB"]
                if row_patho["Total"] != 0 and row_patho["Non-Pathogenic"] != 0 and row_mp3["Pathogenic"] != 0 and row_mp3["Non-Pathogenic"] != 0:
                    #at this point I found two rows for the same SGB and Identifier, I can compare outputs
                    match_counter += 1
                    #print("for data:", row_mp3["SGB"], row_mp3["Identifier"])
                    #print("mp3 detected:", row_mp3["Pathogenic"], "as positive and", row_mp3["Non-Pathogenic"], "as negative")
                    #print("pathofact detected:", row_patho["Pathogenic"], "as positive and", row_patho["Non-Pathogenic"], "as negative")
                    total_patho = row_patho["Total"] + row_patho["Non-Pathogenic"]
                    total_mp3 = row_mp3["Pathogenic"] + row_mp3["Non-Pathogenic"]
                    # this is the difference of the percentage of the positivity and negativity of the outcome
                    pos_difference = abs(row_patho["Total"]/total_patho - row_mp3["Pathogenic"]/total_mp3) 
                    neg_difference = abs(row_patho["Non-Pathogenic"]/total_patho - row_mp3["Non-Pathogenic"]/total_mp3)
                    #print("for data", row_patho["Identifier"], "they differ for POS:", pos_difference, ", NEG:" , neg_difference)
                    pos_glob_difference += pos_difference
                    neg_glob_difference += neg_difference
                    if row_mp3["Pathogenic"] > row_patho["Pathogenic"]: mp3_pos_tops += 1 
                    else: mp3_pos_tops -= 1
                    if row_mp3["Non-Pathogenic"] > row_patho["Non-Pathogenic"]: mp3_neg_tops += 1 
                    else: mp3_neg_tops -= 1
                    if SGB in SGB_neg:
                        patho_cumulative_neg_patho += row_patho["Pathogenic"]
                        mp3_cumulative_neg_patho =+ row_mp3["Pathogenic"]
                        patho_cumulative_neg_non += row_patho["Non-Pathogenic"]
                        mp3_cumulative_neg_non =+ row_mp3["Non-Pathogenic"]
                        neg_counter += 1
                    if SGB in SGB_pos:
                        patho_cumulative_pos_patho += row_patho["Pathogenic"]
                        mp3_cumulative_pos_patho =+ row_mp3["Pathogenic"]
                        patho_cumulative_pos_non += row_patho["Non-Pathogenic"]
                        mp3_cumulative_pos_non =+ row_mp3["Non-Pathogenic"]
                        pos_counter += 1

    print("overall the discrepancy is pathogenic:", pos_glob_difference/match_counter, "; non-pathogenic:", neg_glob_difference/match_counter)
    if mp3_pos_tops > 0: print("overall, mp3 detected more pathogenic proteins")
    else: print("overall, pathofact detected more pathogenic proteins")
    if mp3_neg_tops > 0: print("overall, mp3 detected more non-pathogenic proteins")
    else: print("overall, pathofact detected more non-pathogenic proteins")
    print("---")
    print("Pathofact detected an avg value of", patho_cumulative_neg_patho/neg_counter, "pathogenic proteins for non pathogens")
    print("Pathofact detected an avg value of", patho_cumulative_pos_patho/pos_counter, "pathogenic proteins for pathogens")
    print("MP3 detected an avg value of", mp3_cumulative_neg_patho/neg_counter, "pathogenic proteins for non pathogens")
    print("MP3 detected an avg value of", mp3_cumulative_pos_patho/pos_counter, "pathogenic proteins for pathogens")
    print("---")
    print("Pathofact detected an avg value of", patho_cumulative_neg_non/neg_counter, "non pathogenic proteins for non pathogens")
    print("Pathofact detected an avg value of", patho_cumulative_pos_non/pos_counter, "non pathogenic proteins for pathogens")
    print("MP3 detected an avg value of", mp3_cumulative_neg_non/neg_counter, "non pathogenic proteins for non pathogens")
    print("MP3 detected an avg value of", mp3_cumulative_pos_non/pos_counter, "non pathogenic proteins for pathogens")

#----------------MP3-PATHOFACT_ORIGINAL_COMPARISON--------------
def MP3_pathofact_comparison(mp3, pathofact):
    print("computing a comparison between MP3 and pathofact outputs ...")
    # given the fact that both MP3 and pathofact give as output the number of pathogenic and non pathogenic
    # proteins that are detected in a .fa file, I compare the ratio of the two outputs
    
    mp3 = mp3.reset_index()
    pathofact = pathofact.reset_index()
    match_counter = 0           #number of comparable objects
    pos_glob_difference = 0
    neg_glob_difference = 0
    mp3_pos_tops = 0            #number of times that mp3 predicts more pathogenic protein that pathofact
    mp3_neg_tops = 0            #number of times that mp3 predicts more non-pathogenic protein that pathofact
    
    for index_mp3, row_mp3 in mp3.iterrows():
        for index_patho, row_patho in pathofact.iterrows():
            if row_patho["SGB"] == row_mp3["SGB"] and row_mp3["Identifier"] == row_patho["Identifier"]:
                if row_patho["Total"] != 0 and row_patho["Non-Pathogenic"] != 0 and row_mp3["Pathogenic"] != 0 and row_mp3["Non-Pathogenic"] != 0:
                    #at this point I found two rows for the same SGB and Identifier, I can compare outputs
                    match_counter += 1
                    #print("for data:", row_mp3["SGB"], row_mp3["Identifier"])
                    #print("mp3 detected:", row_mp3["Pathogenic"], "as positive and", row_mp3["Non-Pathogenic"], "as negative")
                    #print("pathofact detected:", row_patho["Pathogenic"], "as positive and", row_patho["Non-Pathogenic"], "as negative")
                    total_patho = row_patho["Total"] + row_patho["Non-Pathogenic"]
                    total_mp3 = row_mp3["Pathogenic"] + row_mp3["Non-Pathogenic"]
                    # this is the difference of the percentage of the positivity and negativity of the outcome
                    pos_difference = abs(row_patho["Total"]/total_patho - row_mp3["Pathogenic"]/total_mp3) 
                    neg_difference = abs(row_patho["Non-Pathogenic"]/total_patho - row_mp3["Non-Pathogenic"]/total_mp3)
                    #print("for data", row_patho["Identifier"], "they differ for POS:", pos_difference, ", NEG:" , neg_difference)
                    pos_glob_difference += pos_difference
                    neg_glob_difference += neg_difference
                    if row_mp3["Pathogenic"] > row_patho["Pathogenic"]: mp3_pos_tops += 1 
                    else: mp3_pos_tops -= 1
                    if row_mp3["Non-Pathogenic"] > row_patho["Non-Pathogenic"]: mp3_neg_tops += 1 
                    else: mp3_neg_tops -= 1
                    

    print("overall the discrepancy is pathogenic:", pos_glob_difference/match_counter, "; non-pathogenic:", neg_glob_difference/match_counter)
    if mp3_pos_tops > 0: print("overall, mp3 detected more pathogenic proteins")
    else: print("overall, pathofact detected more pathogenic proteins")
    if mp3_neg_tops > 0: print("overall, mp3 detected more non-pathogenic proteins")
    else: print("overall, pathofact detected more non-pathogenic proteins")


def plottingMP3():
    labels = ['7967','7968','7701','13582','9963','19395','10083','10085','10088','23226','38353','58197','58198','25181','12968','4925','30826','87490']
    MP3_non_patho = [2234,2150, 6945,3285,4232,1332,4046,4339,3942,5686,3873,4480,4350,3961,7047,2276,2417,4656]
    MP3_patho = [1988,1917,5887,2907,3544,1198,3423,3640,3350,4702,3292,3762,3657,3486,5889,2048,2060,3850]

    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, MP3_non_patho, width, label='non-pathogenic')
    rects2 = ax.bar(x + width/2, MP3_patho, width, label='pathogenic')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    #ax.set_title('Scores by SGB and positivity')
    #ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

def plottingPatho():
    labels = ['7967','7968','13582','9963','10083','10085','23226','38353','58197','58198','12968','4925','30826','87490']
    pathogenic = [735,696,1990,2338,1596,1800,2534,1562,1841,1775,2205,599,995,2550,]
    non_pathogenic = [1520,1480,1344,2004,2553,2653,3286,2395,2755,2685,5041,1712,1482,2187]

    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, non_pathogenic, width, label='non-pathogenic')
    rects2 = ax.bar(x + width/2, pathogenic, width, label='pathogenic')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    #ax.set_title('Scores by SGB and positivity')
    #ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

#------------------MAIN-----------------------------
def main():
    #this is the core of the code
    print("---------STARTING data comparison for PATHOGENICITY------------")

    #----------------reading parsed data---------------------------
    #mp3=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/mp3_pathogenicity_validation.npy', index_col=0)       
    #pathofact=pd.read_csv('//wsl.localhost/Ubuntu/home/vitt/pathofact_pathogenicity_validation.npy', index_col=0)       

    #---------------print parsed data-----------------------------
    #print(mp3)
    #print(pathofact)

    #--------------comparison-------------------------------------
    #MP3_pathofact_comparison(mp3, pathofact)
    #MP3_pathofact_comparison2(mp3, pathofact)
    
    #plottingMP3()
    plottingPatho()

if __name__ == "__main__":
    main()