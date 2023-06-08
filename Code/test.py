import ssvep_preprocessing_API as ssvep_preprocessAPI
import ssvep_model as model

def main():
    channels = ['O1','O2'];
    train_label_dataset = model.make_training_label_dataset('RAW',channels);
    model.SVM_pipeline(train_label_dataset)
main();