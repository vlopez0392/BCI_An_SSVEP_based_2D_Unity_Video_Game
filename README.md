# BCI_An_SSVEP_based_2D_Unity_Video_Game
<h1>Final Project: Spring 2023 Brain Computer Interfaces: Fundamentals and Applications, NTHU, Taiwan</h2>

<h3>1. Project members:</h3>
<ul>
  <li>巫冠緯           - 111062640</li>
  <li>Wu, Shao-Hung	  -	111065543</li>
  <li>Victor D. Lopez - 110062426</li>
</ul>

<h3>2. Introduction</h3>

<h3>3. Data description</h3>

<p>As required, we first describe the experimental design/paradigm, procedure for collecting data, hardware and software used, data size, number of channels, sampling rate, the website from which our data was collected, owner, source, etc.</p>

<ul>
  <li>
    <ins>Number of channels:</ins> 128-channels BIOSEMI (Active electrodes) where the cap layout is found in reference [1]. The electrode placement layout is shown below: 
    <br/>
    <br/>
    <br/>
    <p align="center">
      <img src="/Figures/Sensor_positions/sensor_locations.png" width="600" height="400">
    </p>
  </li>
  <br/>
  <li>
    	<ins>Data size:</ins> 
      <ul>
        <li>Number of subjects: 4</li>
        <li>Number of trials per subject: 5 </li>
        <li>Number of SSVEP stimulation frequencies available: 8 Hz, 14 Hz, 28 Hz</li>
      </ul>
  </li>
  <br/>
  <li><ins>Website where the data was collected:</ins> The data was collected from the website provided in reference [2]. </li>
   <br/>
  <li><ins>Dataset owner:</ins>  Copyright holders of the database are Dr. Hovagim Bakardjian and RIKEN-LABSP [2].</li>
  <br/>
  <li><ins>Description of the experimental design, paradigms, and procedure to collect the data:</ins>
    <p>
      The description of the experimental design is readily provided in reference [3]. In summary, four healthy subjects with corrected       vision or no vision problems and no neurological disorders and no previous training were subjected to SSVEP stimulations at             different frequencies. EEG data was acquired with a 128 active electrode cap found in reference [2]. All the subjects consented         agreement to the experiments under the Declaration of Helsinki [4]. 
    </p>
  </li>
  <li>
    <ins>Hardware and Software used: </ins>
    <p>
    The description of the software/hardware used is also readily available in reference [3]. In summary, a 21 in CRT computer monitor (168 ± 0.4 Hz) was placed 90 centimeters from each subject. To achieve SSVEP stimulation, a 6 x 6 checkerboard pattern with flashing black and white reversing squares was used. 
    </p>
  </li>
</ul>
<br/>
<h3>4. Model Framework</h3>
<br/>
<h3>5. Validation</h3>
<br/>
<h3>6. Results</h3>
<br/>
<h4>6.1 Preprocessing results</h4>
<h4>6.1.1 MNE-ICA and MNE-ICA labelresults</h4>
<br/>
    <p>The following tables showcase our results after applying ICA to our EEG data and using MNE-ICA label to 
    each component as non-brain artifactual or Brain ICs for raw, band-pass filtered, and EEG data using corrected
    using ASR. We provide averages per SSVEP frequency across all subjects and trials for each of the cases discussed previously:</p>
    <br/>
    <ins>8 Hz</ins>
    <p align="center">
      <img src="/Figures/ICA_label_averages/8Hz_ICA_label_averages.png">
    </p>
    <br/>
    <ins>14 Hz</ins>
    <br/>
    <ins>28 Hz</ins>
<br/>
<h4>6.1.2 Comparison of raw, filtered and ASR data power spectrum plots<h2>
<br/>
<br/>
<h3>References</h3>
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
<ol>