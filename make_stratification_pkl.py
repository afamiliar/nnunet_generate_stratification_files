from collections import OrderedDict
import pandas as pd
import numpy as np
import pickle

sub_df = pd.read_csv('stratification_train_val.csv')

out_list = []
for fold in [1,2,3,4,5]:
# for fold in [1]:
    # Create an empty OrderedDict
    ordered_dict = OrderedDict()
    # get the subject assignments for this fold
    sub_fold_df = sub_df[['SubjectID',f'FOLD_{fold}']]
    # initialize lists
    train_list = []
    val_list = []
    # generate a dictionary of arrays for training/validation subjects
    # and update output list
    for ind,row in sub_fold_df.iterrows():
        sub_id = row['SubjectID']
        class_id = row[f'FOLD_{fold}']
        for image_type in [1,2,3,4]: # add separate input for each of the 4 images
            if class_id == 'train':
                train_list.append(f'{sub_id}_{image_type}')
            elif class_id == 'val':
                val_list.append(f'{sub_id}_{image_type}')
    train_array = np.array(train_list)
    val_array = np.array(val_list)
    ordered_dict['train'] = train_array
    ordered_dict['val'] = val_array
    out_list.append(ordered_dict)

# save output to pkl (nnunet-v1)
with open('splits_final_new.pkl', 'wb') as f:
   pickle.dump(out_list, f)
