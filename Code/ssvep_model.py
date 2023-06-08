import ssvep_preprocessing_API as ssvep_preprocessAPI;
import numpy as np;

##IO functions
###Load data for all trials
def load_data(frequency):
    if frequency not in ssvep_preprocessAPI.SSVEP_frequencies:
        print("Invalid frequency");
    else:
        dataset = {};
        curr_data_path = '';
        curr_raw_dict  = {};
        for subject in range(1, ssvep_preprocessAPI.num_subjects+1):
            curr_data_path = ssvep_preprocessAPI.readSSVEP_FIF_data(subject,frequency,'ASR');
            curr_raw_dict = ssvep_preprocessAPI.create_MNE_Raw(curr_data_path, subject, frequency, ssvep_preprocessAPI.info, 'FIF');
            dataset[subject] = curr_raw_dict;
        return dataset;

## Load training data for a dataset of a given SSVEP frequency.
## You can choose the channels from which to load the training data 
## The desired subjects to be loaded must be input as a list of the form [a,b,c]
def load_training_data(dataset, channels, list_subjects):
    valid_subject_list = False;
    for subject in list_subjects:
        if subject >= 1 and subject <= ssvep_preprocessAPI.num_subjects:
            valid_subject_list = True;
    
    if valid_subject_list:
        training_data_channels = ssvep_preprocessAPI.chooseChannels(channels);

        if subject in list_subjects:
            for k,raw_dict in dataset[subject]:
                for key, raw_inst in raw_dict.items():
                    pass;
    else:
        print("Subject not found in provided subject list");


