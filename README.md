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
- Then make an instance of the class:
```
system = ElevatorSystem(<number of elevators>)
```
- Now you can use two of the functions: pick and step. The pick function is a request to pick up a passenger. Inputs to pick function are floor number of passenger and direction (-1 for down, +1 for up, 0 for none). The step function processes time and updates the statuses of elevators. Input to step function is time in seconds.

