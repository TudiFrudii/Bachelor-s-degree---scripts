#!/bin/bash

input=$1
min_len=$2
threshold=$3

if [ "$#" -lt 3 ]; then
    echo "The script need at least three arguments: input_dir, min_len and threshold"
    exit 1
fi

echo "computing mp3 analisys..."

for SGB in $( find $input -type f -name "*_50.fasta" )
do
    echo "computing mp3 analysis on SGB: $SGB"
    #calling ./mp3 from a different dir does not work, working script lies in dir /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/mp3
    ./mp3 $input/$SGB/${SGB}_50.fasta 1 $min_len $threshold
done