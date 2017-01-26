#!/usr/bin/env python
from gatheros import __name__ as module_name
from editor.cmd_interface import EditorShell

import argparse
import sys, os, os.path
import json
import cmd

parser = argparse.ArgumentParser( description = "A tool to read/write 'gatheros' command execution files")
parser.add_argument( "file", help = "The gatheros command execution file to open" )
write_argument = '--write'
parser.add_argument( write_argument, '-w', help = "Open the file in 'write mode'",\
					action = 'store_true', default = False )

def main( arguments = sys.argv[1:] ) :

	args = parser.parse_args( arguments )

	if not os.path.isfile(args.file) and not args.write :
		print "Can't create a file without '%s' argument" % write_argument
		sys.exit(-1)


	jsonFile = open( args.file, 'r+w' )

	commandStruct = None
	# commandStruct = json.load( jsonFile )

	# print str(commandStruct)[:100]

	print jsonFile


	shell = EditorShell ( jsonFile )
	shell.cmdloop()


if __name__ == '__main__' :

	main()
