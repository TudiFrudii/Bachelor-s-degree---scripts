#!/bin/bash

input=$1
output=$2
set_of_classifiers=/shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/Phenotrex/classifiers/class_of_interest

if [ "$#" -lt 2 ]; then
    echo "The script needs input directory input and output as params"
    exit 1
fi

# per ogni cartella del dataset
for SGB_dir in $( ls  $input )
do
        #creazione cartella outputs
        SGB="$(basename $SGB_dir)"
        echo "creating an output directory for ${SGB}"
        mkdir $output/$SGB
        echo "----------------------------"

        for j in $( find  $SGB_dir -type f -name "*.fasta" )
        do
                data="$(basename $j)"
                mkdir  $output/$SGB/$data

                for k in $( find $set_of_classifiers -type f -name "*.class" )
                do
                        classifier="$(basename $k)"
                        touch $output/$SGB/$data/$classifier.csv
                        phenotrex predict --classifier $k $j > $output/$SGB/$data/$classifier.csv
                done
        done
done
