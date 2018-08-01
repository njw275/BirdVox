#!/bin/bash

#BATCH --job-name=add
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0:10:00
#SBATCH --mem=1GB
#SBATCH --output=slurm_add_%j.out

module purge

module pandas

cd ~/scratch/njw275/
python splitAndEvaluate.py
