import socket
import paramiko
import os, sys
import getpass

client = None
ssh = None

def runSocketCommand( comm ) :
	client.send( ' ' + comm + '\n')
	return client.recv(4096*2)

def runLocalhostCommand( comm ) :
	return os.popen( " " + comm ).read()

def runSSHCommand( comm ) :
	stdin, stdout, stderr = ssh.exec_command( comm )
	out = stdout.read()
	if not out :
		return stderr.read()
	return out


def get_command_execute ( args ) :
	global client
	global ssh
	if args.command == "bind" :
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		address = (args.IP, args.port )
		client.connect( address )
		runCommand = runSocketCommand


	elif args.command == "reverse" :
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server.bind( ("0.0.0.0", args.port ) )
		print "Waiting for the Reverse Shell at port %d" % args.port
		try :
			server.listen(5)
		except KeyboardInterrupt :
			print "Aborted by user..."
			sys.exit(-2)
		client, address = server.accept()
		runCommand = runSocketCommand


	elif args.command == "local" :
		runCommand = runLocalhostCommand


	elif args.command == "ssh" :

		user, host = args.connection.split('@')[:2]
		password = args.password
		if not password :
			password = getpass.getpass("(SSH) Password for user '%s': " % user)

		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
		try :
			ssh.connect( host , username = user, password = password, port = args.port )
		except paramiko.ssh_exception.AuthenticationException :
			print "Authentication Failed"
			sys.exit(-1)
		runCommand = runSSHCommand

	return runCommand