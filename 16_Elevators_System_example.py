from ElevatorSystem import ElevatorSystem
from random import randint, choice

system = ElevatorSystem(16)
print('Elevator status [Current floor of Elevator, [{"floor": pick request floor, "direction": pick request direction}], current direction of elevator]', '\n')

# Loop how many times pick and call are called
for j in range(randint(1,16)):
    # Loop to call pick with different inputs random number of times
    for i in range(randint(1,16)):
        system.pick(randint(0,15), choice([-1,1]))

    print('####################')
    print('Elevators status')
    print(system.ele_status)
    print('####################', "\n")

    system.step(randint(1,10))

    print('####################')
    print('Elevators status')
    print(system.ele_status)
    print('####################', "\n")



