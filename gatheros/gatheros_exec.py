#!/usr/bin/env python
from execute.command_function import get_command_execute
from gatheros import __name__ as module_name
from execute.execution_unit import ExecutionUnit

import argparse
import sys, os
import json

base_dir = os.sep.join(__file__.split( os.sep )[:-1])

parser = argparse.ArgumentParser( description = "A tool for remote system enumeration" )

parser.add_argument( "--command-file", '-c',\
					help = "The file that contains the commands to run on the remote system in JSON format",\
					default = base_dir+"/commands/LinuxEnum.json" )

subparsers = parser.add_subparsers( help = "The connection type with the remote host", dest='command')

localhost_parser = subparsers.add_parser( "local" )

ssh_parser = subparsers.add_parser("ssh")
ssh_parser.add_argument("connection", default = "root@172.0.0.1",\
						 help = "SSH connection string. example: 'user@address'")
ssh_parser.add_argument("--port", '-p', help = "TCP port to SSH (default: 22)", default = 22, type = int)
ssh_parser.add_argument("--password", '-P',\
						help = "Password to use when connecting to server. If password is not given it's asked from the tty.")


bind_parser = subparsers.add_parser("bind")
bind_parser.add_argument("IP", help = "The IP address of the remote host")
bind_parser.add_argument("--port", '-p', help = "TCP port to connect (default: 4444)", default = 4444, type = int)


reverse_parser = subparsers.add_parser("reverse")
reverse_parser.add_argument("--port", '-p', help = "TCP port to wait for the shell (default: 4444)", default = 4444, type = int)

parser.add_argument("--output-file", '-o',\
					help = "The file to save the command output" )

# parser.add_argument("--quiet", '-q', help = "")

def command_loader( json_file ) :
	with open( json_file, 'r' ) as file :
		ret = json.load( file )
	return ret


def main( arguments = sys.argv[1:] ) :

	args = parser.parse_args( arguments )
	command_dict = command_loader( args.command_file )

	execute_command = get_command_execute( args )
	execUnit = ExecutionUnit( execute_command, command_dict )
	command_dict = execUnit.execute()

	json_dump = json.dumps( command_dict, indent = 1 )
	
	if args.output_file :
		with open( args.output_file, 'w' ) as toWrite :
			toWrite.write( json_dump )
	else :
		print json_dump

	# return command_dict


if __name__ == '__main__' :

	main()
