<h1>Spring 2023 Brain Computer Interfaces: Fundamentals and Applications Final Project, NTHU, Taiwan</h2>

<h2 align="center">1. Project members and Demo Video</h2>
<h3>1.1. Members</h3>
<h3> * 巫冠緯           - 111065543  </h3>
<h3> * Wu, Shao-Hung	 - 111062640  </h3>
<h3> * Victor D. Lopez - 110062426  </h3>
<h3>1.2 Demo video</h3>
<p align="center">
  <img src="/Figures/usage/demo_video.png" style="width: 80%;">
</p>
<p align="justify">
Demo video link on Drive: <a href ="https://drive.google.com/drive/folders/15Yd4443tgOLVJZ8FmqVolhtWGg87aLyy?usp=drive_link">Demo video</a>
</p>
<p align="justify">
Demo video link on Youtube: <a href ="https://youtu.be/I1fgnRXkMjg">Demo video</a>
</p>

---

<h2 align="center">2. Introduction</h2>
<p align="justify">The aim of this project is to develop a functional BCI system such that it can be integrated to a commercial application. More specifically to a video game. From a publicly available SSVEP dataset, we apply the usual steps of a Machine Learning pipeline such as data preprocessing, feature extraction and feature classification. We provide a detailed report of our findings, software design and implementation, required dependencies, and usage among others.
</p>
<p align="justify">
The sections of this report are as follows: Section 3 provides the dataset description and data quality evaluation and justification. Section 4 provides the BCI system architecture. Section 5 provides the methods that validate our findings and our system. Section 6 provides usage examples of the developed software for the BCI system. Section 7 provides our findings and results and finally, Section 8 provides the consulted references.</p>

---

<h2 align="center">3. Data description</h2>
<h3>3.1 Experimental design and dataset overview </h3>
<p align="justify">As required by the final project guidelines, we first describe the experimental design/paradigm, procedure for collecting data, hardware and software used, data size, number of channels, sampling rate, the website from which our data was collected, the owner and its source.</p>

<ul>
  <li align="justify">
    <ins>Number of channels</ins>: 128-channels BIOSEMI (Active electrodes) where the cap layout is found in reference [1]. The electrode placement layout is shown below: 
    <br/>
    <br/>
    <br/>
    <p align="center">
      <img src="/Figures/Sensor_positions/sensor_locations.png" style="width: 75%;">
    </p>
  </li>
  <br/>
  <li align="justify">
    	<ins>Data size</ins>: 
      <ul>
        <li align="justify">Number of subjects: 4</li>
        <li align="justify">Number of trials per subject: 5 </li>
        <li align="justify">Number of SSVEP stimulation frequencies available: 8 Hz, 14 Hz, 28 Hz</li>
      </ul>
  </li>
  <br/>
  <li align="justify"><ins>Website where the data was collected</ins>: The data was collected from the website provided in reference [2]. </li>
   <br/>
  <li align="justify"><ins>Dataset owner</ins>:  Copyright holders of the database are Dr. Hovagim Bakardjian and RIKEN-LABSP [2].</li>
  <br/>
  <li align="justify"><ins>Description of the experimental design, paradigms, and procedure to collect the data</ins>:
    <p align="justify">
      The description of the experimental design is readily provided in reference [3]. In summary, four healthy subjects with corrected       vision or no vision problems and no neurological disorders and no previous training were subjected to SSVEP stimulations at             different frequencies. EEG data was acquired with a 128 active electrode cap found in reference [2]. All the subjects consented         agreement to the experiments under the Declaration of Helsinki [4]. 
    </p>
  </li>
  <li align="justify">
    <ins>Hardware and Software used</ins>:
    <p align="justify">
    The description of the software/hardware used is also readily available in reference [3]. In summary, a 21 in CRT computer monitor (168 ± 0.4 Hz) was placed 90 centimeters from each subject. To achieve SSVEP stimulation, a 6 x 6 checkerboard pattern with flashing black and white reversing squares was used. 
    </p>
  </li>
