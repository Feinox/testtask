import socket, time



class Client():

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.setting_server = (host, 9090)
		self.shutdown = False
		self.join = False

		self.connect_client()


	def connect_client(self):

		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client.bind((self.host, self.port))

		alias = input("Name client: ")

		while self.shutdown == False:

			if self.join == False:
				client.sendto((" join chat ").encode("utf-8"), self.setting_server)
				self.join = True

			else:
				try:  #блок для предохранения
					message = input()
					if message != "":
						client.sendto((message).encode("utf-8"), self.setting_server)

						"""Принятие ответа и вывод"""
						data, addr = client.recvfrom(1024)

						print(data.decode("utf-8"))

					time.sleep(0.2)

				except:
					client.sendto(
						("[" + alias + "] <= left chat ").encode("utf-8"),
						self.setting_server)

					self.shutdown = True

		client.close()



if __name__ == '__main__':

	#HOST = socket.gethostbyname(socket.gethostname())
	HOST = "192.168.1.25"
	PORT = 0

	Client(HOST, PORT)
