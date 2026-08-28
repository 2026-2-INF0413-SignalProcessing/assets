'''
Audio Processing Library
@author: Aldo Diaz, 2021
'''

import numpy as np
import wave # para reproduzir arquivos WAV
from music21 import midi # para reproduzir arquivos MIDI
from IPython.display import Audio

def audioread(filename):
    '''
    Loads audio data on a file an returns:
     - An array 'x' of type 'numpy.float'
     - The samply frequency 'fs'
    Each sound channel will be a column of the array.
    '''
    ifile = wave.open(filename)
    fs = ifile.getframerate()
    frames = ifile.getnframes()
    x = ifile.readframes(frames)
    x = np.frombuffer(x, dtype='uint16')
    x = x.astype('int16')
    x = x.astype(float) / np.iinfo('uint16').max # 2^NUM_BITS - 1
    
    channels = ifile.getnchannels()
    if channels > 1:
        '''
        x[0]: left channel
        x[1]: right channel
        '''
        x = x.reshape((len(x) // channels, channels)).T

    return x, fs

def play(x, fs=None):
    '''
    Plays audio files (WAV, OGG)
    '''
    display(Audio(data=x, rate=fs))

def playMIDI(filename):
    '''
    Play MIDI files
    '''
    mf = midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    s = midi.translate.midiFileToStream(mf)
    s.show('midi')
