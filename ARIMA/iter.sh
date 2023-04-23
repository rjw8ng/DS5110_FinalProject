#!/usr/bin/env bash
#SBATCH --job-name="iter"
#SBATCH --output=arima_slurm_outputs/iter.out
#SBATCH --error=arima_slurm_outputs/iter.err
#SBATCH --partition=gpu
#SBATCH --time=3:00:00
#SBATCH --account=ds--6013
#SBATCH --gres=gpu
#SBATCH --mem=32GB

module load anaconda

python iter.py