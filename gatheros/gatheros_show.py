#!/usr/bin/env python

import show.application as flask
import gatheros

import argparse
import sys, os
import json



parser = argparse.ArgumentParser( description = "A tool for presenting System information gathered by 'gatheros execute' module" )

bind_option = parser.add_mutually_exclusive_group()
bind_option.add_argument("-a", "--address",\
					help = "IP were the %s WebPage will be served" % gatheros.__name__, default = 'localhost')
bind_option.add_argument( "-G", "--global", help = "Sets the WebPage to global bind address", action = 'store_true')
bind_option.add_argument("-L", "--localhost", help = "Sets the WebPage to bind to localhost", action = 'store_true')

# parser.add_argument# Global
parser.add_argument("-p", "--port",\
					help = "Port were the %s WebPage will be served" % gatheros.__name__, type = int, default = 8085)
parser.add_argument("--quiet", "-q",\
					help = "Start the service without spawning a browser instance", action = "store_true", default = False)
parser.add_argument("file",\
					help = "Location of the 'gatheros' system info file to open", default = '-')



def show( command_dict, ip, port, execUnit = None ) :
	flask.commStruct = command_dict
	flask.execUnit = execUnit
	flask.flask_app.run( host = ip, port = port )


def main( arguments = sys.argv[1:], execUnit = None, command_dict = None ) :

	args = parser.parse_args( arguments )
	# print args
	if not command_dict :
		with open( args.file, 'r' ) as file :
			command_dict = json.load( file )

	# print args
	if vars(args)['global'] :		# collision with 'global' py keyword
		address = '0.0.0.0'
	elif args.localhost :
		address = 'localhost'
	else :
		address = args.address

	if not args.quiet :
		os.system(" firefox http://localhost:%d &" % ( args.port) )
	else :
		print "Starting Web Application at 'http://localhost:%d'" % args.port

	show( command_dict, address, args.port, execUnit )


if __name__ == '__main__' :

	main()