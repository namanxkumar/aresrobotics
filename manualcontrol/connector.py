# Client side connector code for manual keyboard control of the rover
import socket
import time
import argparse

HOST = '192.168.29.139'
PORT = 9999


class Connector():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.connect((self.host, self.port))

    def send(self, data):
        start = time.time()
        encoded = str.encode(data)
        self.s.send(encoded)
        callback = self.s.recv(1024)
        end = time.time()
        return callback, end - start

    def encoder(self, s1, s2):
        return '0,' + str(s1) + ',' + str(s2)

    def close(self):
        self.s.close()

# TESTING


def main():
    parser = argparse.ArgumentParser(description="Connection Testing")
    # HOST
    parser.add_argument('-H', '--host', type=str, default=HOST,
                        help="Host IP (default: 192.168.29.139)")
    # PORT
    parser.add_argument('-P', '--port', type=int, default=PORT,
                        help="Port Number (default: 9999)")
    # Parse Arguments
    args = parser.parse_args()

    # Connect to Server
    c = Connector(args.host, args.port)

    # Send Data
    data = input("Enter data to send: ")
    callback, time_taken = c.send(data)
    print("Callback: " + str(callback))
    print("Time taken: " + str(time_taken))

    # Close Connection
    c.close()


if __name__ == "__main__":
    main()
