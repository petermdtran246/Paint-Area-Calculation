import math
def paint_calc(height, width, cover):
    num_of_cans = (test_h * test_w) / 5
    print(f"You'll need {math.ceil(num_of_cans)} cans of paint.")


test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
# Keyword arguments
paint_calc(height=test_h, width=test_w, cover=coverage)