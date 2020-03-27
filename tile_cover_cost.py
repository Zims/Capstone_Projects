# Find Cost of Tile to Cover W x H Floor - 
# Calculate the total cost of tile it would take to cover a floor plan of width and height, 
# using a cost entered by the user. Visual or ui??? How to calculate the useless cuts?

# fitst calculate for a room 2x400*220cm and 2x300*220cm. Tile = 20*30cm. Price per m**2 = x. 
# Calculate needed m**2 to cover room. 

# Check length and width vs full tile count + count of tiles that are cut.


# Room size --
big_width = (400, 220)
short_width = (300, 220)
tile_size = (20, 30)


def get_price():
    while type(price_sqm) != int or float:
        try:
            price_sqm = float(input('Price per sqm? ')):
        except ValueError:
            print('Sorry, a bet must be an number!')
        else:
        if type(price_sqm) != int or float:


def sq_area(gabarites):
    return gabarites[0] * gabarites[1]

def combined_sq_area(big_wall, small_wall):
    return big_wall*2 + small_wall*2

big_wall = sq_area(big_width)
small_wall = sq_area(short_width)
tile_area = sq_area(tile_size)
whole_area = combined_sq_area(big_wall, small_wall)

print(big_wall)
print(small_wall)
print(tile_area)
print(whole_area)