#!/bin/bash
#SBATCH -J Train-nnunet
#SBATCH -p high
#SBATCH --gres=gpu:1
#SBATCH --mem=128g
#SBATCH -o ./job.out
#SBATCH -e ./job.err

#abort on error
set -e

source ~/miniconda3/bin/activate "";
conda activate nnunet5;

export nnUNet_raw_data_base="/homedtic/aperramon/Seg5/nnUNet_raw_data_base"
export nnUNet_preprocessed="/homedtic/aperramon/Seg5/nnUNet_preprocessed"
export RESULTS_FOLDER="/homedtic/aperramon/Seg5/RESULTS_FOLDER"

cd /homedtic/aperramon/Seg5/nnUNet_preprocessed/

nnUNet_train 3d_fullres nnUNetTrainerV2 Task005_LALAA all