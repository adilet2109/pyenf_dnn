import librosa
import numpy as np
import os
import soundfile as sf
import random

def generate_ordered_list(length, min_val, max_val):
    if length <= 0:
        return []

    if min_val > max_val:
        min_val, max_val = max_val, min_val

    return sorted(random.randint(min_val, max_val) for _ in range(length))

def remove_segments(audio_array, sr, cut_points, duration):
    # Convert cut points and duration to samples
    cut_samples = [int(cut_point * sr) for cut_point in cut_points]
    duration_samples = int(duration * sr)

    # Initialize modified audio array
    modified_audio = audio_array.copy()
    # Iterate over cut points and remove specified duration
    for cut_sample in cut_samples:
        end_sample = cut_sample + duration_samples
        modified_audio = np.concatenate((modified_audio[:cut_sample], modified_audio[end_sample:]))
    return modified_audio

def generate_output_filename(input_filename, cut_points):
    # Capitalize first letter of input filename
    base_name = input_filename.capitalize()
    # Generate part of the name with cut points
    cut_points_str = '_'.join([str(int(point)) + 'scns' for point in cut_points])
    return base_name + '_' + cut_points_str + '.wav'

# Read the audio file
file_path = "/home/adilet/pyenf_dnn/newampvol5_new/rawaudio/vol5new.wav"
output_directory = "/home/adilet/pyenf_dnn/newampvol5_new/input"
y, sr = librosa.load(file_path)

cut_points = generate_ordered_list(24, 20, 3400) #[120, 180, 200, 210, 300, 450, 600, 860] # 8
duration = 0.001  # Duration to remove in seconds

# Remove segments based on cut points and duration
y_modified = remove_segments(y, sr, cut_points, duration)

# Generate output file name
output_filename = generate_output_filename(os.path.splitext(os.path.basename(file_path))[0], cut_points)

output_file_path = output_directory + "/" + output_filename

# Save the modified audio back to a file
sf.write(output_file_path, y_modified, sr, format='WAV')

print(output_filename)
