import unittest
import collections

# part 1
# Directions Transformers
DIRECTIONS = {"N": 0, "E": 1, "S": 2, "W": 3}
REVERSE_DIRECTIONS = {0: "N", 1: "E", 2: "S", 3: "W"}
MOVES = {
    0: (0, 1),  # Move up (increase y)
    1: (1, 0),  # Move right (increase x)
    2: (0, -1), # Move down (decrease y)
    3: (-1, 0)  # Move left (decrease x)
}

# Returns Number representing direction
def rotate(direction, turn):
    # turn left
    if turn == 'L':
        if direction == 0:
            direction = 3
        else:
            direction = direction - 1  # Turn left
        return direction
    # turn right
    elif turn == 'R':
        return (direction+1) % 4
    # no turn
    return direction

# Move Car
# Main Functionality
def moveCar(grid_size, start_pos, start_dir, instructions):
    # extract starting position
    x, y = start_pos
    # convert direction to number format
    direction = DIRECTIONS[start_dir]

    # parse instructions
    for instruction in instructions:
        # rotate
        if instruction == "L" or instruction == "R":
            direction = rotate(direction, instruction)
        # move forward
        elif instruction == 'F':
            i, j = MOVES[direction]
            newX = x + i
            newY = y + j
            # if out of bounds ignore command
            if newX in range(grid_size[0]) and newY in range(grid_size[1]):
                x,y = newX, newY

    final_dir = REVERSE_DIRECTIONS[direction]
    return (x, y), final_dir

# part 2

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

def moveCarCollisions(cars, grid_size):
    collision_events = []

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
    
    # check if cars collide at starting positions
    isCollided, collisions = checkCollisions(positions)
    if isCollided:
        for pos, car_ids in collisions.items():
            collision_events.append({
                'cars': sorted(car_ids),
                'position': pos,
                'step': 0
            })
        return collision_events

    # start moving cars step-by-step, checking for collisions
    for step in range(maxSteps):
        for car_id, car in cars.items():
            # check if there are instructions for car_id to execute at step
            if step < len(car[2]):
                # if valid, apply instruction, reuse code logic in part 1
                positions[car_id], directions[car_id] = moveCar(grid_size, positions[car_id], directions[car_id], car[2][step])
        # if collisions, return
        isCollided, collisions = checkCollisions(positions)
        if isCollided:
            for pos, car_ids in collisions.items():
                collision_events.append({
                    'cars': sorted(car_ids),
                    'position': pos,
                    'step': step+1
                })
            return collision_events
    # if no collisions
    print("no collisions")
    return collision_events


class TestMoveCar(unittest.TestCase):
    def test_case_1(self):
        """Test 1 - Same as provided test case"""
        grid_size = (10, 10)
        start_pos = (1, 2)
        start_dir = 'N'
        instructions = "FFRFFFRRLF"
        expected_pos = (4, 3)
        expected_dir = 'S'
        self.assertEqual(moveCar(grid_size, start_pos, start_dir, instructions), (expected_pos, expected_dir))

    def test_case_2(self):
        """Test 2 - Out of bounds start, shouldn't move"""
        grid_size = (2, 2)
        start_pos = (1, 2)
        start_dir = 'N'
        instructions = "RFFFF"
        expected_pos = (1, 2)  # Out of bounds, so should stay at (1, 2)
        expected_dir = 'E'
        self.assertEqual(moveCar(grid_size, start_pos, start_dir, instructions), (expected_pos, expected_dir))

    def test_case_3(self):
        """Test 3 - Out of bounds test, should end up on grid edge"""
        grid_size = (3, 3)
        start_pos = (1, 2)
        start_dir = 'N'
        instructions = "RFFFF"
        expected_pos = (2, 2)  # Stops at grid boundary (2,2)
        expected_dir = 'E'
        self.assertEqual(moveCar(grid_size, start_pos, start_dir, instructions), (expected_pos, expected_dir))

    def test_case_4(self):
        """Test 4 - Full rotation to the left and move"""
        grid_size = (5, 5)
        start_pos = (2, 2)
        start_dir = 'N'
        instructions = "LLLFFF"  # Should face 'E' and move forward 3 units
        expected_pos = (4, 2)  # Moves east 3 units
        expected_dir = 'E'
        self.assertEqual(moveCar(grid_size, start_pos, start_dir, instructions), (expected_pos, expected_dir))

    def test_case_5(self):
        """Test 5 - Only turning in place, no movement"""
        grid_size = (5, 5)
        start_pos = (3, 3)
        start_dir = 'W'
        instructions = "RRRR"  # Turns 360 degrees, should still face 'W'
        expected_pos = (3, 3)  # No movement
        expected_dir = 'W'
        self.assertEqual(moveCar(grid_size, start_pos, start_dir, instructions), (expected_pos, expected_dir))

    # Add more test cases...

class TestCollisions(unittest.TestCase):
    def test_case_1(self):
        """Test 1 - Same as provided test case"""
        grid_size = (10, 10)
        cars = {
            "A": ((1,2), "N", "FFRFFFFRRL"),
            "B": ((7,8), "W", "FFLFFFFFFF")
        }
        expected_collision_events = [
            {'cars': ['A', 'B'], 'position': (5, 4), 'step': 7},
        ]
        self.assertEqual(moveCarCollisions(cars, grid_size), expected_collision_events)
    
    def test_case_2(self):
        """Test 2 - collide on starting position"""
        grid_size = (10, 10)
        cars = {
            "A": ((1,2), "N", "FFRFFFFRRL"),
            "B": ((7,8), "W", "FFLFFFFFFF"),
            "C": ((1,2), "N", "FFRFFFFRRL"),
            "D": ((7,8), "W", "FFLFFFFFFF")
        }
        expected_collision_events = [
            {'cars': ['A', 'C'], 'position': (1, 2), 'step': 0},
            {'cars': ['B', 'D'], 'position': (7, 8), 'step': 0},
        ]

        self.assertEqual(moveCarCollisions(cars, grid_size), expected_collision_events)

    def test_case_3(self):
        """Test 3 - No collisions, cars move straight and avoid each other"""
        grid_size = (10, 10)
        cars = {
            "A": ((0, 0), "E", "FFFFFFFFF"),  # Moves east across the grid
            "B": ((9, 9), "W", "FFFFFFFFF"),  # Moves west across the grid
        }
        expected_collision_events = []  # No collisions expected

        self.assertEqual(moveCarCollisions(cars, grid_size), expected_collision_events)



if __name__ == '__main__':
    # test part 1
    print("===PART 1===")
    loader = unittest.TestLoader()
    suite_part_one = loader.loadTestsFromTestCase(TestMoveCar)
    runner = unittest.TextTestRunner()
    runner.run(suite_part_one)
    
    # test part 2
    print("===PART 2===")
    loader = unittest.TestLoader()
    suite_part_two = loader.loadTestsFromTestCase(TestCollisions)
    runner = unittest.TextTestRunner()
    runner.run(suite_part_two)

