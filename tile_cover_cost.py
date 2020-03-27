# Find Cost of Tile to Cover W x H wall - 
# Calculate the total cost of tile it would take to cover a room, 
# using a cost entered by the user. Visual or ui???

# fitst calculate for a room 2x400*220cm and 2x300*220cm. Tile = 20*30cm. Price per m**2 = x. 
# Calculate needed m**2 to cover room. 

# CRATE x y axes input
# Advanced: Check length and width vs full tile count + count of tiles that are cut. 
# Or sq/m of full tiles + extra 1 for each row and collumn - 1

# Ask is it walls or floor. Seperate func for any choice


# Also, add 20% to the total square footage if the tigitle is being laid in a diagonal or diamond pattern. Try wakatime


# Room size --
# (x, z) = x is len. z is height
big_width = (4.0, 2.2)
short_width = (3.0, 2.2)
tile_size = (0.2, 0.3)
extra_tile = 1.15




def get_price():
    price_sqm = None
    while type(price_sqm) != int or float:
        try:
            price_sqm = float(input('The price per sqm? '))
        except ValueError:
            print('Sorry, price in USD!')
        else:

            whole_price = round(price_sqm * whole_area, 2)
            print(f'The whole price is {whole_price} USD. Press Ctrl + C to exit')


def sq_area(gabarites):
    return gabarites[0] * gabarites[1]

def wall_sq_area(x, z):
    return x*2 + z*2

def floor_sq_area(x, y):
    return x * y

big_wall = round(sq_area(big_width), 2)

small_wall = round(sq_area(short_width), 2)

tile_area = round(sq_area(tile_size), 3)

whole_area = round(wall_sq_area(big_wall, small_wall), 2)

should_buy = round(whole_area * extra_tile, 2)



# print(big_wall)
# print(small_wall)
# print(tile_area)
print(whole_area)
print(f'The whole area is {whole_area} sq/m')
print(f'To be on the safe side you should buy 15% extra tile. That\'s {should_buy} sq/m')

get_price()