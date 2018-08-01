#!/bin/bash

#BATCH --job-name=retrieve
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0:10:00
#SBATCH --mem=1GB
#SBATCH --output=slurm_retrieve_%j.out

module purge
source activate birds

cd /scratch/njw275/python_files/
python RetrievalFunction.py
