# Accept keyboard commands to control the rover
from pynput import keyboard
from rover import Rover
from mobility import Mobility
import argparse

HOST = '192.168.29.139'
PORT = 9999


def main():
    # Request parameters
    parser = argparse.ArgumentParser(
        description='Manually control rover mobility')
    # HOST
    parser.add_argument('-H', '--host', type=str, default=HOST,
                        help="Host IP (default: {})".format(HOST))
    # PORT
    parser.add_argument('-P', '--port', type=int, default=PORT,
                        help="Port Number (default: {})".format(PORT))
    # VERBOSITY
    parser.add_argument('-v', '--verbosity', type=int,
                        default=1, help='Verbosity level')
    args = parser.parse_args()

    # Initialize Rover
    rover = Rover((args.host, args.port))
    # Connect to the rover
    rover.connect()

    # Initialize Mobility
    mobility = Mobility(rover, args.verbosity)

    # Setup the keyboard listener
    def on_press(key):
        if key == keyboard.Key.up:
            mobility.increaseLinearSpeed()
        elif key == keyboard.Key.down:
            mobility.decreaseLinearSpeed()
        elif key == keyboard.Key.right:
            mobility.increaseTransverseSpeed()
        elif key == keyboard.Key.left:
            mobility.decreaseTransverseSpeed()
        elif key == keyboard.Key.space:
            mobility.stop()

    def on_release(key):
        if key == keyboard.Key.esc:
            return False
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

    # Start the listener
    listener.start()


if __name__ == '__main__':
    main()
