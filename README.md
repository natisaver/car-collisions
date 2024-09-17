# car-collisions

## Features

- Simulates car movement on a grid.
- Supports turning left (L), turning right (R), and moving forward (F).
- Handles grid boundaries to prevent the car from moving out of bounds.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
   git clone https://github.com/natisaver/car-collisions.git
   cd car-collisions
```

### Running the Simulation
Make sure you are in the project folder car-collisions
- depending on python version, try either of the following commands to run the program
```bash
python3 cars.py
```

```bash
python cars.py
```

### Expected Output
You should see all 5 test cases pass for part 1
- And 3 test cases pass for part 2, since one of the test cases has no collisions, "no collisions" is printed out
```bash
PKTHP223TG:car-collisions username$ /usr/bin/python3 /Users/username/car-collisions/cars.py
===PART 1===
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
===PART 2===
..no collisions
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## Overview
We are testing two main functionalities:

#### Car Movement (moveCar):
Simulates a car moving within a grid based on initial position, direction, and movement instructions.

#### Collision Detection (moveCarCollisions):
Detects collisions between multiple cars on the grid based on their individual movements and positions.

## Test Suites
1. Car Movement Tests (TestMoveCar)
This test suite ensures that the moveCar function behaves correctly in different scenarios. The function simulates the movement of a car based on grid boundaries, start position, initial direction, and instructions.

Test Cases:
```
Test 1: Basic Movement and Turning
Cars follow a sequence of instructions and end at the expected position and direction.
Grid size: (10, 10)
Start position: (1, 2), facing N
Instructions: FFRFFFRRLF
Expected result: Final position (4, 3), facing S

Test 2: Out of Bounds - No Movement
The car starts out of bounds and doesn't move.
Grid size: (2, 2)
Start position: (1, 2) (out of bounds)
Instructions: RFFFF
Expected result: Position remains (1, 2), facing E

Test 3: Boundary Check - Stops at Edge
The car moves forward but stops when reaching the grid boundary.
Grid size: (3, 3)
Start position: (1, 2)
Instructions: RFFFF
Expected result: Final position (2, 2), facing E (stops at grid boundary)

Test 4: Full Rotation and Movement
The car makes a full rotation to the left and then moves forward.
Grid size: (5, 5)
Start position: (2, 2), facing N
Instructions: LLLFFF (rotates and moves)
Expected result: Final position (4, 2), facing E

Test 5: No Movement - Only Turning in Place
The car makes turns but does not move.
Grid size: (5, 5)
Start position: (3, 3), facing W
Instructions: RRRR (360-degree rotation)
Expected result: Position remains (3, 3), facing W
```

2. Collision Detection Tests (TestCollisions)
This test suite checks for collisions between multiple cars as they move within the grid. The moveCarCollisions function monitors the cars' movements and reports any collisions.

Test Cases:
```
Test 1: Single Collision After Several Steps
Two cars collide at a specific position after several steps.

Grid size: (10, 10)
Cars:
"A": Starts at (1, 2), facing N, instructions: FFRFFFFRRL
"B": Starts at (7, 8), facing W, instructions: FFLFFFFFFF
Expected collision:
Cars involved: ['A', 'B']
Collision position: (5, 4)
Step: 7

Test 2: Multiple Collisions at Starting Positions
Multiple cars collide at their starting positions.

Grid size: (10, 10)
Cars:
"A" and "C": Both start at (1, 2), facing N, same instructions
"B" and "D": Both start at (7, 8), facing W, same instructions
Expected collisions:
Cars involved: ['A', 'C'], collision at (1, 2), step 0
Cars involved: ['B', 'D'], collision at (7, 8), step 0

Test 3: No Collisions, Cars Avoid Each Other
Two cars move straight in opposite directions without colliding.

Grid size: (10, 10)
Cars:
"A": Starts at (0, 0), facing E, instructions: FFFFFFFFF (moves east)
"B": Starts at (9, 9), facing W, instructions: FFFFFFFFF (moves west)
Expected result: No collisions detected.

```
