from ElevatorSystem import ElevatorSystem

# calling class with 3 elevators
system = ElevatorSystem(3)

# Elevator status print format
print('Elevator status print format [Current floor of Elevator, [{"floor": pick request floor, "direction": pick request direction}], current direction of elevator]', '\n')

# 3 pick up calls
system.pick(3,1)
system.pick(5,-1)
system.pick(8,-1)

#print should show pick up calls in elevators status
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# calling step with 1 seconds
system.step(1)

# printing elevators status after step
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# pick call
system.pick(2, 1)

#print should show pick up calls in elevators status
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# calling step with 6 seconds
system.step(6)

# printing elevators status after step
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# pick calls
system.pick(1,-1)
system.pick(9,-1)

#print should show pick up calls in elevators status
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# calling step with 8 seconds
system.step(8)

# printing elevators status after step
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

#pick calls
system.pick(5,-1)

#print should show pick up calls in elevators status
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')

# calling step with 5 seconds
system.step(3)

# printing elevators status after step
print('####################')
print('Elevators status')
print(system.ele_status)
print('####################', '\n')