</ul>
<h3>3.2 Data quality Evaluation</h3>
<p align="justify">
The reliability, credibility and quality of the data sources is justified both theoretically through literature review and by exploring the data ourselves. Then, we make the following claims:
</p>
<ol>
  <li align="justify">The reliability and credibility of the sources is provided through literature review of references [2],[3] and [5]. Part of the dataset used in this project was obtained in experiments conducted reference [3] and whose details have already been thoroughly described in the previous section. </li>
  <br/>
  <li align="justify">The quality of the sources is provided by analyzing the independent components within the EEG data through the MNE library ICA and ICA-label packages in references [6],[7]. We provide the average numbers of ICs classified by ICLabel per SSVEP frequency as required by the final project guidelines in section 7 Results sub -section 7.1.1. In addition, we provide several power spectrum plots in sub-section 7.1.2 to qualitatively compare the the power at the target frequencies between raw, filtered and artificially subspace reconstructed data (ASR).</li>
</ol>

---

<h2 align="center">4. Model Framework</h2>
<p align="justify">
The model framework and architecture of our project is based on a typical SSVEP-based BCI system architecture. Reference [13] provides a nice figure of the model architecture which is shown below:
</p>
  <p align="center">
    <img src="/Figures/usage/architecture.png" style="width: 75%;" >
  </p>
  <p align="justify">
  Since our data is extracted from the dataset described in section 3.1, this project focuses mainly on the following three components:
  </p>
  <ol>
    <li align="justify">Data preprocessing</li>
    <li align="justify">Feature Extraction</li>
    <li align="justify">Feature Classification</li>
  </ol>
  <p align="justify">
  We describe them briefly below. 
  </p>
  <p align="justify">
    <strong>1. Data preprocessing:</strong> From the three signal processing techniques above, data preprocessing is the most time consuming and computationally expensive stage to carry out. As required by the final project guidelines, the following data preprocessing pipeline (shown in green in the figure) was implemented: 
  </p>
  <p align="center">
    <img src="/Figures/usage/pipeline.jpeg" style="width: 85%;">
  </p>
   <p align="justify">
  We have designed a preprocessing API (See section 5.1) to perform the data preprocessing step. It's purpose it's to effectively execute the stages shown in the green rectangle in the figure above by working in conjunction with the Python MNE software library for EEG and MEG data exploration[9]. The raw data from the dataset described in the previous section. Bandpass filtering is applied through the MNE library to eliminate the influence of frequencies above 50 Hz (line noise). 
  </p>
  <p align="justify">
  Artifact subspace reconstruction on the other hand, reduces corrects artifacts such that the resulting data better represent the
  brain EEG signals. The ASR library used in this project is based on reference [8]. Finally ICA and ICA-label allow for the reconstruction of the brain-source dataset (final step) by identifying the ICs corresponding to brain sources and ICA-label allows us to identify the kind of artifacts from every IC.The implemented ICA and ICA-label models are based on references [6] and [7]. Relevant results are provided in Section 7.
  </p>
  <p align="justify">
 <strong> 2. Feature extraction</strong> Once our data has been reconstructed, we may extract features of interest. In our case, we are interested in brain-source EEG signals coming from the visual cortex or the occipital lobe of the brain. From the 10-20 EEG placement system [14], the O1 and O2 electrodes are placed in this region of the brain, thus we extract features as power spectrum density data points from 8 channels from the 128-channel Biosemi montage which roughly correspond to the O1 and O2 electrodes mentioned previously. This feature extraction process is similar to the one conducted in reference [10]. Relevant results are provided in Section 7.
 </p>
 <p align="justify">
<strong> 3. Feature classification </strong> Finally, we implement some machine learning models such as support vector machines (SVMs) to classify each feature according to their specific SSVEP frequency label. We compare the performance of the classifier on several evaluation metrics both on RAW and ASR corrected brain-source datasets to validate both the data preprocessing quality and the effectiveness and reliability of our BCI system. Relevant results are provided in Section 7.
</p>

