import scipy.io 
import mne
import numpy as np #asrpy requires numpy version < 1.24.0 
import matplotlib.pyplot as plt
import os
from asrpy import ASR
from mne.preprocessing import ICA;
import sklearn
import mne_icalabel

### Designed by Victor D. Lopez :)

#EEG system data
n_channels = 128
sampling_freq = 256
biosemi128 = mne.channels.make_standard_montage("biosemi128");
info = mne.create_info(biosemi128.ch_names, sfreq=sampling_freq, ch_types="eeg");
num_trials = 5;
num_subjects = 4;
SSVEP_frequencies = [8,14,28]

##SSVEP channels of interest
O1 = ['A13','A14','A15','A16'];
O2 = ['A26','A27','A28','A29'];
P3 = ['A5', 'A18'];
P4 = ['A31','A32'];
PZ = ['A19','A20'];
P7 = ['A8','A9','A10','A11','A12'];
P8 = ['B5','B6','B7','B8','B9']
CP1 = ['D16','D17']
CP2 = ['B2','B19']
eeg_channels = [O1,O2,P3,P4,PZ,P7,CP1,CP2];
eeg_channels_keys = ['O1','O2','P3','P4','PZ','P7','CP1','CP2'];

#ICA parameters 
n_components = 35;
seed = 42;

###IO FUNCTIONALITY and HELPER FUNCTIONS
###Target directories to output eeg data
target_directories = ['RAW','FILT','ASR']
file_types = ['MAT', 'FIF']

##HELPER FUNCTIONS
##Checks that input subject number and input SSVEP frequencies are valid
def assertSubjectFrequency(frequency, subject):
    isCorrectSubject = False;
    isCorrectFrequency = False;

    if subject>0 and subject <= num_subjects:
        isCorrectSubject = True;
    if frequency in SSVEP_frequencies:
        isCorrectFrequency = True;

    return isCorrectSubject and isCorrectFrequency;

##Generate keys for desired subject and frequency. Returns a list with the keys
def generateKeys(subject, frequency):
    key_list = [];
    if(assertSubjectFrequency(frequency, subject)):
        currkey = '';
        trial = 1;
        frequency = str(frequency) + 'Hz';
        for i in range(1,num_trials+1):
            currkey = 'sub' + str(subject) + '_' + frequency + '_trial' + str(trial);
            trial+=1;
            key_list.append(currkey);
    else:
        print("Input frequency or subject not found. Try again")
    
    return key_list;

def generateStages(stage):
    if stage == 'all':
        return ['all']
    else:
        stages = [];
        available_stages = ['raw', 'filter']
        for st in available_stages:
            stages.append(st);
            if st == stage:
                break
        
        return stages;

def printProcessingStatus_trial(subject, frequency):
    print("-----------------------------------------------------------------------------------------");
    print("NOW PROCESSING SUBJECT: " + str(subject) + " at SSVEP FREQUENCY: " + str(frequency) + "Hz");
    print("-----------------------------------------------------------------------------------------");

def printProcessingStatus_key(key):
    print("-----------------------------------------------------------------------------------------");
    print("NOW PROCESSING: " + key);
    print("-----------------------------------------------------------------------------------------");

## IO
## Returns .mat file paths for the desired subject and frequency
def readSSVEP_MAT_data(subject, frequency):
    path_list = [];

    if(assertSubjectFrequency(frequency, subject)):
        SSVEPdatapath = 'SSVEP_' + str(frequency) + 'Hz';
        cwd_path = os.path.join(os.getcwd(),SSVEPdatapath,'SUB'+str(subject));

        for trial in range(1,num_trials+1):
            file = SSVEPdatapath+'_Trial'+str(trial)+'_SUBJ'+str(subject)+'.MAT';
            curr_trial_file_path = os.path.join(cwd_path,file);
            path_list.append(curr_trial_file_path);
    else:
        print("Input frequency or subject not found. Try again")

    return path_list;

