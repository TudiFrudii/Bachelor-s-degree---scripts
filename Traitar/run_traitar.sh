#!/bin/bash

input=$1
output_dir=$2
queue=$3

if [ "$#" -lt 3 ]; then
    echo "The script needs input file, directory of output and queue as params"
    exit 1
fi

logs_dir=$2
traitar_script=/shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/prova_traitar2/traitar.pbs

mkdir -p $logs_dir
while read sgb; do
    if [ "$queue" == "short_cpuQ" ]; then
        queued_proc=`qstat -u $USER short_cpuQ | wc -l`
        while [[ $queued_proc -gt 34 ]]
        do
            sleep 5m
            queued_proc=`qstat -u $USER short_cpuQ | wc -l`
        done
    fi


    qsub -q ${queue} -l mem=4GB -o ${logs_dir}/${sgb}.o -e ${logs_dir}/${sgb}.e -l ncpus=1 -v sgb=${sgb},out=${output_dir} ${traitar_script}
done < $input