---

<h2 align="center">5. Validation</h2>
<h2>5.1 Software Design</h2>
<p align="justify">
From the software side, we validate the effectiveness and reliability of our BCI system by relying on many popular python libraries such as numpy, scikit-learn or the MNE library to explore, visualize, and analyze human neurophysiological EEG data [9]. The complete list of dependencies this project relies on is shown in section 6 Usage.
</p>
<p align="justify">
Due to the large size of our dataset, we had to design a data preprocessing API (See the ssvep_preprocessing_API.py module in the Code directory) to parse our data into the appropriate MNE data structures, perform the necessary IO to load the required datasets, save the clean datasets to the appropriate directories, and finally to plot the results shown in section 7 Results. This API is created based on good software practices such as DRY and KISS among others. 
</p>
<p align="justify">
For instance, consider we want to reconstruct brain source EEG data from the ICs computed by ICA. The following code snippet achieves this:
</p>

```
### Reconstruct brain EEG data from ICs - This is the clean data that will be fed into the classifier
def reconstruct_eeg_data_ICA(raw_dict , ica_dict, includeOther = True):
    brain_source_data = {};
    include = []
    for key,rawArray in raw_dict.items():
        include = ica_dict[key].labels_['brain'];
        if(includeOther):
            include.extend(ica_dict[key].labels_['other']);
        brain_source_data[key] = ica_dict[key].apply(raw_dict[key], include = include);
    
    return brain_source_data;
```

<p align="justify">
The variables 'raw_dict' and 'ica_dict' are dictionary data structures whose keys are of the form 'sub#_fHz_Trial#' and contain raw processed data (raw, band pass filtered or ASR) for a specific subject,frequency for all trials and and their respective ICs. This data structure design allowed for the creation of functions like the one shown above and many others in the API. Their simplicity in conjunction with the power MNE python library made this project possible.
</p>
<p align="justify">
Note 1: The preprocessing API can be found here: <a href ="https://github.com/vlopez0392/BCI_An_SSVEP_based_2D_Unity_Video_Game/blob/main/Code/ssvep_preprocessing_API.py">SSVEP_preprocessing_API</a>

Note 2: A demo video is provided in section 1.2 Demo Video to showcase the API's performance and quality.
</p>
<h2>5.2 Quantitative and qualitative validation methods</h2>
<p align="justify">Quantitative and qualitative methods were also explored to validate the effectiveness and reliability of our BCI system. We made many qualitatve judgements based on both EEG time-series and PSD spectrum plots based on the literature and the dataset itself. For instance, based on experiment number 3 conducted in [3] by the authors of the dataset, subject 1 was prone to have excellent SSVEP responses at a frequency of 8 Hz. This was verified and validated by our experiments and thus we make use of this subject's PSD plot in this report.</p>

<p align="justify">In addition, we make a quantitative analysis of the average number and type artifacts found by the MNE ICAlabel package in section 7 Results. We conclude that as the original dataset goes through each of the stages of the data preprocessing pipeline, the number of brain sources tends to increase as well as observing a better distribution of the type and average number of other artifacts.
</p>

<p align="justify">
Finally, we make use of Machine Learning techniques such as support vector machines (SVMs) and random forests (RF) to implement a simple SSVEP classifier whose output would serve as an input to the video game we developed. Evaluation metrics such as accuracy, precision and recall and figures such as confusion matrices are shown in section 7 results. These results help to futher validate the effectiveness and realibility of out BCI system.
</p>

---

