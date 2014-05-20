'''
The hw6 module is written to have
a songdata function, and a getartists function.
See their individual docstrings for further info.
These functions were written by Braden Smith, Fall 2013.
'''

import pyen
import os, sys
os.environ["ECHO_NEST_API_KEY"] = open("Key.txt").read().strip()
en = pyen.Pyen()
def songdata(response):
	'''The songdata function is a function that, when
        called it accepts input in the form of a dictionary. It then iterates over 
		every entry in the dictionary and obtains song/artist data. It then formats
		and outputs the collected data.
    '''
	
	for info in response['songs']: #This for loop iterates over every part of the dictionary.
		response = en.get('artist/familiarity', name=info['artist_name']) 
		#The above statement accesses Echo Nest and obtains the artist's familiarity score.
		fam=response['artist']['familiarity'] #This collects the familiarity score.
		final="%0.2f" % fam #This statement formats the fam. score by truncation.
		nam=info['artist_name'].encode('utf8') #This statement insures there are no encoding errors.
		
		sys.stdout.write("\t{} {}\n".format(final,nam)) #This statement prints the formatted data for each song.
		
def getartists(**ins):
	'''The getartists function is a function that, when
        called it accepts input in the form of a parameter for a query. It then 
		queries the EchoNest database and returns the records.
    '''
	response = en.get('song/search', title=name, **ins) #This statement queries the database.
	return response #This statement returns the results. 
	
#The above functions are used in the code to follow.
	
sys.stdout.write("-Song Search-\n") #This statement outputs a title for the program.
name=raw_input("Please enter a song name: ") #This statement requests input from user then stores it.

first=getartists(results="60",sort='artist_familiarity-desc') #This statement calls the DB query function.
second=getartists(results="60", start='60',sort='artist_familiarity-desc') #this statement calls the DB query function for the 2nd 60 records.
sys.stdout.write("Familiarity  Artist Name") #This statement outputs the collumn headers.
songdata(first) #This statement calls the function to output data.
songdata(second) #This statement calls the function to output data for the 2nd 60 records.