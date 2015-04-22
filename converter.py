# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:25:43 2015

@author: timasemenov
"""

import scipy.io as sio
import numpy as np
import pydub
from scipy.io import wavfile
from os import listdir, path, remove

# ffmpeg binary
pydub.AudioSegment.converter = '/usr/local/Cellar/ffmpeg/2.6.1/bin/ffmpeg'

genres = ['Rap', 'Rock']        # List of different genres
music = '/Users/timasemenov/ML' # path to the music folder
size = 0                        # number of training examples stored
X = []                          # training set
y = []                          # label set
    
def sample(mp3, time, rate, index):
    global X, y    
    
    duration = len(mp3)
    parts = duration / 1000 / time
    temp = path.join('/Users/timasemenov', 'temp.wav')    
    mp3.export(temp, format='wav')      # convert an mp3 file to wav format    
    fs, data = wavfile.read(temp)       # read the .wav file as numpy array
    remove(temp)                        # delete the temporary .wav file
    for array in np.split(data[:parts*time*44100], parts):
        x = np.reshape(np.cumsum(np.split(np.array(array), rate), 1)[:,-1], 2*rate)
        X.append(x)
        y.append(index)
        
        
def save(X, y):
    sio.savemat('data.mat', {'X':np.array(X), 'y':np.array(y)})


# time = duration in seconds of the audio samples we analyze
# rate = audio sampling rate in hertz
def main(time, rate):
    global size, genres, music, X, y

    for genre in genres:
        path_to_genre = path.join(music, genre)
        for song in listdir(path_to_genre):
            path_to_song = path.join(path_to_genre, song)
            try:
                music_mp3 = pydub.AudioSegment.from_mp3(path_to_song) 
                # add current .mp3 file to the training set
                sample(music_mp3, time, rate, genres.index(genre))
                print(song)
            except pydub.exceptions.CouldntDecodeError:
                print "Couldn't decode " + song
    save(X, y) 
  
      
main(20, 20)