<h2 align="center">6. Usage</h2>
  <h3>6.1 Code</h3>
  <p align="justify">All the code we developed during this project can be found in this repository in the Code directory located in the main directory. The following link will take you there: <a href="https://github.com/vlopez0392/BCI_An_SSVEP_based_2D_Unity_Video_Game/tree/main/Code">Code</a></p>

  <h3>6.2 Usage example</h3>
  <h3>6.2.1 Download the code and datasets</h3>
  <p align="justify">In a directory of your choice run the following command from your terminal:
  </p>

  ```
  $ git clone https://github.com/vlopez0392/BCI_An_SSVEP_based_2D_Unity_Video_Game
  ``` 

  <p align="justify">You can also download a zip file of the code by pressing the green <>Code button as shown  in the figure below:</p>
  <p align="center">
      <img src="/Figures/usage/code_download_usage.png">
  </p>
  <p align="justify">The following datasets are <strong>required</strong> to execute the code demo:<a href = "https://drive.google.com/drive/folders/1RRNWbd4Qa-aQntIK8nYdbixSbBvO-wfO"> Download required datasets here</a>.</p>
  <ol>  
     <li align="justify"><strong>RAW:</strong>  Contains the brain source raw data in .fif format</li>
    <li align="justify"><strong>FILT:</strong>  Contains the brain source bandpass (1-50 Hz) filtered data in .fif format</li>
    <li align="justify"><strong>ASR:</strong>  Contains the brain source bandpass (1-50 Hz) filtered and artifact subspace reconstructed (ASR) data in .fif format</li>
  </ol>
  <p align="justify">The following datasets [2] are <strong>optional</strong> and are for developing purposes only. No code demo will be provided for data preprocessing because this process is very computationally expensive.Hardware acceleration with an NVIDIA A100 GPU in a Google Colab (Pro) environment was performed to carry out data preprocessing. Total processing time was around 1.5 hours. We do not recommend performing data preprocessing locally. <a href = "https://drive.google.com/drive/folders/1tIW4ZFdN1LiKlRQBDkMeIuwmwb30VmV_?usp=sharing"> Download optional datasets here</a>.</p>
  <ol>  
    <li align="justify"><strong>SSVEP_8Hz</strong>:   Contains the raw data for 8Hz frequency in .MAT format</li>
    <li align="justify"><strong> SSVEP_14Hz</strong>: Contains the raw data for 14Hz frequency in .MAT format</li>
    <li align="justify"><strong> SSVEP_28Hz</strong>: Contains the raw data for 28Hz frequency in .MAT format</li>
  </ol> 
  
<h3>6.2.2 Required directory structure </h3>  
 <p align="justify">Once the repository has been cloned and the datasets have been downloaded to the directory of your choice, some housekeeping must be done in your directory to ensure correct code execution. The following figure shows the required directory structure (both GUI and terminal) to execute the code demo</p>
<p align="center">
      <img src="/Figures/usage/directory.png">
</p>
<p align="justify">
3 python files for preprocessing, model and code demo are required along with the required datasets described in the previous subsections. The shown pycache directory is not required. 
</p>
<h3>6.2.3 Required dependencies </h3>  
<p align="justify">
The following are the required dependencies of this project. Please install them to execute the code demo. If this proves too time consuming, please check the demo video to see the code demo examples provided in the next section.
</p>
  <ul>  
    <li align="justify">python = 3.11.1</li> 
    <li align="justify">scipy = 1.10.1</li>
    <li align="justify">mne   = 1.4.0</li>
    <li align="justify">numpy=  1.23.5 (Version < 1.24.0 required for asr)</li>
    <li align="justify">matplotlib = 3.7.1</li>
    <li align="justify">sklearn = 1.2.2</li>
    <li align="justify">mne_icalabel = 0.4</li>
    <li align="justify">torch = 2.0.1</li>
    <li align="justify">asrpy [8]</li> 
  </ul>  
<h3>6.2.4 Code demo </h3> 
<p align="justify">
Once again, make sure you have followed the steps in the sub-sections 6.2.1 and 6.2.2 and go into the directory where the code and required datasets are stored. In addition, make sure you have installed the required dependencies
described in the previous subsection. 

