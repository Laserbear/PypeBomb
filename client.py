import socket

target_host = "0.0.0.0"
target_port = 9999

if(len(sys.argv) > 1):
     try:
          target_ip = sys.argv[1]
          target_port = int(sys.argv[2])
     except Exception:
          pass #lazy


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))
'''
client.send("ls")

response = client.recv(4096)

print "Output: " + response.rstrip("\n")
'''
while True:
	lmao = raw_input("Enter Command:\n")
	client.send(lmao)
	response = client.recv(4096)
	print "Output: " + response.rstrip("\n")
