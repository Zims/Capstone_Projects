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
# big_width = (4.0, 2.2)
# short_width = (3.0, 2.2)
# tile_size = (0.2, 0.3)
extra_tile = 1.15


def get_lenght():
    while type(input) != int or float:
        try:
            x_lenght = float(input('*  The floor length in meters? '))
            return x_lenght
        except ValueError:
            print('Sorry, use a number! (50cm = 0.5)')


def get_width():
    while type(input) != int or float:
        try:
            y_width = float(input('*  The floor width in meters? '))
            return y_width
        except ValueError:
            print('Sorry, use a number! (50cm = 0.5)')
        else:
            print(y_width)

def get_price():
    sq_m = get_lenght() * get_width()
    price_sqm = None
    while type(price_sqm) != int or float:
        try:
            price_sqm = float(input('*  The price per sqm? '))
        except ValueError:
            print('Sorry, price in USD!')
        else:
            print('*'*58)
            extra = round(sq_m * extra_tile, 2)
            print(f'*  You raw diameters are {sq_m} sq/m but we advise 15% extra. \n*  That is {extra} sq/m\n')
            whole_price = sq_m * 1.15 * price_sqm
            print(f'             ✅ The whole price is {whole_price} USD.✅ \n\n*  Type in different price or press Ctrl + C to exit \n*  or start over for different room.')
            print('/\\'*29)


get_price()
# get_width()