def readSSVEP_FIF_data(subject, frequency, target):
    path_list = [];

    if(assertSubjectFrequency(frequency, subject)):
        if target in target_directories:
            cwd_path = os.path.join(os.getcwd(),target,str(frequency)+'Hz','SUB'+str(subject));

            SSVEPfilepath = target+'_SSVEP'+'_sub'+str(subject)+'_'+str(frequency)+'Hz';
            for trial in range(1,num_trials+1):

                file = SSVEPfilepath+'_trial'+str(trial)+'_raw.fif';
                curr_trial_file_path = os.path.join(cwd_path,file);
                path_list.append(curr_trial_file_path);
        else: 
            print('Target directory is not supported');
    else:
        print("Input frequency or subject not found. Try again")

    return path_list;

#Output clean data in .fif format to the target directory;
def saveEEGdata(brain_source_data_dict, target_dir):
    raw_dict = dict();
    t_path = '';
    if target_dir in target_directories:
        ic_key = '';
        for frequency in SSVEP_frequencies:
            for subject in range(1,num_subjects+1):
                ic_key = 'sub' + str(subject) + '_' + str(frequency)+'Hz';

                raw_dict = brain_source_data_dict[ic_key];
                for key, rawObject in raw_dict.items():
                  t_path = os.path.join(os.getcwd(),target_dir,str(frequency)+'Hz','SUB'+str(subject),target_dir+'_SSVEP_'+key+'_raw.fif');
                  rawObject.save(t_path, overwrite = True);
    else:
        print('Target directory is not supported');

########################################### PREPROCESSING Pipeline #######################################
## 1. Raw data
## Specify the type of file to read (either .mat or .fif)
## Create MNE Raw Objects for each .mat file for the chosen subject and frequency
## Create MNE Raw Objects for each .fif file for the chosen subject and frequency

def create_MNE_Raw(path_list, subject, frequency, info, filetype):
    if not path_list:
        print("Empty path list. Try again")
        return None;
    else:
        if filetype in file_types:
            data_dict = {}
            file_idx = 0;
            keyList = generateKeys(subject, frequency);
            key = '';

            if filetype == 'MAT':
                for matfile in path_list:
                    key = keyList[file_idx]
                    data = scipy.io.loadmat(matfile);
                    np_arr = np.array(data['EEGdata']);
                    data_dict[str(key)] = mne.io.RawArray(np_arr,info);
                    data_dict[str(key)].set_montage(biosemi128);
                    file_idx+=1;
            
            elif filetype == 'FIF':
                for FIFfile in path_list:
                    key = keyList[file_idx]
                    data_dict[str(key)] = mne.io.read_raw_fif(FIFfile);
                    file_idx+=1;
            
            return data_dict;
        else:
            print("Unknown file type. Please input either .mat or .fif files only")
            return None;

## 2. Filtering data - Bandpass filter 1-50 Hz
## - Input a dictionary of mne Raw objects 
## - Outputs a dictionary of the filtered mne Raw objects 
def bandpassFilter(rawDict, l_freq, h_freq):
    filtered_dict = {};
    for key,rawArray in rawDict.items():
        filtered_dict[key] = rawArray.filter(l_freq, h_freq, picks = 'eeg'); # l_freq < h_freq -> passband filter
    return filtered_dict;

## 3. ASR - Input: A Raw array. Either raw eeg data or previously filtered eegdata
##        - Output: Raw onbject transformed by ASR
def applyASR(rawDict , cutoff):
    asr_dict = {};
    print("Applying ASR...")
    asr = ASR(sampling_freq, cutoff=cutoff);
    for key,rawArray in rawDict.items():
        asr.fit(rawArray);
        asr_dict[key] = asr.transform(rawArray);
    return asr_dict;

## 4. ICA and ICLabel
def applyICA(rawDict, n_components, seed, max_iter):
    ica_dict = {};
    ica = ICA(n_components=n_components, random_state= seed, max_iter =max_iter, method = "infomax", fit_params=dict(extended=True), verbose = False);
    for key,rawArray in rawDict.items():
        rawArray.set_eeg_reference("average");
        ica_dict[key] = ica.fit(rawArray);
    return ica_dict;

### Label each IC 
def labelICA(rawDict, ica):
    labels_prob = dict();
    for key,rawArray in rawDict.items():
        labels_prob[key]= mne_icalabel.iclabel.iclabel_label_components(rawArray,ica[key],True);
    
    return labels_prob;

