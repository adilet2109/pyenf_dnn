import pdb
from os import listdir
from os.path import isfile, join, splitext
import numpy as np
import cv2
import pickle
import pyenf
import scipy.io.wavfile
from scipy import signal
import math
from scipy.fftpack import fftshift
import matplotlib.pyplot as plt
import librosa
from skimage.util import img_as_float
from skimage.segmentation import slic
from scipy.stats.stats import pearsonr
import re

fs = 1000  # downsampling frequency (increase amount of samples)
nfft = 8192 # decides resolution of spectograms 
frame_size = 2  # change it to 6 for videos with large length recording
overlap = 0
window_size = 5
shift_size = window_size/100
input_dir = "/home/adilet/pyenf_dnn/newamp/input"
output_dir = "/home/adilet/pyenf_dnn/newamp/output"
input_files_list = []
#pattern = r"_\d+min"
pattern = r"_\d+scns"

for file in listdir(input_dir):
    if file.endswith(".wav"):
        input_files_list.append(file)

for file in input_files_list:
    power_signal_recording, fs = librosa.load(join(input_dir, file), sr=fs)  # loading the power ENF data
    file_length = power_signal_recording.size
    total_windows = math.ceil(((file_length/fs)-window_size+1)/shift_size)
    for i in range(0,total_windows):
        spectrum_check = "_0_"
        window_start = int(i*shift_size*fs)
        window_end = int(window_start+(window_size*fs))
        sampled_data = power_signal_recording[window_start:window_end]
        f, t, P = signal.spectrogram(sampled_data, nfft=nfft, fs=fs, mode = 'magnitude')
        plt.figure(figsize=(8,8))
        plt.pcolormesh(t, f, 10*np.log(P), shading='gouraud', cmap = 'gray')#'seismic')
        plt.ylim(298,302)
        #plt.ylim(118,122)
        #plt.ylim(59.5,60.5)
        plt.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = False, bottom = False)
        if file[0].isupper():
            matches = re.findall(pattern,file)
            #seconds_cut = [int(''.join(filter(str.isdigit, i)))*fs*60 for i in matches]
            seconds_cut = [int(''.join(filter(str.isdigit, i)))*fs for i in matches]
            for cut in seconds_cut:
                if cut > (window_start + 2*(shift_size*fs)) and cut < (window_end-2*(shift_size*fs)):
                #if cut >= window_start and cut <= window_end:
                    spectrum_check = "_1_"
            matches = None
            seconds_cut = None
        output_name = splitext(file.lower())[0]
        output_name = re.sub(pattern, '', output_name)
        file_name = output_dir + "/" + output_name + spectrum_check  + "recording_" + str(i) + ".png"
       # plt.ylabel('Frequency [Hz]')
        plt.savefig(file_name)
        plt.cla()
        plt.clf
        plt.close()
