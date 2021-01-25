#!/bin/bash
#SBATCH -J Train-nnunet
#SBATCH -p high
#SBATCH --gres=gpu:1
#SBATCH --time=infinite
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

cd /homedtic/xmorales/Seg/nnUNet_preprocessed/

nnUNet_train 3d_lowres nnUNetTrainerV2 Task001_LALAA 0
nnUNet_train 3d_lowres nnUNetTrainerV2 Task001_LALAA 1
nnUNet_train 3d_lowres nnUNetTrainerV2 Task001_LALAA 2
nnUNet_train 3d_lowres nnUNetTrainerV2 Task001_LALAA 3
nnUNet_train 3d_lowres nnUNetTrainerV2 Task001_LALAA 4

nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes Task001_LALAA 0
nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes Task001_LALAA 1
nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes Task001_LALAA 2
nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes Task001_LALAA 3
nnUNet_train 3d_cascade_fullres nnUNetTrainerV2CascadeFullRes Task001_LALAA 4