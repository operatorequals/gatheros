#!/usr/bin/env python
import gatheros_exec
import gatheros_show
import gatheros

import argparse
import sys, os
import tempfile

parser = argparse.ArgumentParser( description = "A tool for System Enumeration and Presentation" )

temp = tempfile.NamedTemporaryFile( delete = True )
# print temp
# sys.exit()
parser.add_argument( "--execute", help = "", type = str, default = "-o %s local" % temp.name )
# parser.add_argument( "--file", )

parser.add_argument( "--show", help = "", default = "%s -a localhost" % temp.name )




def main( arguments = sys.argv[1:] ) :

	# print arguments
	args = parser.parse_args( arguments )
	# print args
	print "Running 'execute' module with '%s' arguments" % args.execute
	command_dict = gatheros_exec.main( args.execute.split() )

	print "Running 'show' module with '%s' arguments" % args.show
	gatheros_show.main( args.show.split() )	


if __name__ == '__main__' :

	main()