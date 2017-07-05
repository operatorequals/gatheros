import socket
import paramiko
import os, sys
import getpass

# from time import sleep

client = None
ssh = None

def runSocketCommand( comm ) :
	canc_rand = os.urandom(4).encode('hex')
	compl_rand = os.urandom(4).encode('hex')
	
	command = ' ' + comm + ' && echo %s || echo %s \n' % ( compl_rand, canc_rand )
	print "> " + command,
	client.send( command )
	resp = ''

	while compl_rand not in resp and canc_rand not in resp :
		resp += client.recv( 4096 * 4 )
	resp = resp.strip()

	if compl_rand in resp :
		return resp.replace( compl_rand, '' )
	if canc_rand in resp :
		return ''

	return resp


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
		# client.settimeout(2)
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
		# client.settimeout(2)
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
		except paramiko.ssh_exception.NoValidConnectionsError :
			print "No SSH server found on port %s:%d" % (host, args.port)
			sys.exit(-2)
		runCommand = runSSHCommand

	return runCommand