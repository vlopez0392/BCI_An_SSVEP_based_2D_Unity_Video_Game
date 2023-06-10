import ssvep_preprocessing_API as ssvep_preprocessAPI
import ssvep_model as model
import sys

##Plot arguments
PSD_args_len = 5;
PTIME_args_len = 6;
PSD_args =  ['-plot', '-psd']
PTIME_args = ['-plot', '-time']
target_directories = ['-raw', '-filt','-asr'];
MODEL_args = ['-raw','-asr'];
MODEL_plots = ['-features','-confusion'];

def main():
    if len(sys.argv) < 2:
        print("Fatal Error: Please enter at least five arguments");
    else:
        args_in = sys.argv[1:]
        if args_in[0] == '-plot' and (args_in[1] == '-time' or args_in[1] == '-psd') :
            if len(args_in) < 5:
                print("Fatal Error: Please input at least five arguments in the correct format.")
            else:     
                subject = int(args_in[2]);
                frequency = int(args_in[3])
                if ssvep_preprocessAPI.assertSubjectFrequency(frequency,subject):
                    target = args_in[4]
                    if target not in target_directories:
                        print("Fatal Error: Please input a correct dataset parameter: -raw , -filt , or -asr");
                    else:
                        target = target[1:].upper();
                        path_list = ssvep_preprocessAPI.readSSVEP_FIF_data(subject, frequency,target);
                        raw_dict  = ssvep_preprocessAPI.create_MNE_Raw(path_list,subject,frequency,ssvep_preprocessAPI.info,'FIF');
                        #Plot PSD
                        if len(args_in) == PSD_args_len and args_in[1] == '-psd':
                            ssvep_preprocessAPI.plot_Raw_PSD(raw_dict, fmin = frequency - 8, fmax= frequency+10, pick_channels=None, average= False);
                        
                        #Plot EEG Time series 
                        elif (len(args_in) == PSD_args_len or len(args_in) == PTIME_args_len) and args_in[1] == '-time': 
                            if len(args_in) == PTIME_args_len:
                                num_trials = int(args_in[5])
                            else:
                                num_trials = 1;
                            if num_trials < 1 or num_trials > ssvep_preprocessAPI.num_trials:
                                print("Fatal Error: Invalid number of trials.")
                            else:
                                ssvep_preprocessAPI.plot_Raw_data(raw_dict,num_trials,None);
                        else:
                            print("Fatal Error: Please enter input arguments correctly");
                else:
                    print("Fatal Error: Input invalid subject, frequency");
        elif args_in[0] == '-model':
            if len(args_in) < 3:
                print("Fatal Error: Please input exactly three arguments in the correct format.")
            else:
                target = args_in[1];
                if target not in MODEL_args:
                    print("Fatal Error: Please input a correct dataset parameter: -raw or -asr");
                else:
                    plot_model = args_in[2];
                    if plot_model not in MODEL_plots:
                        print("Fatal Error: Please input a correct plot type parameter: -features or -confusion");
                    else:
                        frequency = 8;
                        subject   = 1;
                        target = target[1:].upper();
                        dataset = model.load_data(frequency,target);
                        channels = ['O1','O2'];
                        if plot_model == '-features':
                            model.load_label_plot_training_data(dataset,channels,frequency,1,40,True);
                        else:
                            train_label_dataset = model.make_training_label_dataset(target,channels);
                            model.SVM_pipeline(train_label_dataset, True);
        else:
            print("Fatal Error: Please enter input arguments correctly");
main();