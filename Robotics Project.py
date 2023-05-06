# Import the necessary modules
from controller import Robot

# Create a robot instance
robot = Robot()

# Get the motor devices
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the target position of the motors
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set the velocity of the motors
left_motor.setVelocity(0.5)
right_motor.setVelocity(0.5)

# Run the simulation
while robot.step(64) != -1:
    pass
