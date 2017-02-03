import datetime
import os
import re


def createCodename( name ) :
 	codename = name.lower()
	codename = re.sub( "\s", "", codename )
	codename = re.sub( "\W", "", codename )
	return codename

def createEmptyStruct () :
	ret = {}
	ret['CommandGroups'] = {}
	ret['Commands'] = {}
	ret['OperatingSystem'] = ""
	ret['Populated'] = False
	ret['DependenyTokens'] = []
	ret['Metadata'] = {
		'author' : '',
		'description' : '',
		'creation_date' : datetime.datetime.now().strftime ( "%Y-%m-%d" ),
		'reference': ''
	}
	return ret


def createEmptyCommandGroup ( name ) :
	codename = createCodename( name )
	ret = {}
	ret['name'] = name
	ret['index'] = createEmptyCommandGroup.index
	ret['Commands'] = []
	createEmptyCommandGroup.index += 1
	return ( codename, ret )
createEmptyCommandGroup.index = 0


def createEmptyCommand ( zero_index = False ) :
	if zero_index :
		createEmptyCommand.index = 0

	unique = os.urandom(12).encode( 'hex' )
	ret = {}
	ret['command'] = ''
	ret['description'] = ''
	ret['index'] = createEmptyCommand.index
	ret['depends'] = []
	ret['unlocks'] = []
	ret['response_filter'] = ''	# the 'response' variable will contain the command response
	ret['show'] = True
	createEmptyCommand.index += 1

	return ( unique, ret )
createEmptyCommand.index = 0



def addCommand( struct, comm_group_codename, comm_id, command ) :
	struct['Commands'][comm_id] = command
	struct['CommandGroups'][comm_group_codename]['Commands'][comm_group_codename].append(comm_id)


def deleteCommand( comm_id, comm_group_codename = None ) :
	del struct['Commands'][comm_id]
	if comm_group_codename :
		struct['CommandGroups'][comm_group_codename]
	else :
		for commandgroup in struct['CommandGroups'].values() :
			try :
				commandgroup['Commands'].remove( comm_id )
			except :
				pass
