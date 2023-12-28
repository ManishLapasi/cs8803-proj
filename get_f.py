import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import matplotlib.pyplot as plt


def freq(file, start_time, end_time):

    sr, data = wavfile.read(file)
    print(sr, data, len(data))
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Read portion of wav file between start and end times
    dataToRead = data[int(start_time * sr / 1000) : int(end_time * sr / 1000) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)
    return xf,yf
    

def get_most_occurring(xf, yf, num_freqs):
    xf_yf = list(zip(xf, yf))
    xf_yf.sort(key = lambda x: x[1])
    return [xf_yf[i][0] for i in range(num_freqs)]


def remove_noise_from_source(sound_file, noise_file, start_time, end_time, num_freqs):
    xf_sound, yf_sound = freq(sound_file, start_time, end_time)
    xf_noise, yf_noise = freq(noise_file, start_time, end_time)
    yf = np.abs(yf_sound-yf_noise)

    # asserting freqs are same
    assert((xf_noise == xf_sound).all())

    plt.plot(xf_sound, yf)
    plt.show()

    return get_most_occurring(xf_sound, yf, num_freqs)

sound_file = "./cs8803-mci-audio/blender_1/test_2023-11-06_18-39-11-28-1.wav"
noise_file = "./cs8803-mci-audio/nothing/test_2023-11-06_18-39-10-27-1.wav"
start_time = 0
end_time = 5000
num_freqs = 10

xf,yf = freq(noise_file, start_time, end_time)
print("most occuring frequencies in the noise file", get_most_occurring(xf, yf, num_freqs))
xf,yf = freq(sound_file, start_time, end_time)
print("most occuring frequencies in the sound file", get_most_occurring(xf, yf, num_freqs))
print(remove_noise_from_source(sound_file, noise_file, start_time, end_time, num_freqs))