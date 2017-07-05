#!/usr/bin/env python
import gatheros_exec
import gatheros_show
import gatheros

import argparse
import sys, os
import tempfile

parser = argparse.ArgumentParser( description = "A tool for System Enumeration and Presentation" )

temp = tempfile.NamedTemporaryFile( delete = True )

parser.add_argument( "-E", "--execute", help = "Arguments to 'Exec' module", type = str, default = "-o %s local" % temp.name )

parser.add_argument( "-S", "--show", help = "Arguments to 'Show' module", default = "%s -L" % temp.name, type = str )

parser.add_argument( "--live", help = "Keep the connection alive and add a Live Command handler to the WebPage",\
						default = False, action = 'store_true'  )


def main( arguments = sys.argv[1:] ) :

	# print arguments
	args = parser.parse_args( arguments )
	# print args
	execute_args = " -q " + args.execute
	print "Running 'execute' module with '%s' arguments" % execute_args
	command_dict = gatheros_exec.main( execute_args.split() )
	execUnit = gatheros_exec.getExecutionUnit()

	show_args = args.show
	print "Running 'show' module with '%s' arguments" % show_args
	if args.live :
		gatheros_show.main( show_args.split(), execUnit , command_dict = command_dict )	
	else :
		gatheros_show.main( show_args.split(), command_dict = command_dict )


if __name__ == '__main__' :

	main()