# Paint Area Calculation

This project calculates the number of cans of paint required to cover a wall based on its height, width, and the coverage area per can of paint.

## Algorithm
The algorithm follows these steps:

### Input: The program prompts the user to enter three values:

  -  height: The height of the wall in meters (m).
  -  width: The width of the wall in meters (m).
  -  coverage: The area covered by a single can of paint in square meters (m²).

### Calculation:

  -  The program calculates the total wall area by multiplying the height and width: wall_area = height * width.

### Cans Required:

  -  To determine the number of paint cans needed, the program divides the total wall area by the coverage area per can and rounds the result up using the math.ceil function: num_of_cans = math.ceil(wall_area / coverage).

### Output:
  -  The program displays a message indicating the number of cans of paint required: "You'll need {num_of_cans} cans of paint.".
