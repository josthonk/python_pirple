# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:07:58 2021

@author: yosua
"""

"""
This file for atributes in Songs Database, 
so we can filter later for each atributes
"""
# Artist or Band Name
Artist = "Deftones"

# Band or BoyBand or Single or 
ArtistType = "Band"

# The song's album
Album = "Saturday Night Wrist"

# Track number in the album
TrackNumber = 1

#Song's Title
Title = "Hole In The Earth"

# This song's genre
Genre = "Alt Metal"

# This song's year of release
YearReleased = 2006

# This song's producer/producers
Producer = "Shaun Lopez, Bob Ezrin"

#This song's duration in second
LengthInSecond = 253

#This song / artist Label 
Labels = "Maverick"

"""
print(Artist)
print(ArtistType)
print(Album)
print(TrackNumber)
print(Title)
print(Genre)
print(YearReleased)
print(Producer)
print(LengthInSecond)
print(Labels)
"""

#Functions
def genre():
    genre = Genre
    print(genre)
def artist():
    artist = Artist
    print(artist)
def year():
    year = YearReleased
    print(year)
genre()
artist()
year()

#boolean Extra Credit
def testForBoolean():
    yrr = YearReleased
    return True
print(testForBoolean())   




    