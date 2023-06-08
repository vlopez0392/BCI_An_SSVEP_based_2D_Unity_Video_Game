import ssvep_preprocessing_API as ssvep_preprocessAPI;
import numpy as np;
from sklearn import svm;
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

### Designed by Victor D. Lopez :)

labels = [8,14,28];
n_subjects = ssvep_preprocessAPI.num_subjects;
n_trials   = ssvep_preprocessAPI.num_trials;
fmin = 1;
fmax = 40;

##1. IO functions
###Load data for all trials and all subjects in a single dataset 
def load_data(frequency,target):
    if frequency not in ssvep_preprocessAPI.SSVEP_frequencies:
        print("Invalid input frequency");
    else:
        if target not in ssvep_preprocessAPI.target_directories:
            print("Invalid target dataset");
        else:
            dataset = [];
            curr_data_path = '';
            curr_raw_dict  = {};
            for subject in range(1, ssvep_preprocessAPI.num_subjects+1):
                curr_data_path = ssvep_preprocessAPI.readSSVEP_FIF_data(subject,frequency,target);
                curr_raw_dict = ssvep_preprocessAPI.create_MNE_Raw(curr_data_path, subject, frequency, ssvep_preprocessAPI.info, 'FIF');
                dataset.append(curr_raw_dict);
            return dataset;

##2. Feature extraction, loading training and label data functions
##Get np.shape of a single raw_dict instance power spectrum from the dataset
def get_train_shape(dataset, fmin, fmax, channels):
    #Get training channels and number of samples
    train_channels = ssvep_preprocessAPI.chooseChannels(channels);
    shape_samples  = len(train_channels)*n_subjects*n_trials;

    #Get raw_dict instance
    raw_dict = dataset[0];
    raw_inst = list(raw_dict.values())[0]; 

    #Determine shape of the features by computing spectrum in the desired frequency range
    shape_features = raw_inst.compute_psd(fmin = fmin, fmax = fmax, picks = train_channels).get_data().shape[1];
    return (shape_samples,shape_features)

## Load training data for a dataset of a given SSVEP frequency.
## You can choose the channels (features) and frequency range from which to load the training data. 
## This function also allows plotting the extracted features for visualization purposes
def load_label_plot_training_data(dataset, channels, frequency, fmin, fmax, plot_channels = False):
    train_channels = ssvep_preprocessAPI.chooseChannels(channels);
    f_min = fmin;
    f_max = fmax;

    #Determine shape of training data:
    train_data_shape = get_train_shape(dataset,f_min,f_max,channels);
    train_data = np.empty(train_data_shape);
    label_data = np.zeros(shape = (train_data_shape[0],1)) + frequency;
    idx = 0;
    for raw_dict in dataset:
        for key, raw_inst in raw_dict.items():
            spectrum = raw_inst.compute_psd(fmin = f_min, fmax = f_max, picks = train_channels);
            if plot_channels:
                spectrum.plot();
                plt.title(key);
                plt.show();
            else:
                curr_data = spectrum.get_data();
                for j in range(0,len(train_channels)):
                    train_data[idx] = curr_data[j]
                    idx+=1;
    return [train_data, label_data];

def make_training_label_dataset(target, channels):
   current_dataset = [];
   dataset_sequence = []
   for frequency in ssvep_preprocessAPI.SSVEP_frequencies:
       current_dataset = load_data(frequency,target);
       curr_train_label = load_label_plot_training_data(current_dataset,channels,frequency,fmin,fmax, plot_channels=False); 
       dataset_sequence.append(curr_train_label);

   train_dataset = np.concatenate([dataset_sequence[0][0],dataset_sequence[1][0], dataset_sequence[2][0]])
   label_dataset = np.concatenate([dataset_sequence[0][1],dataset_sequence[1][1], dataset_sequence[2][1]])

   return [train_dataset,label_dataset];

def learning_pipeline(train_label_dataset):
    X = train_label_dataset[0]; ## Training data
    y = train_label_dataset[1]; ## Labels for each training sample
    


