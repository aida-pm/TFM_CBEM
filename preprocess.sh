#!/bin/bash
#SBATCH -J Pre-nnunet
#SBATCH -p high
#SBATCH -c 1
#SBATCH --mem=128g
#SBATCH -o ./job.out
#SBATCH -e ./job.err

#abort on error
set -e

source ~/anaconda3/bin/activate "";
conda activate nunet;

export nnUNet_raw_data_base="/homedtic/xmorales/Seg/nnUNet_raw_data_base"
export nnUNet_preprocessed="/homedtic/xmorales/Seg/nnUNet_preprocessed"
export RESULTS_FOLDER="/homedtic/xmorales/Seg/RESULTS_FOLDER"

cd /homedtic/xmorales/Seg/nnUNet_raw_data_base/nnUNet_raw_data/

nnUNet_plan_and_preprocess -t 001