</p>
<h4>6.2.4.1 Plotting PSD and EEG time series plots from the terminal </h4> 
<p align="justify">
The usage is as follows:
</p>

```
$ python code_demo.py [-plot], [-time,-psd],[subject],[frequency],[-raw,-filt,-asr],[num_trials('-time')] 
```

<p align="justify">
Note: You can see this process in the project demo video too.
</p>

<p align="justify">
<strong>Example 1</strong>: Plot a time series eeg signal for all channels of the raw brain source dataset for subject 1 and a frequency of 8Hz. Plot a single trial. 

Then, to plot the EEG time series of Example 1 we input:
</p>

```
$ python code_demo.py -plot -time 1 8 -raw 1
```

<p align="justify">
The following EEG time series plot is output:
</p>
<p align="center">
      <img src="/Figures/usage/example1.png">
</p>
<p align="justify">
<strong>Example 2</strong>: Plot the power spectrum density (PSD) for all channels of the ASR brain source dataset for subject 1 and a frequency of 14Hz:

Then, to plot the PSD plot of Example 2 we input:
</p>

```
$ python code_demo.py -plot -psd 1 14 -asr
```

<p align="justify">
PSD plots for all trials will be output. The following figure shows the PSD plot of the selected ASR data for trial 1:
</p>
<p align="center">
      <img src="/Figures/usage/example2.png">
</p>
<h4>6.2.4.3 Plotting extracted features and classifier output figures </h4> 
<p align="justify">
The usage is as follows:
</p>

```
$ python code_demo.py [-model], [-raw, -asr],[-features,-confusion] 
```
<p align="justify">
<strong>Example 3</strong>: Plot the extracted features from the ASR dataset of subject 1 at a frequency of 8 Hz (Default for demo):

Then, to plot features we input:
</p>

```
$ python code_demo.py -model -asr -features
```

<p align="justify">
<strong>Example 4</strong>: Run the SVM classifier on the features extracted from Example 3 and plot the resulting confusion matrix.

Then, to plot the confusion matrix we input:
</p>

```
$ python code_demo.py -model -asr -features
```

<p align="justify">
Note: These examples are shown in the demo video. Executing the code_demo.py file with the parameters above allow us to plot some extracted features from either the brain-source raw or asr datasets. Confusion matrices and features plots are output in GUI form while the corresponding evaluation metrics are output to the terminal. 
</p>

<h4>6.2.4.4 Google Colab notebook - Data preprocessing (visualization only) </h4> 
<p align="justify">
You can explore the data preprocessing process in the Google Colab notebook here: <a href ="https://drive.google.com/drive/folders/1SQRlH2BddoyUDPOVLezxzRE0DcMiUyG1">Notebook</a>

Note: DO NOT try to execute any of the cells unless you have original dataset in the Colab File explorer. Otherwise, the original cell's output will be deleted.
</p>

---

<h2 align="center">7. Results</h2>
<h3>7.1 Preprocessing results</h3>
<h3>7.1.1 MNE-ICA and MNE-ICA label results</h3>
    <p align="justify">The following tables showcase our results after applying ICA to our EEG data and using MNE-ICA label to 
    each component as non-brain artifactual or Brain ICs for raw, band-pass filtered, and EEG data using corrected
    using ASR. We provide averages per SSVEP frequency across all subjects and trials for each of the cases discussed previously:</p>
    <p align="justify"> Number of ICs: 35 components</p>
    <h3 align = "center"><ins>SSVEP 8 Hz frequency - 4 subjects with 5 trials each </ins></h3>
    <p align="center">
      <img src="/Figures/ICA_label_averages/8Hz_ICA_label_averages.png">
    </p>
    <h3 align = "center"><ins>SSVEP 14 Hz frequency - 4 subjects with 5 trials each</ins></h3>
    <p align="center">
      <img src="/Figures/ICA_label_averages/14Hz_ICA_label_averages.png">
    </p>
    <h3 align = "center"><ins>SSVEP 28 Hz frequency - 4 subjects with 5 trials each</ins></h3>
    <p align="center">
      <img src="/Figures/ICA_label_averages/28Hz_ICA_label_averages.png">
    </p>
    <p align="justify">
    <strong>Discussion of results</strong>:
    As expected, due to noisy nature of raw eeg data, even when executing ICA with 35 components, most of them where classified as other. On the other hand, after applying a simple band pass filter we observe a great improvement in the distribution quality of identified artifacts and brain sources. This pattern of improvement is also observed after applying artifact subspace reconstruction (ASR) to our data. This verifies the claim about the reliability, quality and credibility of our data sources as expressed in sub-section 3.2.
    </p>
