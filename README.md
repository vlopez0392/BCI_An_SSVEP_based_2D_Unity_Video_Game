# BCI_An_SSVEP_based_2D_Unity_Video_Game
<h1>Final Project: Spring 2023 Brain Computer Interfaces: Fundamentals and Applications, NTHU, Taiwan</h2>

<h3 align="center">1. Project members</h3>
<ul>
  <li>巫冠緯           - 111065543  </li>
  <li>Wu, Shao-Hung	  -	111062640  </li>
  <li>Victor D. Lopez - 110062426  </li>
</ul>

---

<h3 align="center">2. Introduction</h3>

---

<h3 align="center">3. Data description</h3>
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

<h3 align="center">4. Model Framework</h3>

---

<h3 align="center">5. Validation</h3>

---

<h3 align="center">6. Usage</h3>
  <h3>6.1 Code</h3>
  <p align="justify">All the code we developed during this project can be found in this repository in the Code directory located in the main directory. The following link will take you there: <a href="https://github.com/vlopez0392/BCI_An_SSVEP_based_2D_Unity_Video_Game/tree/main/Code">Code</a></p>

  <h3>6.2 Usage example</h3>
  <h3>6.2.1 Download the code and datasets</h3>
  <p align="justify">In a directory of your choice run the following command from your terminal:
  </p>
  <p align="justify">
    <code align="justify">$ git clone https://github.com/vlopez0392/BCI_An_SSVEP_based_2D_Unity_Video_Game</code>
  </p>
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
    <li align="justify">asr [8]</li> 
  </ul>  
<h3>6.2.4 Code demo </h3> 
<p align="justify">
Once again, make sure you have followed the steps in the sub-sections 6.2.1 and 6.2.2 and go into the directory where the code and required datasets are stored. In addition, make sure you have installed the required dependencies
described in the previous subsection. 

</p>
<h4>6.2.4.1 Plotting PSD and EEG time series plots from the terminal </h4> 
<p align="justify">
The usage is as follows:

<code align="justify">$ python code_demo.py [-plot,-model], [-time,-psd],[subject],[frequency],[-raw,-filt,-asr],[num_trials -> 'time ONLY'] </code>

Note: You can see this process in the project demo video too.
</p>

<p align="justify">
<strong>Example 1</strong>: Plot a time series eeg signal for all channels of the raw brain source dataset for subject 1 and a frequency of 8Hz. Plot a single trial. 

Then, to plot the EEG time series of Example 1 we input:

<code align="justify">$ python code_demo.py -plot -time 1 8 -raw 1</code>

The following EEG time series plot is output:
</p>
<p align="center">
      <img src="/Figures/usage/example1.png">
</p>
<p align="justify">
<strong>Example 2</strong>: Plot the power spectrum density (PSD) for all channels of the ASR brain source dataset for subject 1 and a frequency of 14Hz:

Then, to plot the PSD plot of Example 2 we input:

<code align="justify">$ python code_demo.py -plot -psd 1 14 -asr</code>

PSD plots for all trials will be output. The following figure shows the PSD plot of the selected ASR data for trial 1:
</p>
<p align="center">
      <img src="/Figures/usage/example2.png">
</p>

<h4>6.2.4.3 Google Colab notebook - Data preprocessing (visualization only) </h4> 
<p align="justify">
You can explore the data preprocessing process in the Google Colab notebook here: <a href ="https://drive.google.com/drive/folders/1SQRlH2BddoyUDPOVLezxzRE0DcMiUyG1">Notebook</a>

Note: DO NOT try to execute any of the cells unless you have original dataset in the Colab File explorer. Otherwise, the original cell's output will be deleted.
</p>

---

<h3 align="center">7. Results</h3>
<h3>7.1 Preprocessing results</h3>
<h3>7.1.1 MNE-ICA and MNE-ICA label results</h3>
    <p align="justify">The following tables showcase our results after applying ICA to our EEG data and using MNE-ICA label to 
    each component as non-brain artifactual or Brain ICs for raw, band-pass filtered, and EEG data using corrected
    using ASR. We provide averages per SSVEP frequency across all subjects and trials for each of the cases discussed previously:</p>
    <p align="justify"> Number of ICs: 35 components</p>
    <h4 align = "center"><ins>SSVEP 8 Hz frequency - 4 subjects with 5 trials each </ins></h4>
    <p align="center">
      <img src="/Figures/ICA_label_averages/8Hz_ICA_label_averages.png">
    </p>
    <h4 align = "center"><ins>SSVEP 14 Hz frequency - 4 subjects with 5 trials each</ins></h4>
    <p align="center">
      <img src="/Figures/ICA_label_averages/14Hz_ICA_label_averages.png">
    </p>
    <h4 align = "center"><ins>SSVEP 28 Hz frequency - 4 subjects with 5 trials each</ins></h4>
    <p align="center">
      <img src="/Figures/ICA_label_averages/28Hz_ICA_label_averages.png">
    </p>
    <p align="justify">
    <strong>Discussion of results</strong>:
    As expected, due to noisy nature of raw eeg data, even when executing ICA with 35 components, most of them where classified as other. On the other hand, after applying a simple band pass filter we observe a great improvement in the distribution quality of identified artifacts and brain sources. This pattern of improvement is also observed after applying artifact subspace reconstruction (ASR) to our data. This verifies the claim about the reliability, quality and credibility of our data sources as expressed in sub-section 3.2.
    </p>
<br/>
<h3>7.1.2 Visualization of raw, filtered and ASR data power spectrum density (PSD) plots</h3>
<p align="justify"> 
The following plots show the influence of filtering the raw data through various means, either by a passband filter or by ASR. Notice that thes PSD plots correspond to the data before performing ICA. In them, we can observe the increase in power density as we move through the stages of the data preprocessing pipeline. Below, we show the PSD plots for subject 1, trial 1 at a SSVEP frequency of 8Hz:
</p>
<h4 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - Raw PSD</ins></h4>
<p align="center">
  <img src="/Figures/psd_plots/raw.png">
</p>
<h4 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - Band pass filtered PSD</ins></h4>
<p align="center">
  <img src="/Figures/psd_plots/filter.png">
</p>
<h4 align = "center"><ins>SSVEP 8 Hz frequency - Subject 1, Trial 1 - ASR PSD</ins></h4>
<p align="center">
  <img src="/Figures/psd_plots/asr.png">
</p>
<h3>7.2 Performance and evaluation metrics results</h3>
<h3>7.2.1 Visualization of IC brain-source PSD extracted features from dataset</h3>

<br/>
<h3>7.2.2 Evaluation metrics considered</h3>

---

<h3 align = "center">8. References</h3>
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
<ol>