### Reconstruct brain EEG data from ICs - This is the clean data that will be fed in to the classifier
def reconstruct_eeg_data_ICA(raw_dict , ica_dict, includeOther = True):
    brain_source_data = {};
    include = []
    for key,rawArray in raw_dict.items():
        include = ica_dict[key].labels_['brain'];
        if(includeOther):
            include.extend(ica_dict[key].labels_['other']);
        brain_source_data[key] = ica_dict[key].apply(raw_dict[key], include = include);
    
    return brain_source_data;

### ICA preprocessing pipeline : Input: Subject, frequency, desired stages to process.
### Outputs a list of dictionaries containing the IC data to be labeled or reconstructed
### 
### Parameters: filter_data: Performs bandpass filtering (Set to False only to compare ICAlabel averages)
###             asr_data:    Performs Artifact Subspace reconstruction (Set to False only to compare ICAlabel averages)   
### 
### The data will be completely preprocessed if filter_data and asr_data are set to True (default behavior)
### Very computationally expensive - Call only when hardware acceleration is available

def computeICA_preprocessing_pipeline(filter_data = True, asr_data = True):   
    SSVEP_8Hz_IC  = dict(); 
    SSVEP_14Hz_IC = dict(); 
    SSVEP_28Hz_IC = dict(); 

    ic_key = '';
    for frequency in SSVEP_frequencies:
        for subject in range(1,num_subjects+1):
            printProcessingStatus_trial(subject, frequency);
            ic_key = 'sub' + str(subject) + '_' + str(frequency)+'Hz';
            dict_pair = list();
            ica_dict = dict();

            #Read SSVEP data paths
            path_list = readSSVEP_MAT_data(subject, frequency);

            #1. Create Raw data dictionary for all trials
            raw_dict = create_MNE_Raw(path_list, subject, frequency, info, 'MAT');
            if not filter_data and not asr_data:
                ica_dict = applyICA(raw_dict, n_components, seed, 1000);
                dict_pair = [ica_dict,raw_dict]
            #2. Filter data
            if filter_data:
                filtered_dict = bandpassFilter(raw_dict, 1, 50);
                if not asr_data:
                    ica_dict = applyICA(filtered_dict, n_components, seed, 1500);
                    dict_pair = [ica_dict,filtered_dict]

            # #3 Perform ASR
            if asr_data:
                if subject == 4 and frequency == 14: ##ASR rejects this data - Consider filtered data only
                    ica_dict = applyICA(filtered_dict, n_components, seed, 1500);
                    dict_pair = [ica_dict,filtered_dict]
                    pass
                else:    
                    asr_dict = applyASR(filtered_dict, cutoff=20);
                    ica_dict = applyICA(asr_dict, n_components, seed,2000);
                    dict_pair = [ica_dict,asr_dict]
            
            if frequency == 8:
                SSVEP_8Hz_IC[ic_key] = dict_pair;
            elif frequency == 14:
                SSVEP_14Hz_IC[ic_key] = dict_pair;
            elif frequency == 28:
                SSVEP_28Hz_IC[ic_key] = dict_pair;

    return [SSVEP_8Hz_IC, SSVEP_14Hz_IC, SSVEP_28Hz_IC];

#Use ICA label to label all the computed ICs
def ICAlabel_preprocessing_pipeline(ICA_SSVEP_list):
    for j in range(0, len(ICA_SSVEP_list)):
        for key,dict_pair in ICA_SSVEP_list[j].items():
            printProcessingStatus_key(key);
            ica_dict = dict_pair[0];
            raw_dict = dict_pair[1];            
            labelICA(raw_dict, ica_dict);