<h3>7.1.2 Visualization of raw, filtered and ASR data power spectrum density (PSD) plots</h3>
<p align="justify"> 
The following plots show the influence of filtering the raw data through various means, either by a passband filter or by ASR. Notice that the PSD plots correspond to the data before performing ICA. In them, we can observe the increase in power density at the target frequencies and their harmonics as we move through the stages of the data preprocessing pipeline. Below, we show the PSD plots for subject 1, trial 1 at a SSVEP frequency of 8Hz:
</p>
<h3 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - Raw PSD</ins></h3>
<p align="center">
  <img src="/Figures/psd_plots/raw.png">
</p>
<h3 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - Band pass filtered PSD</ins></h3>
<p align="center">
  <img src="/Figures/psd_plots/filter.png">
</p>
<h3 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - ASR PSD</ins></h3>
<p align="center">
  <img src="/Figures/psd_plots/asr.png">
</p>
<h3>7.2 Performance and evaluation metrics results</h3>
<h3>7.2.1 Visualization of IC brain-source PSD extracted features from dataset</h3>
<p align="justify">
In the figures below, we have extracted PSD features from 8-channels in the occipital region of the brain as described in the model framework section. The figures show the brain-source processed data up to the ASR preprocessing stage, that is, the cleanest data in our dataset. 
</p>
<p align="justify">
In the left figure, we have the features corresponding to subject 1 (all trials) and in the figure to the right we have the features corresponding to subject 2 (all trials), both figures at a target SSVEP frequency of 8Hz. In some of them, we can observe the characteristic sharp increase in power peaks at the target frequency and their harmonics.
</p>
<h3 align = "center"><ins>Subject 1, 2 (All trials 8Hz) PSD features </ins></h3> 
<p align="center">
  <img src="/Figures/features/features.png">
</p>
<h3>7.2.2 Evaluation metrics</h3>
<p align="justify"> 
The figures show below correspond to the SVM-classifier results when trained with brain-source raw and asr cleaned data. 8 channels of interest were selected as feature extraction targets in order to construct the training, testing and label datasets. 
</p>

<p align="justify"> 
Each of the samples had 313 data points corresponding to the power spectrum density computed between frequencies of 1 and 40 Hz. This method to extract data features is based on [10].The number of samples correspond to product of the number of subjects = 4, number of trials = 5 and number of target channels = 8. Thus, per SSVEP frequency, there were a total of 160 samples for which our extracted dataset consisted of 480 samples with 313 features each.
</p>

<p align="justify"> 
Classification is performed using the sklearn.svm SVC python library found in [11] which is based in the original NTU-based implementation by Chih-Chung Chang and Chih-Jen Lin [12].
</p>

<h3 align = "center"><ins> Raw brain-source extracted EEG signals classification results </ins></h3>
<p align="center">
  <img src="/Figures/metrics/raw.png">
</p>
<h3 align = "center"><ins> ASR corrected brain-source extracted EEG signals classification results </ins></h3>
<p align="center">
  <img src="/Figures/metrics/ASR_results.png">
