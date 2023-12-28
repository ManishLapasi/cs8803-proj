# CS8803 Project - Audio based Consumption Detection (AbCD)

This repo contains the code used for our CS8803 - MCI project.

## Prerequisites

- [ ] raspberry Pi
- [ ] microphone
- [ ] pytorch - on system or rPI
- [ ] arecord - on rPi
- [ ] `cs8803-audio-files` folder - contains subdirectories for each category, which contain the corresponding audio clips.

## Steps

- The `myscript.sh` file is used to record audio clips. By default, the audio clips are named by timestamp. It is at the discretion of the audio collector to discern different audio sources (or edit the file accordingly). 
- The `ml_preproc_multi.ipynb` notebook is used to convert the audio snippets into spectrograms, which are saved in the `data` directory. If a `data` directory is not present, it needs ot be created before running the file.
- The `model_N_multidevice_15epochs.ipynb` notebook runs the CNN model and evaluates it. By default, it is mapped to Google Drive for data storage and retrieval - this can be edited if necessary.

There are many other files which show the different approaches and results we obtained over the course of training the model on the amount of data collected over time.

The spectrograms of the audio data files used in this project can be found [here](https://drive.google.com/drive/folders/1N-W-B_M5x9cbqcsrwe5F3mg6K3EG-oBC?usp=sharing). Feel free to reach out to us if you're unable to access them!

## Contributors

- Aishwarya Solanki (903808969) - `aishwarya.solanki@gatech.edu`
- Manikandan Lapasi Parthasarathy (903839333) - `mlp7@gatech.edu`
- Nikhil Sachdeva (903819985) - `nsachdeva32@gatech.edu`
