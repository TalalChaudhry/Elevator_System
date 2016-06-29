# Elevator_System

# Requirements
- Python 3
- Numpy installed

# How to run and description
This tool simulats an elevator System. The main file ElevatorSystem.py and two accompanying examples are well documented to understand the code. This is a short description of it.

- First import the class from the ElevatorSystem.py file:
```
from ElevatorSystem import ElevatorSystem 
```
- Then make an instance of the class (input the number of elevators, default = 16):
```
system = ElevatorSystem(<number of elevators>)
```
- Now you can use two of the functions: pick and step. The pick function is a request to pick up a passenger. Inputs to pick function are floor number of passenger and direction (-1 for down, +1 for up, 0 for none). The step function processes time and updates the statuses of elevators. Input to step function is time in seconds. An example of the way they can be called:
```
system.pick(4,1)
system.step(3)
system.pick(8,-1)
system.pick(5,1)
system.step(2)
```
- The class also has one other function: update_status. This just updates the status of each elevator: its current floor, destination floors and direction. This shouldnt be called by the user



