# Elevator_System
A tool to simulate an Elevator System
# Requirements
- Python 3 (Python 2 is enough actually. But to display the prints in the example files better, python3 should be used)
- Numpy installed

# How to run and description
This tool simulats an elevator System. The main file ElevatorSystem.py and two accompanying examples are well documented to understand the code. This is a short description of it.

- First import the class from the ElevatorSystem.py file:
```
from ElevatorSystem import ElevatorSystem 
```
- Then make an instance of the class (input the number of elevators (positive number), default = 16):
```
system = ElevatorSystem(<number of elevators>)
```
- Now you can use two of the functions: pick and step. The pick function is a request to pick up a passenger. Inputs to pick function are floor number of passenger (>=0) and direction (-1 for down, +1 for up, 0 for none). The step function processes time and updates the statuses of elevators. Input to step function is time in seconds (>=0). One second is taken for any elevator to move one floor up or down. An example of the way they can be called:
```
system.pick(4,1)
system.step(3)
system.pick(8,-1)
system.pick(5,1)
system.step(2)
```
- The class also has one other function: update_status. This just updates the status of each elevator: its current floor, destination floors and direction. This should not be called by the user

# Functionality
This tool can simulate an elevator system. It can process several pick reqests and update the elevators accordingly. The optimum elevator is chosen for each requests using the following criteria with decreasing importance:
- The elevator that is static is favoured over elevators that are moving
- The elevator moving in same direction as the pick request is favoured over elevators that are moving in opposite direction
- The elevator that is closest to the pick request is favoured over others

To see the status of elevators, run the following command:
```
print (system.ele_status)
```
The output will be a list with each entry representing:
```
[Current floor of elevator, [{"floor": pick request floor, "direction": pick request direction}], current direction of elevator]
```
The entry in the list corresponds to the elevator ID.

# Accompanying examples
There are two accompanying examples: Easy_example.py and 16_Elevators_System_example.py. They are provided for the user to understand better. They are also documented.

# Improvements
Of course the code can be improved. For instance:
- After the pick up request is completed, another request to the floor where passenger wants to go could be processed.
- The criteria to choose the optimum elevator could be improved
- Checks can be added if inputs are incorrect.
- Testing