# Find Cost of Tile to Cover W x H Floor - 
# Calculate the total cost of tile it would take to cover a floor plan of width and height, 
# using a cost entered by the user. Visual or ui??? How to calculate the useless cuts?

# fitst calculate for a room 2x400*220cm and 2x300*220cm. Tile = 20*30cm. Price per m**2 = x. 
# Calculate needed m**2 to cover room. 


# Room size --
height = 220
big_width = 400
short_width = 300

def wall_sq_area(height, width):
    return height * width 

def combined_sq_area(big_wall, small_wall):
    return big_wall*2 + small_wall*2

big_wall = wall_sq_area(height, big_width)
small_wall = wall_sq_area(height, short_width)
whole_area = combined_sq_area(big_wall, small_wall)

print(big_wall)
print(small_wall)
print(whole_area)