#!/bin/bash
#SBATCH -J Predict-nnunet
#SBATCH -p short
#SBATCH --gres=gpu:1
#SBATCH --mem=96g
#SBATCH -o ./job.out
#SBATCH -e ./job.err

#abort on error
set -e

source ~/miniconda3/bin/activate "";
conda activate nnunet5;

export nnUNet_raw_data_base="/homedtic/aperramon/Seg5/nnUNet_raw_data_base"
export nnUNet_preprocessed="/homedtic/aperramon/Seg5/nnUNet_preprocessed"
export RESULTS_FOLDER="/homedtic/aperramon/Seg5/RESULTS_FOLDER"

cd /homedtic/aperramon/Seg5/

nnUNet_predict -i Frame -o Predict_frames -t Task005_LALAA -m 3d_fullres -f all
# nnUNet_predict -i Xabier -o Predictions2 -t Task005_LALAA -m 3d_fullres -f all
# nnUNet_predict -i nnUNet_raw_data_base/nnUNet_raw_data/Task005_LALAA/imagesTs -o Predictions -t Task005_LALAA -m 3d_fullres -f all