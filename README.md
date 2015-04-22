# Music-Genre-Analyzer
This is my very first Machine Learning project.

## Main idea
Given a set of music files, we divide each one of them into equal parts (a 20s long piece by default), and transform these pieces into .wav files. Then we open these files as [numpy](http://www.numpy.org/) arrays, divide them into equal parts (20 parts by default), and sum the frequencies and amplitudes inside of them. Thus, we get an array of a certain length (2 * number_of_parts) that can be stored for further analysis.

## List of files
* [downloader.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/downloader.py) – downloads all tracks from your subscriptions on [soundcloud.com](https://soundcloud.com) and saves them in the current working directory sorted by genres
* [converter.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/converter.py) – creates initial training set from the music files in the given directory and saves it as a MATLAB file
* [model.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/model.py) – trains a classifier using Quadratic Discriminant Analysis and finds the best regularization parameter
* [data.mat](https://github.com/pyany/Music-Genre-Analyzer/blob/master/data.mat) – the training set
