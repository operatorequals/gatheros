#!/usr/bin/env python
from execute.command_function import get_command_execute

import argparse
import sys, os
import json


parser = argparse.ArgumentParser( description = "A tool for remote system enumeration" )

parser.add_argument("--command-file", '-f',\
					help = "The file that contains the commands to run on the remote system in JSON format",\
					default = "commands/LinuxEnum.json" )

subparsers = parser.add_subparsers( help = "The connection type with the remote host", dest='command')

localhost_parser = subparsers.add_parser("local")

ssh_parser = subparsers.add_parser("ssh")
ssh_parser.add_argument("SSH_connection", default = "root@172.0.0.1",\
						 help = "SSH connection string. example: 'user@address'")
ssh_parser.add_argument("--port", '-p', help = "TCP port to SSH (default: 22)", default = 22, type = int)


bind_parser = subparsers.add_parser("bind")
bind_parser.add_argument("IP", help = "The IP address of the remote host")
bind_parser.add_argument("--port", '-p', help = "TCP port to connect (default: 4444)", default = 4444, type = int)


reverse_parser = subparsers.add_parser("reverse")
reverse_parser.add_argument("--port", '-p', help = "TCP port to wait for the shell (default: 4444)", default = 4444, type = int)

parser.add_argument("--output-file", '-o',\
					help = "The file to save the command output" )


def command_loader( json_file ) :
	with open( json_file, 'r' ) as file :
		ret = json.load( file )
	return ret


def execute( command_dict, execute_command ) :

	for command_group in command_dict['command_groups'] :
		# print command_group
		for command in command_dict['command_groups'][command_group] :
			# print command
			response = execute_command( command['command'] ).strip()
			try :
				response = response.decode('utf-8')
			except :
				pass
			command['response'] = response

	return command_dict



def main( arguments = sys.argv[1:] ) :

	args = parser.parse_args( arguments )
	print args
	command_dict = command_loader( args.command_file )

	execute_command = get_command_execute( args )
	execute( command_dict, execute_command )

	json_dump = json.dumps( command_dict, indent = 1 )
	if args.output_file :
		with open( args.output_file, 'w' ) as toWrite :
			toWrite.write( json_dump )
	else :
		print json_dump

	return command_dict


if __name__ == '__main__' :

	main()
