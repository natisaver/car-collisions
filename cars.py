# part 1
DIRECTIONS = {"N": 0, "E": 1, "S": 2, "W": 3}
REVERSE_DIRECTIONS = {0: "N", 1: "E", 2: "S", 3: "W"}

# move_car
def moveCar(grid_size, start_pos, start_dir, instructions):
    x, y = start_pos
    direction = DIRECTIONS[start_dir]
    
    for instruction in instructions:
        if instruction == 'L':
            direction = (direction - 1) % 4  # Turn left
        elif instruction == 'R':
            direction = (direction + 1) % 4  # Turn right
        elif instruction == 'F':
            if direction == 0:  # North
                new_y = y + 1
                if new_y < grid_size[1]:  # Ensure not out of bounds
                    y = new_y
            elif direction == 1:  # East
                new_x = x + 1
                if new_x < grid_size[0]:  # Ensure not out of bounds
                    x = new_x
            elif direction == 2:  # South
                new_y = y - 1
                if new_y >= 0:  # Ensure not out of bounds
                    y = new_y
            elif direction == 3:  # West
                new_x = x - 1
                if new_x >= 0:  # Ensure not out of bounds
                    x = new_x

    final_dir = REVERSE_DIRECTIONS[direction]
    return (x, y), final_dir

# part 2
import collections 

def checkCollisions(positions):
    collisions = {}
    visited = collections.defaultdict(list)
    
    # Check all cars' positions
    for car_id, pos in positions.items():
        visited[pos].append(car_id)
    
    # Check for positions where more than one car is present
    for pos, car_ids in visited.items():
        if len(car_ids) > 1:  # Collision detected
            collisions[pos] = car_ids
    
    if collisions:
        return True, collisions  # Return all collided cars
    return False, None

def partTwo(cars):
    positions = {}
    directions = {}
    maxSteps = 0
    for car_id, car in cars.items():
        # positions
        positions[car_id] = car[0]
        # directions
        directions[car_id] = car[1]
        # highest instruction length
        maxSteps = max(maxSteps, len(car[2]))
    
    # check if they collide at the start
    isCollided, collisions = checkCollisions(positions)
    if isCollided:
        for k,v in collisions.items:
            print(k)
            print(v)
        print(0)

    # move all cars and check for collisions
    for step in range(maxSteps):
        # move each car
        for car_id, instructions in cars.items():
            # check if there are any more instructions
            if step < len(car[2]):
                # use part 1
                positions[car_id], directions[car_id] = moveCar(grid_size, positions[car_id], directions[car_id], car[2][step])
        # print if any collisions
        isCollided, collisions = checkCollisions(positions)
        if isCollided:
            for k,v in collisions.items:
                print(k)
                print(v)
            print(step+1)
            break
    # if no collisions
    print("no collisions")


# test part 2
grid_size = (10, 10)
cars = {
    "A": ((1,2), "N", "FFRFFFFRRL"),
    "B": ((7,8), "W", "FFLFFFFFFF")
}

partTwo(cars)
