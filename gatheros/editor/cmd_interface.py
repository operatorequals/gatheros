import cmd
import json

from empty_creator import createEmptyCommandGroup, createEmptyStruct, createEmptyCommand
from populator import populateDict

class EditorShell ( cmd.Cmd ) :


	def __init__ ( self, file ) :
		cmd.Cmd.__init__(self)
		self.file = file
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


	def do_list( self, line ) :
		for group in self.struct['CommandGroups'].keys() :
			print group


	def do_show_command( self, line ) :

		pass

	def do_edit_command( self, line ) :
		if not line :
			print "Need a 'command identifier' "
			return
		line = line.strip()
		toks = line.split()
		ident = toks[0]
		for group in self.struct['CommandGroups'].values() :
			try :
				comm = group[ ident ]
				break
			except :
				pass

		print comm

	def do_save( self, line ) :
		json.dump( self.struct, self.file, indent = 1 )
		self.file.flush()





	def do_d_list( self, line ) :
		for group in self.struct.keys() :
			print group


	def do_d_show( self, line ) :
		print json.dumps( self.struct, indent = 1 )

