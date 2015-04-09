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


def sample(mp3, time, rate):
    duration = len(mp3)
    snippet = mp3[(duration-time*1000)/2 : (duration+time*1000)/2]
    temp = path.join('/Users/timasemenov', 'temp.wav')
    snippet.export(temp, format='wav')      # convert an mp3 file to wav format
    fs, data = wavfile.read(temp)           # read the .wav file as numpy array
    step = 44100 / rate
    remove(temp)                            # delete the temporary .wav file
    return data[::step]

def save(X, y):
    sio.savemat('data.mat', {'X':X, 'y':y})

# time = duration in seconds of the audio samples we analyze
# rate = audio sampling rate in hertz
def main(time, rate):
    global size, genres, music
    X = []    # training set
    y = []                             # label set
    for genre in genres:
        path_to_genre = path.join(music, genre)
        for song in listdir(path_to_genre):
            path_to_song = path.join(path_to_genre, song)
            try:
                music_mp3 = pydub.AudioSegment.from_mp3(path_to_song) 
                # add current .mp3 file to the training set
                X.append(sample(music_mp3, time, rate))
                y.append(genres.index(genre))
                size += 1
                print(size)
            except pydub.exceptions.CouldntDecodeError:
                print "Couldn't decode " + song
    save(X, y) 
        
main(20, 20)