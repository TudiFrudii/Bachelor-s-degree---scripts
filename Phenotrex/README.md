`run_phenotrex.sh` is the script that allows to run phenotrex on multiple data. 
In order to use phenotrex you need to activate a conda environment `conda activate vossanna_phenotrex`
This script needs two arguments:
- input directory (as a set os subdirectories {SGBs} containig file as {SGB}.fasta)
- output directory

The script will create a tree of subdirectory automatically.

This script could need to be changed internally if you want to run different classifiers.
The classifiers I used are in /shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/Phenotrex/classifiers/class_of_interest
