# Import the necessary modules
from controller import Robot, Keyboard

# Create a robot instance
robot = Robot()

# Get the motor devices
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the target position of the motors
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set the velocity of the motors
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Create a keyboard instance
keyboard = Keyboard()

# Enable the keyboard
keyboard.enable(64)

# Set the robot's initial direction
direction = 0.0

# Run the simulation
while robot.step(64) != -1:
    # Get the pressed key
    key = keyboard.getKey()

    # Update the robot's direction based on the pressed key
    if key == Keyboard.UP:
        left_motor.setVelocity(3.0)
        right_motor.setVelocity(3.0)
    elif key == Keyboard.DOWN:
        left_motor.setVelocity(-3.0)
        right_motor.setVelocity(-3.0)
    elif key == Keyboard.LEFT:
        direction += 0.1
        left_motor.setVelocity(2.0)
        right_motor.setVelocity(-2.0)
    elif key == Keyboard.RIGHT:
        direction -= 0.1
        left_motor.setVelocity(-2.0)
        right_motor.setVelocity(2.0)
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)

    # Set the robot's direction
    robot.setOrientation([0, 1, 0, direction])
