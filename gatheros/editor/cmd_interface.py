import cmd
import json
import termcolor

from struct_manager import createEmptyCommandGroup, createEmptyStruct, createEmptyCommand
from populator import populateDict

class EditorShell ( cmd.Cmd ) :


	def __init__ ( self, file ) :
		cmd.Cmd.__init__(self)
		self.file = file
		# self.struct = json.load ( self.file )
		try :
			self.struct = json.load ( self.file )
		except :
			print "[!] Can't open the JSON file, creating a new struct"
			self.struct = createEmptyStruct()

		self.cur_node = self.struct


	def do_add( self, line ) :
		if not line :
			return
		line = line.strip()
		toks = line.split()
		ident = toks[0].lower()
		if 'command' == ident :
			self.do_add_command( ' '.join( toks [1:] ) )
			pass	# add command

		elif 'group' == ident :
			self.do_add_group( ' '.join( toks [1:] ) )

			pass	# add command

		elif 'dependency' == ident :
			pass	# add command

		else :
			print " '%s' not available subcommand!" % ident


	def do_add_group( self, line ) :
		if not line :
			print "Need a 'name' "
			return
		line = line.strip()
		toks = line.split()
		codename, group = createEmptyCommandGroup( toks[0] )
		populateDict(group)
		print group
		self.struct['CommandGroups'][ codename ] = group


	def do_add_command( self, line ) :
		if not line :
			print "Need a 'group code name' "
			return
		line = line.strip()
		toks = line.split()
		codename = toks[0]
		unique, command = createEmptyCommand( )
		populateDict( command )
		self.struct['CommandGroups'][ codename ]['Commands'][ unique ] = command
		print "Command '%s' created!" % unique


	def do_add_dependency( self, line ) :
		pass




	def do_show_command( self, line ) :

		pass


	def do_edit_command( self, line ) :
		if not line :
			print "Need a 'command identifier' "
			return
		line = line.strip()
		toks = line.split()
		ident = toks[0]
		for gname, group in self.struct['CommandGroups'].iteritems() :
			try :
				comm = group['Commands'][ident]
				break
			except :
				pass

		if not comm :
			print "Identifier '%s' doesn't exist" % comm
			return
		populateDict( comm, False )


	def do_edit_group( self, line ) :
		if not line :
			print "Need a 'command identifier' "
			return
		line = line.strip()
		toks = line.split()
		gname = toks[0]
		group = self.struct['CommandGroups'][gname]
		populateDict( group )

		if not comm :
			print "Identifier '%s' doesn't exist" % comm
			return


	def do_list( self, line ) :
		for group in self.struct['CommandGroups'].keys() :
			print group

	def do_list_commands( self, line ) :
		for gname, group in self.struct['CommandGroups'].iteritems() :
			print "=========== %s ===========" % group['name']
			for k, v in group['Commands'].iteritems() :
				print '''{0:24} -| {1:<64}\n-> {2:<64}
'''.format( k, v['command'].encode('utf8'), v['description'].encode('utf8') )
			print "=========== --- ===========" 
			print 


	def do_save( self, line ) :

		self.file.seek(0)
		self.file.write( json.dumps( self.struct, indent = 1 ) + '\n' )
		self.file.truncate()


	def do_create_dependency( self, line ) :
		if not line :
			print "Need a 'name' "
			return
		line = line.strip()
		toks = line.split()
		dep = toks[0]
		self.struct['DependencyTokens'].append( dep )


	def do_d_list( self, line ) :
		for group in self.struct.keys() :
			print group


	def do_d_show( self, line ) :
		print json.dumps( self.struct, indent = 1 )

