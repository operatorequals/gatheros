#!/usr/bin/env python
import gatheros_execute
import gatheros_show
import gatheros

import argparse
import sys, os


parser = argparse.ArgumentParser( description = "A tool for System Enumeration and Presentation" )


parser.add_argument( "--execute", help = "", type = str )

parser.add_argument( "--show", help = "" )


'''
execute_command = None

command_dict = gatheros_execute.command_loader( json_file )


gatheros_execute.execute( command_dict, execute_command )


gatheros_show.show( command_dict )
'''


def main( arguments = sys.argv[1:] ) :

	print arguments
	args = parser.parse_args( arguments )
	print args
	gatheros_execute.main( args.execute.split() )



if __name__ == '__main__' :

	main()