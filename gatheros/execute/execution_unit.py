

from pprint import pprint
import sys



class ExecutionUnit :

	def __init__ ( self, execute_command, commStruct ) :
		self.execute_command = execute_command
		self.commStruct = commStruct
		self.dependencies_met = set()
		self.allCommands = set( self.commStruct['Commands'].keys() ) 
		self.allCommandsDict = self.commStruct['Commands']
		
		self.notExecuted = self.allCommands


	def executeCommandSet( self, commSet ) :

		commFailed = set()

		for comm_id in commSet :
			command = self.commStruct['Commands'][comm_id]
			self.notExecuted.remove( comm_id )

			try :
				response = self.execute_command ( command['command'] ).decode( 'utf8' )
				self.dependencies_met.update( command['unlocks'] )
			except :
				commFailed.add( comm_id )
				print "[!] Command '%s' couldn't be executed." % comm_id
				print "'%s'" % command['command']
				# command['error'] = True
				print sys.exc_info()[0]
				continue

			try :
				filter_ = command['response_filter']
				if filter_ :
					response = self.filterResponse( response, filter_ )
			except KeyError:
				pass
			except :
				print "Command '%s' filter:\n>>> %s\n Couldn't be executed.\n" % (comm_id, filter_)
			command['response'] = response


		# commSet.difference_update( commFailed )
		return commSet


	def filterResponse( self, response, filter_ ) :
		ret = str( eval ( filter_,  ) )
		return ret


	def getReadyCommands( self ) :
		ret = set()
		for comm_id in self.notExecuted :
			command = self.allCommandsDict[ comm_id ]
			commDependencies = set( command['depends'] )
			if commDependencies <= self.dependencies_met :
				ret.add( comm_id )
		return ret


	def execute( self ) :
		wDependencies = set( [ id_ for id_, command in self.allCommandsDict.iteritems()\
										if command['depends'] ] )
		woutDependencies = self.allCommands - wDependencies

		readyCommands = self.getReadyCommands()

		print "Remaining Commands: %d" % len(self.notExecuted)
		while readyCommands :
			self.executeCommandSet( readyCommands )
			print "Remaining Commands: %d" % len(self.notExecuted)
			readyCommands = self.getReadyCommands()

		self.commStruct['Populated'] = True
		return self.commStruct