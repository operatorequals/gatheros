import datetime
import os
import re



def createEmptyStruct () :
	ret = {}
	ret['CommandGroups'] = {}
	ret['DependenyTokens'] = []
	ret['Metadata'] = {
		'author' : '',
		'description' : '',
		'creation_date' : datetime.datetime.now().strftime ( "%Y-%m-%d" )
	}
	return ret


def createEmptyCommandGroup ( name ) :
	codename = name.lower()
	codename = re.sub( "\s", "", codename )
	codename = re.sub( "\W", "", codename )
	ret = {}
	ret['name'] = name
	ret['index'] = createEmptyCommandGroup.index
	ret['Commands'] = {}
	createEmptyCommandGroup.index += 1
	return ( codename, ret )
createEmptyCommandGroup.index = 0


def createEmptyCommand ( ) :
	unique = os.urandom(8).encode( 'hex' )
	ret = {}
	ret['command'] = ''
	ret['description'] = ''
	ret['index'] = createEmptyCommand.index
	ret['depends'] = []
	ret['solves'] = []
	ret['response_filter'] = ''	# the 'response' variable will contain the command response
	ret['show'] = True
	createEmptyCommand.index += 1

	return ( unique, ret )
createEmptyCommand.index = 0
