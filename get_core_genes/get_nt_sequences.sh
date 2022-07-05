#!/bin/bash

input=$1
output=$2

if [ "$#" -lt 2 ]; then
    echo "The script needs input file and output directory as params"
    exit 1
fi

echo "retriving nt_sequences..."

while read SGB;
do
        echo "reading SGB: ${SGB}"
        python /shares/CIBIO-Storage/CM/scratch/projects/nkarcher_FMT_meta/scripts/uniref90_pangenome/get_core_genes_nt.py --sgb $SGB --output $output -r Jan21
done < $input
