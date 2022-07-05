#!/bin/bash

input=$1
cores=$2

if [ "$#" -lt 2 ]; then
    echo "The script needs input directory and cores as params"
    exit 1
fi

echo "computing pathofact complete analisys..."

for SGB in $( ls $input )
do
        echo "computing pathofact analysis on SGB: $SGB"
        #echo "complete path is $input/$SGB"
        #ACTUAL CONFIGURATION OF PATHOFACT

        rm /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/PathoFact/config.yaml

        (
        echo 'pathofact:'
        echo ' ' sample: ['"'${SGB}_50'"']
        echo '  project: output'
        echo ' ' datadir: $input/$SGB
        echo '  workflow: "complete" #options: "complete", "AMR", "Tox", "Vir"'
        echo '  size_fasta: 10000 #Adjustable to preference'
        echo '  scripts: "scripts"'
        echo '  signalp: "/shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/PathoFact/signalp-5.0b/bin"'
        echo '  deepvirfinder: "submodules/DeepVirFinder/dvf.py"'
        echo '  tox_hmm: "databases/toxins/combined_Toxin.hmm"'
        echo '  tox_lib: "databases/library_HMM_Toxins.csv"'
        echo '  tox_threshold: 40 #Bitscore threshold of the toxin prediction, adjustable by user to preference'
        echo '  vir_hmm: "databases/virulence/Virulence_factor.hmm"'
        echo '  vir_domains: "databases/models_and_domains"'
        echo '  plasflow_threshold: 0.7'
        echo '  plasflow_minlen: 1000'
        echo '  runtime:'
        echo '    short: "00:10:00"'
        echo '    medium: "01:00:00"'
        echo '    long: "02:00:00"'
        echo '  mem:'
        echo '    normal_mem_per_core_gb: "4G"'
        echo '    big_mem_cores: 4'
        echo '    big_mem_per_core_gb: "30G"'
        ) >> /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/PathoFact/config.yaml

        snakemake -s Snakefile --use-conda --reason --cores $2 -p
done
