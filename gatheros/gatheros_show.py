#!/usr/bin/env python

import show.application as flask

import argparse
import sys, os
import json


parser = argparse.ArgumentParser( description = "A tool for presenting System information gathered by 'gatheros execute' module" )

parser.add_argument("-a" "--address",\
					help = "IP were the %s WebPage will be served" % sys.argv[0], default = 'localhost')
parser.add_argument("-p", "--port",\
					help = "Port were the %s WebPage will be served" % sys.argv[0], type = int, default = 8085)
parser.add_argument("--quiet","-q",\
					help = "Start the service without spawning a browser instance", action = "store_true", default = False)
parser.add_argument("file",\
					help = "Location of the 'gatheros' system info file to open")



def show( command_dict, ip, port ) :
	flask.commStruct = command_dict
	flask.flask_app.run( host = ip, port = port )


def main( arguments = sys.argv[1:] ) :

	args = parser.parse_args( arguments )
	# print args
	with open( args.file, 'r' ) as file :
		command_dict = json.load( file )

	if not args.quiet :
		os.system(" firefox http://localhost:%d &" % args.port)
	else :
		print "Starting Web Application at 'http://localhost:%d'" % args.port

	show( command_dict, args.a__address, args.port )


if __name__ == '__main__' :

	main()