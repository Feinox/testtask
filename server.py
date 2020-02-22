import socket, time
import random as rd



class Server():

	def __init__(self, host, port):
		self.host = host
		self.port = port


	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((self.host, self.port))

		quit = False
		print("[ Server Started ]")

		while not quit:
			try:
				data, addr = s.recvfrom(1024)

				connect_time = \
					time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
				print(f"[{addr[0]}]=[{str(addr[1])}]=[{connect_time}]/"
					  f"{data.decode('utf-8')}", end="\n")

				if data.decode("utf-8") == "number":
					""" отправка клиенты """
					s.sendto((str(rd.randint(1, 500))).encode("utf-8"), addr)

			except:
				print("\n[ Server Stopped ]")
				quit = True

		s.close()


if __name__ == "__main__":

	#HOST = socket.gethostbyname(socket.gethostname())
	HOST = "192.168.1.25"
	PORT = 9090

	Server(HOST, PORT).run()
