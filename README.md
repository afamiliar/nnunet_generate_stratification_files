## Example for creating pickle file needed by nnUnet when stratifying inputs into training/validation across folds for model training

[See nnUnet documentation here](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/manual_data_splits.md)

In this example there are 5 folds. Each subject has 4 input files that need to be grouped into either train or validation sets but not both (listed as "CID_1" "CID_2" "CID_3 "CID_4" in train/val file).

Manually defined split is in the CSV file which is picked up by `make_stratification_pkl.py`