#Compute ICA averages of labeled data 
# - Input : A previously labeled dataset by ICAlabel 
# - Output: A dictionary indexed by subject and SSVEP frequency whose values are IClabel averages indexed
#   by brain source or artifact     
def compute_ICAlabel_averages(labeled_SSVEP_list):
    average_label_dict = dict();
    for j in range(0, len(labeled_SSVEP_list)):
        for key,dict_pair in labeled_SSVEP_list[j].items():
            ica_dict = dict_pair[0];
            curr_label_dict = dict();
            acc_list = list();
            average_values = list();
            isEmpty = True;

            for ic_key in ica_dict.keys():
                if isEmpty:
                    acc_list = [0]*len(list(ica_dict[ic_key].labels_));
                    isEmpty = False;

                curr_label_dict = ica_dict[ic_key].labels_.copy();
                curr_label_dict = {k: len(v) for k, v in curr_label_dict.items()}
                acc_list = [acc_list[v] + list(curr_label_dict.values())[v] for v in range (len(acc_list))]  
            
            average_values = [value//num_trials for value in acc_list]
            average_label_dict[key] = dict(zip(dict.fromkeys(curr_label_dict),average_values));
    
    return average_label_dict;

#Reconstruct eeg data from ICA and save clean data to .fif format
def reconstructEEG_preprocessing_pipeline(labeled_SSVEP_list, includeOther = True):
    ic_key = '';
    idx = 0 
    ica_dict = dict();
    brain_source_data_dict = dict();

    for frequency in SSVEP_frequencies:
        for subject in range(1,num_subjects+1):
            ic_key = 'sub' + str(subject) + '_' + str(frequency)+'Hz';
            ica_dict = labeled_SSVEP_list[idx][ic_key][0];
            raw_dict = labeled_SSVEP_list[idx][ic_key][1];
            printProcessingStatus_key(ic_key);

            #Apply ICA 
            curr_brain_data = reconstruct_eeg_data_ICA(raw_dict , ica_dict, includeOther);
            brain_source_data_dict[ic_key] = curr_brain_data;

        idx+=1;
    return brain_source_data_dict;

###PLOTTING FUNCTIONALITY
def chooseChannels(channel_list):
    channel_dict = dict(zip(eeg_channels_keys,eeg_channels));
    chosen_channels = [];

    for key in eeg_channels_keys:
        if key in channel_list:
            chosen_channels.extend(channel_dict[key]);

    return chosen_channels;

###Plot RawData - Input a dictionary of mne Raw objects and the number of trials you want to display.
###             - Outputs auto-scaled raw data for the selected subject and SSVEP frequency
def plot_Raw_data(rawDict, trials, pick_channels):
    if trials > 0 and trials <= num_trials:
        key_list = list(rawDict.keys());
        key_list.sort();

        currKey = '';
        for trial in range(0,trials):
            currKey = key_list[trial];
            rawDict[currKey].plot(scalings = 'auto' , title = currKey);
            plt.show();
    else: 
        print("Invalid number of trials");
        return None;

###Plot PSD - Input dictionary of mne Raw objects and in the desired frequency range
###         - Outputs power spectrum plots of all trials of a given subject and SSVEP frequency
def plot_Raw_PSD(rawDict, fmin, fmax, pick_channels = None, average = True):
    if pick_channels is not None:
        pick_channels = chooseChannels(pick_channels)

    for key,data in rawDict.items():
          spec = data.compute_psd(average = 'mean',fmin = fmin, fmax = fmax, picks = pick_channels);
          spec.plot(picks='data', exclude='bads',average = average);    
          plt.title(key);
    plt.show();

###Plot sources - ICA - Input dictionary of ICA objects given the desired frequency and subject and trials
###############       - Outputs an time series IC data plot
def plot_ICA_sources(subject, frequency, trials, ica_dict, raw_dict):
    if(assertSubjectFrequency(frequency, subject)):
        if trials > 0 and trials <= num_trials: 
            key_list = list(ica_dict.keys());
            key_list.sort();
        
            currKey = '';
            for trial in range(0,trials):
                currKey = key_list[trial];
                ica_dict[currKey].plot_sources(raw_dict[currKey], title = currKey);
        else:
            print(print("Invalid number of trials"));
            return None;
    else:
        print("Input frequency or subject not found. Try again")
        return None;

### Plot sensor locations
def plot_sensor_locations():
    #Get raw instance 
    path = readSSVEP_FIF_data(1, 8, 'RAW')[0];
    raw_inst = mne.io.read_raw(path);
    raw_inst.plot_sensors(show_names = True, ch_type = 'eeg', ch_groups = 'position');
    plt.show();















