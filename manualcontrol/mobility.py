# Commands for manually controlling rover mobility
from rover import Rover
import argparse

STEPSIZE_a = 1
STEPSIZE_d = 1


class Mobility():
    def __init__(self, rover, verbosity=1):
        self.rover = rover
        self.verbosity = verbosity

    def increaseLinearSpeed(self):
        self.rover.updateState(linear=min(
            self.rover.linearSpeed + STEPSIZE_a, 100))

    def decreaseLinearSpeed(self):
        self.rover.updateState(linear=max(
            self.rover.linearSpeed - STEPSIZE_a, -100))

    def increaseTransverseSpeed(self):
        self.rover.updateState(transverse=min(
            self.rover.transverseSpeed + STEPSIZE_a, 100))

    def decreaseTransverseSpeed(self):
        self.rover.updateState(transverse=max(
            self.rover.transverseSpeed - STEPSIZE_a, -100))

    def stop(self):
        self.rover.updateState(linear=0, transverse=0)

    def decelerate(self):
        # TODO: Implement deceleration
        pass

# TESTING


def main():
    parser = argparse.ArgumentParser(
        description='Manually control rover mobility')
    # HOST
    parser.add_argument('-H', '--host', type=str, default='192.168.29.139',
                        help="Host IP (default: 192.168.29.139)")
    # PORT
    parser.add_argument('-P', '--port', type=int, default=9999,
                        help="Port Number (default: 9999)")
    # VERBOSITY
    parser.add_argument('-v', '--verbosity', type=int,
                        default=1, help='Verbosity level')
    args = parser.parse_args()
    rover = Rover((args.host, args.port))
    rover.connect()
    mobility = Mobility(rover, args.verbosity)

    while True:
        print("\nCurrent state:")
        rover.printState()
        print("\nCommands:")
        print("\tIncrease linear speed:  i")
        print("\tDecrease linear speed:  d")
        print("\tIncrease transverse speed:  j")
        print("\tDecrease transverse speed:  k")
        print("\tStop:  s")
        print("\tDecelerate:  a")
        print("\tQuit:  q")
        command = input("\nEnter command: ")
        if command == 'i':
            mobility.increaseLinearSpeed()
        elif command == 'd':
            mobility.decreaseLinearSpeed()
        elif command == 'j':
            mobility.increaseTransverseSpeed()
        elif command == 'k':
            mobility.decreaseTransverseSpeed()
        elif command == 's':
            mobility.stop()
        elif command == 'a':
            mobility.decelerate()
        elif command == 'q':
            rover.disconnect()
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
