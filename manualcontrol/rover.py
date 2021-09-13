# Implement Rover object to maintain and manage state
from connector import Connector


class Rover():
    def __init__(self, address):
        self.address = address
        self.linearSpeed = 0
        self.transverseSpeed = 0

    def connect(self):
        self.connector = Connector(*self.address)

    def updateState(self, linear, transverse):
        self.linearSpeed = linear if linear is not None else self.linearSpeed
        self.transverseSpeed = transverse if transverse is not None else self.transverseSpeed
        encoded = self.connector.encoder(
            self.linearSpeed, self.transverseSpeed)
        callback, duration = self.connector.send(encoded)
        self.printState()
        print("Received: {}\nDuration: {}".format(callback, duration))

    def printState(self):
        print("Linear speed: {}\nTransverse speed: {}".format(
            self.linearSpeed, self.transverseSpeed))

    def disconnect(self):
        self.connector.close()
