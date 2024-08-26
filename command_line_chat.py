import socket
import threading

public_partner = None

host_ip_address = input('wat is het ip addres van de host ? ')
choice = input("Do you want to host (1) or to connect (2): ")

if choice == '1':
  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.bind((host_ip_address, 9999))
  server.listen()

  client, _ = server.accept()
elif choice == '2':
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.connect((host_ip_address, 9999))
else:
  exit()

def sending_messages(c):
  while True:
    message = input('')
    c.send(message.encode())
    print('you: ' + message)

def receiving_messages(c):
  while True:
    message = input('')
    c.send(message.encode())
    print('partner: ' + c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client)).start()
threading.Thread(target=receiving_messages, args=(client)).start()
