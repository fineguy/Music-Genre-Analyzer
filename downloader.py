# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:32:16 2015

@author: timasemenov
"""

import os
import soundcloud
import wget


genres = ['Rap', 'Rock'] # List of different genres
files = list()           # paths to all downloaded songs
urls = list()            # list of their urls

# Create folders for music files
for genre in genres:
    try:
        os.mkdir(genre)
        print 'Folder ' + genre + ' created'
    except OSError:
        print 'Folder ' + genre + ' already exists'

# Create a new client that uses the user credentials oauth flow
me = soundcloud.Client(client_id='556b2d1b8a02102fa1f7ad8c1ef60ebb',
                           client_secret='b55ed8f5c0f81b8d8b3c637c1d4b33fb',
                           username='pyany',
                           password='5Onxqz2ADT')
                           
# Making sure that song names contain only valid characters      
allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789-_()@#$&+="
def get_title(title):
    return ''.join([c for c in title if c in allowed])
    
# Download tracks from followed users
for user in me.get('/me/followings'):
    id = user.id
    username = user.username
    print 'Collecting data from ' + username
    
    # Collect tracks from playlists
    print 'Collecting playlists ...'
    for playlist in me.get('/users/'+str(id)+'/playlists'):
        for track in playlist.tracks:
            title = get_title(track['title'])
            genre = track['genre']
            if genre != None:
                filename = genre + '/' + title + '.mp3'
                if not os.path.isfile(filename):
                    if track['streamable']:
                        try:
                            genres.index(genre)
                            url = me.get(track['stream_url'], allow_redirects=False).location
                            urls.append(url)
                            files.append(filename)  
                        except ValueError:
                            print "Oops! Could not recognize '" + title + "' genre"
                    else:
                        print "'" + title + "' cannot be downloaded"
                else:
                    print "'" + title + "' was already downloaded"
    
    # Collect user tracks
    print 'Collecting tracks ...'
    for track in me.get('users/'+str(id)+'/tracks'):
        title = get_title(track.title)
        genre = track.genre
        if genre != None:
            filename = genre + '/' + title + '.mp3'
            if not os.path.isfile(filename):
                if track.streamable:
                    try:
                        genres.index(genre)
                        url = me.get(track.stream_url, allow_redirects=False).location
                        urls.append(url)
                        files.append(filename)
                    except ValueError:
                        print "Oops! Could not recognize '" + title + "' genre"
                else:
                        print "'" + title + "' cannot be downloaded"
            else:
                print "'" + title + "' was already downloaded"


# Download tracks
for x in range(len(urls)):
    print 'Starting download ...'
    wget.download(urls[x], files[x])
    print files[x].split('/')[1] + ' successfully downloaded'
        
