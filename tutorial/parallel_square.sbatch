#!/bin/bash

#BATCH --job-name=parsquare
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=0:10:00
#SBATCH --mem=1GB
#SBATCH --output=slurm_parsquare_%j.out

module purge

cd ~/NJW-BirdVox/src
python parallel_square.py
