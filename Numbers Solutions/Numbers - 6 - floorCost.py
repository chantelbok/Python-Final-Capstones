"""Program to calculate the cost to tile a floor area. Question did not specify whether the cost is per m^2/ft^2
so ended up just assuming that it did."""


def cost_calc(width, length, cost):
    """
    Function to calculate cost
    """
    return width * length * cost


def main():  # Wrapper function

    floor_width = float(input('Please enter a number for the width of the floor '))
    floor_length = float(input('Please enter a number for the length of the floor '))
    tile_cost = float(input('Please enter a number for the cost per square '))
    print('Cost to tile the floor is:', cost_calc(floor_width, floor_length, tile_cost))


if __name__ == '__main__':
    main()
