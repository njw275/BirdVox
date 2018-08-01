#!/bin/bash

#BATCH --job-name=medianfilt_onsetsAndPeaks
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=3:45:00
#SBATCH --mem=10GB
#SBATCH --mail-type=END
#SBATCH --mail-user=njw275@nyu.edu
#SBATCH --output=slurm_medianfilt_onsetsAndPeaks_%j.out

module purge
source activate birds

cd /home/njw275/NJW-BirdVox/src/python_files/
python medianfilt_onsetsAndPeaks.py
