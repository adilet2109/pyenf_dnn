# pyenf_dnn
Python tools to train CNN on ENF Spectrograms from Audio Sources

# Environments
## enfenv
- python environment for pyenf tools
- Python Version = 3.6.13
- Environments used are mentioned in environment-enfenv.yml

## enfdnn
- python environment for training CNN models with fastai library 
- Python Version = 3.11.5
- Environments used are mentioned in environment-enfdnn.yml

# Usage
## pyENF_spectrogram_gen.py
- the script to generate spectrograms from audio files
- environment: enfenv
- input: *input_dir* variable that stores the name of directory with WAV files
- output: *output_dir* variable that stores the name of directory where spectrograms in PNG format will be stored
- edit input/output variables and run the script from command line
```
python pyENF_spectrogram_gen.py
```

## spectogram_formating.ipynb
- notebook to interactively inspect spectrograms from audio files
- environment: enfenv

## pyENF_forged_data_gen.py
- a script to cut WAV file to create a forged data  

## video_gen
- directory that contains script to generate a video of consequent set of spectrogram samples

## models-training
- directory with training code for Noise and Forging detectors

## audio-power-correlation/code
- a script to inspect presence of ENF in audio recording by cross correlation with power recording
