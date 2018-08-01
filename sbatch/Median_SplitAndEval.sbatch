#!/bin/bash

#BATCH --job-name=Median_SplitAndEval
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --mem=12GB
#SBATCH --mail-type=END
#SBATCH --mail-user=njw275@nyu.edu
#SBATCH --output=slurm_Median_SplitAndEvaluate_%j.out

module purge
source activate birds

cd /home/njw275/NJW-BirdVox/src/python_files/
python Median_SplittingandEvaluating.py
