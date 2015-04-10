# Music-Genre-Analyzer
This is my very first Machine Learning project.

## Main idea
Given a set of music files, we take only the middle part in each one of them (a 20s long piece by default), and transform it into a .wav file. Then we open this file as a [numpy](http://www.numpy.org/) array, divide it into equal parts (20 parts by default), and sum the values inside of them. Thus, we get an array of a certain length (number_of_seconds * number_of_parts) that can be stored for further analysis.

## List of files
* [downloader.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/downloader.py) – downloads all tracks from your subscriptions on [soundcloud.com](https://soundcloud.com) and saves them in the current working directory sorted by genres
* [converter.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/converter.py) – creates initial training set from the music files in the given directory and saves it as a MATLAB file
* [SVM.py](https://github.com/pyany/Music-Genre-Analyzer/blob/master/SVM.py) – trains a Support Vector Machine classifier using the generated training set

