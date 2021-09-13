# Manual Control
This is the manual keyboard control library for the rover.

Current implementation allows for control of linear and transverse (left & right) speeds via arrow keys.

[ ] TODO: Implement rover arm (manipulator.py) control
[ ] TODO: Implement deceleration logic (mobility.py)

### Descriptions
- **connector:** Connects to the rover
- **mobility:** Provides a class with functions to control rover speed
- **rover:** Provides class to manage and maintain rover state
- **main:** Accepts keyboard input, initializes a Rover object, initializes a Mobility object (mobility-py) and is the file to be run by default.