#!/usr/bin/env bash
#SBATCH --job-name="aggregate"
#SBATCH --output=slurm_outputs/csv_to_one_df.out
#SBATCH --error=slurm_outputs/csv_to_one_df.err
#SBATCH --partition=gpu
#SBATCH --time=3:00:00
#SBATCH --account=ds--6013
#SBATCH --gres=gpu
#SBATCH --mem=32GB

module load anaconda

python csv_to_one_df.py