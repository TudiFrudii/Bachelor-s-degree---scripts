`run_pathofact.sh` is the script that allows using Pathofact on a set of SGBs.
This screept neeeds to be placed inside the PathoFact directory of its installation.
/shares/CIBIO-Storage/CM/scratch/users/vittoria.ossanna/PathoFact/config.yaml
will be modified each time in order to run PathoFact.

In order to run, Pathofact needs a directory containing *n* subdirectories with the SGBs' ID. In each subfolder a file "{SGB}_50.fna" is needed.
Please notice that the extension .fna is compulsory, therefore you could need to rename files coming from /shares/CIBIO-Storage/CM/scratch/users/aitor.blancomiguez/tests/chocophlansgb/uniref90_pangenome/get_core_genes_nt.py 
In this script there are some variables that could need to be changed as the path for SignalP.

The scritp needs two args:
- input direcroty
- cores

In order for PathoFact to run you need to acrivate conda environment before running
`conda activate PathoFact`

Outputs will be collected inside each input subfolder