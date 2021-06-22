# TFM_CBEM
Github repository for the final master project (TFM) on the Automatic segmentation of the left atrium and left atrial appendage in 4D-flow magnetic resonance imaging data.

## Contains
- preprocess.sh: run the pre-processing of the U-Net by means of the nnU-Net framework
- training.sh: run the training of the U-Net by means of the nnU-Net framework
- predict.sh: run inference using the U-Net model trained by means of the nnU-Net framework
- downsampling.ipynb: convert the CT scans to resolution 128x128
- upsampling.ipynb: reverse convert the CT scans to their original resolution
- change background 4dflow.ipynb: remove background in the 4D-flow segmentations
- changespacing_4Dflow.ipnyb: convert the 4D flow data to the same spacing the nnU-Net infers to CTs
- conversor_of_format_nnunet.ipynb: code to convert files to .nii.gz or .nrrd format
- metrics_network.ipynb: compute Dice score, Hausdorff distance and contour-Dice for testing data. #credits to Kristine A. Juhl for the contour-Dice score.

## Contact
Any comments on the code, please contact Aida Perramon Malavez.
aida.perramon01@estudiant.upf.edu
