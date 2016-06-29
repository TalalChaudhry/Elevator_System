import numpy as np

# simulates an elevator system
class ElevatorSystem:

    # Initializing. This contains status of all elevators
    def __init__ (self, number_of_elevators = None):
        number = 16 if number_of_elevators is None else number_of_elevators
        
        self.ele_status = [] 
        for i in range(number):
            self.ele_status.append([0, [], 0]) # [Elevator id, Current floor, [{pick request floor floor, pick request direction}], current direction of elevator]

    # This updates the status of elevators
    def update_status(self, ele_id, update_goal_floor, direction): 
        self.ele_status[ele_id][1].append({"floor": update_goal_floor, "direction": direction}) # adding floor/direction entry to destination
        self.ele_status[ele_id][2] = np.sign(self.ele_status[ele_id][1][0]["floor"] - self.ele_status[ele_id][0]) # updating elevator direction
        
        #If elevator going up, then sort floors in ascending order, and direction in descending
        if self.ele_status[ele_id][2] == 1:
            self.ele_status[ele_id][1].sort(key=lambda x:x['floor'])
            self.ele_status[ele_id][1].sort(key=lambda x:x['direction'], reverse = True)
        #Else if elevator going down, then sort floors in descending order, and direction in ascending
        elif self.ele_status[ele_id][2] == -1:
            self.ele_status[ele_id][1].sort(key=lambda x:x['floor'], reverse = True)
            self.ele_status[ele_id][1].sort(key=lambda x:x['direction'])

    # Function to make a pick up request. Determines optimum elevator to call and calls the status method to update that elevator
    def pick(self, floor_num, direction):
        #Initializing.
        difference_1 = [] # contains list of distances from pick request floor to only static elevators' current floor
        difference_2 = [] # contains list of distances from pick request floor to moving in same direction elevators' floor
        busy = [] # contains list of distances from pick request to moving in opposite direction elevators' floor

        # Looping over elevators' statuses
        for i,ele in enumerate(self.ele_status):
            if ele[2] == 0: # If an elevator is static
                if ele[0] == floor_num: # And if elevator is on same floor as request. That elevator is processed to pick up. Return function
                    self.update_status(i, floor_num, direction)
                    return 0
                # Input distance of all static elevators (but not on same floor) from the pick up request floor
                difference_1.append({"difference": abs(ele[0] - floor_num), "ele_id": i})
                
            elif ele[2] == direction: #Input distance of all moving elevators in the same direction as pick up request direction
                difference_2.append({"difference": abs(ele[0] - floor_num), "ele_id": i})
                
            else: #Input distance of all moving elevators but opposite direction.
                busy.append({"difference": abs(ele[0] - floor_num), "ele_id": i})
        
        # If any static elevator available, find the closest one and update the request to its status. return function
        if len(difference_1) > 0:
            difference_1.sort(key=lambda x:x['difference'])
            self.update_status(difference_1[0]["ele_id"], floor_num, direction)
            return 0
        
        # If any elevator moving in same direction available, find the closest one and update its status. return function
        if len(difference_2) > 0:
            difference_2.sort(key=lambda x:x['difference'])
            self.update_status(difference_2[0]["ele_id"], floor_num, direction)
            return 0
            
        # If all are busy and moving in opposite direction then just select the closest one.
        best_ele_busy = min(busy, key=lambda x:x["difference"])
        self.update_status(best_ele_busy["ele_id"], floor_num, direction)
        
        
    def step(self, time): # Function to process time and update the elevators' statuses
        for i in range(time): # Loop over how much time has passed
            for i,ele in enumerate(self.ele_status): # Loop over all the elevators' statuses
                if len(ele[1]) != 0: # If elevator is not static but moving
                    ele[0] += ele[2] # depending on the direction of the elevator, add or subtract a floor
                    if ele[0] == ele[1][0]["floor"]: # If the elevator reaches the floor of its (first) destination
                        ele[1].pop(0) # Remove that entry as the pickup request has been processed
                        if len(ele[1]) == 0: # If elevator has no further destinations to go to
                            ele[2] = 0 # Set its direction to 0. Now it is static
                        else:    
                            ele[2] = np.sign(ele[1][0]["floor"] - ele[0]) # Set its direction towards the next destination's floor
                    
                


