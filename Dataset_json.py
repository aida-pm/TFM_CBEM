# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:59:49 2020

@author: javi485
"""

from collections import OrderedDict
from batchgenerators.utilities.file_and_folder_operations import *
import numpy as np
import os
import json
import re
import shutil


if __name__ == "__main__":
    folder_training = "/Training"
    folder_test = "/Testing"
    output_folder = "/Seg/nnUNet_raw_data_base/nnUNet_raw_data/Task001_LALAA/"
    
    maybe_mkdir_p(join(output_folder, "imagesTr"))
    maybe_mkdir_p(join(output_folder, "imagesTs"))
    maybe_mkdir_p(join(output_folder, "labelsTr"))
    maybe_mkdir_p(join(output_folder, "labelsTs"))
    
    # train
    all_train_files = []
    data_files_train = [i for i in subfiles(folder_training, suffix=".nii.gz")if i.find("_1.nii.gz")==-1]
    corresponding_seg_files = [i[:-7] + "_1.nii.gz" for i in data_files_train]
    for d, s in zip(data_files_train, corresponding_seg_files):
        patient_identifier = d.split("/")[-1][:-7]
        all_train_files.append(patient_identifier + "_0000.nii.gz")
        shutil.copy(d, join(output_folder, "imagesTr", patient_identifier + "_0000.nii.gz").replace("\\","/"))
        shutil.copy(s, join(output_folder, "labelsTr", patient_identifier + ".nii.gz").replace("\\","/"))
            
    # test
    all_test_files = []
    data_files_test = [i for i in subfiles(folder_test, suffix=".nii.gz") if i.find("_1.nii.gz")==-1 ]
    corresponding_seg_files_ts = [i[:-7] + ".nii.gz" for i in data_files_test]
    for d in data_files_test:
        patient_identifier = d.split("/")[-1][:-7]
        all_test_files.append(patient_identifier + "_0000.nii.gz")
        shutil.copy(d, join(output_folder, "imagesTs", patient_identifier + "_0000.nii.gz").replace("\\","/"))
        shutil.copy(s, join(output_folder, "labelsTs", patient_identifier + ".nii.gz").replace("\\","/"))
        
    json_dict = OrderedDict()
    json_dict['name'] = "NZ"
    json_dict['description'] = "Burdeos dataset Left Atrium CT"
    json_dict['tensorImageSize'] = "3D"
    json_dict['reference'] = "see ACDC challenge"
    json_dict['licence'] = "see ACDC challenge"
    json_dict['release'] = "0.0"
    json_dict['modality'] = {
        "0": "CT"
    }
    json_dict['labels'] = {
        "0": "background",
        "1": "LALAA"
    }
    json_dict['numTraining'] = len(all_train_files)
    json_dict['numTest'] = len(all_test_files)
    json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i.split("/")[-1][:-12], "label": "./labelsTr/%s.nii.gz" % i.split("/")[-1][:-12]} for i in
                             all_train_files]
    json_dict['test'] = ["./imagesTs/%s.nii.gz" % i.split("/")[-1][:-12] for i in all_test_files]

    save_json(json_dict, os.path.join(output_folder, "dataset.json"))