</p>
<p align="justify">
<strong>Discussion of results</strong>:
As expected, we observe an increase in the classification accuracy (3%) for the brain-source ASR dataset when compared with the brain-source RAW dataset which validates the the data preprocessing step of our project. After ICA labeling, the brain-source ICs for the raw dataset are mostly none, for which the brain-source RAW dataset is reconstructed from the other categories. On the other hand, the brain-source ICs for the ASR dataset are significantly higher. Thus, we conclude that the ASR dataset to better represent the the brain-source signals from the subjects in the experiment. An increase of 3% in accuracy is not negligible for BCI intended applications. 
</p>
<h3>7.3 Developed Video game screenshots, Integration discussion and Future Work</h3>
<p align="justify">
The following figure is frame of the video game we developed in Unity: 
</p>
<p align="center">
  <img src="/Figures/game/game_maze.png">
</p>
<p align="justify">
Each of the flickering lights flicker at the SSVEP frequencies in our project. The user can then control the ball by fixing their sight in the desired direction flicker. The light on top of the screen allows for up and down movements since the user will be provided a button for the program to reverse the direction whenever the button is pressed. This design is due to the fact that we only have three SSVEP frequencies. 
</p>

<p align="justify">
<strong>Integration and Future Work</strong>: Classifier-Game integration was not performed in this project since concepts beyond the scope of the project were required to succesfully implement a simulated BCI video game. For instance, Reinforcement Learning techniques would be required for the program to correctly select the most probable light the user would fix their sight in. Then, a simulated EEG signal corresponding to the target frequency would need to be simulated with signal processing techniques. Thus, researchers interested in these topics may continue our work in the future. 
</p>

<p align="justify">
The game code is found here: <a href ="https://drive.google.com/drive/folders/17-8GTmWANoxvA8LXoMzcVqJH5AR8Rz5F?usp=drive_link">Game code</a>
</p>

---

<h2 align = "center">8. References</h2>
  <p>
  [1] http://www.biosemi.com/headcap.htm 
  </p>
  <p>
  [2] http://www.bakardjian.com/work/ssvep_data_Bakardjian.html
  </p>
  <p>
  [3] Bakardjian H, Tanaka T, Cichocki A, Optimization of SSVEP brain responses with application to eight-command Brain–Computer Interface, Neurosci Lett, 2010, 469(1):34-38. (http://dx.doi.org/10.1016/j.neulet.2009.11.039)
  </p>  
  <p>
  [4] https://www.wma.net/policies-post/wma-declaration-of-helsinki-ethical-principles-for-medical-research-involving-human-subjects/
  </p>
  <p>
  [5] Bakardjian, H., Martinez, P., Cichocki, A., Robust Multi-Command SSVEP-Based Brain-Machine Interface Without Training using Small Moving or Stationary Patterns, Japanese Patent #22385, 2008
  </p>
  <p>
  [6] https://mne.tools/stable/generated/mne.preprocessing.ICA.html
  </p>
  <p>
  [7] https://mne.tools/mne-icalabel/stable/index.html
  </p>
  <p>
  [8] https://github.com/DiGyt/asrpy
  </p>
  <p>
  [9] https://mne.tools/stable/index.html
  </p>
  <p>
  [10] E. Kalunga, K. Djouani, Y. Hamam, S. Chevallier and E. Monacelli, "SSVEP enhancement based on Canonical Correlation Analysis to improve BCI performances," 2013 Africon, Pointe aux Piments, Mauritius, 2013, pp. 1-5, doi: 10.1109/AFRCON.2013.6757776.
  </p>
  <p>
  [11] https://www.csie.ntu.edu.tw/~cjlin/libsvm/
  </p>
  <p>
  [12] https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
  </p>
  <p>
  [13] Demir, Ali Fatih & Arslan, Huseyin & Uysal, Ismail. (2019). Bio-Inspired Filter Banks for Frequency Recognition of SSVEP-Based Brain–Computer Interfaces. IEEE Access. 7. 160295-160303. 10.1109/ACCESS.2019.2951327. 
  </p>
  <p>
  [14] https://www.ers-education.org/lrmedia/2016/pdf/298830.pdf
  </p>
<ol>