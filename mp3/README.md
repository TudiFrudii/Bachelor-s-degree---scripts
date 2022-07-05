`run_mp3.sh` is the executable that alloex analysis with mp3.
This script needs to be placed inside the directory of mp3 installation.
This script requires three arguments:
- global input direcroty which containd file as "{SGB}_50.fasta". These files can be also in subdurectories.
These files are generated from /shares/CIBIO-Storage/CM/scratch/users/aitor.blancomiguez/tests/chocophlansgb/uniref90_pangenome/get_core_genes.py script. See *cartella con lo script* for information on how to get these files.
- minimum length of the sequence (for metagenomic sets 50 is suggested)
- threshold (suggested 0.2)