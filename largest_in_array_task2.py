"""
Task 2 -  
Create a 2D array.
Find the index of the largest 2 array.
Display largest two arrays
"""

import random


def main():
    
    # 2 dimensional array
    two_d_array = get_two_dimensional_array()
    print "2D Aarray: {}".format(two_d_array)
    
    # displaying positions
    positions = list(get_largest_arrays_positions(two_d_array))
    print "Positions: {}".format(positions)
    
    # displaying largest arrays
    l_arrays = [two_d_array[positions[0]], two_d_array[positions[1]]]
    print "Largest two arrays: {}".format(l_arrays)
    

def get_largest_arrays_positions(two_d_array):
    """
    :param two_d_array:Two dimensional array
    :return: Largest two arrays and their postions
    """
    largest_arr_sum = second_largest_arr_sum = 0
    pos_largest = pos_second_largest = 0
    
    for pos, array in enumerate(two_d_array):
        
        array_sum = sum(array)
        
        if array_sum > largest_arr_sum:
            pos_largest = pos
            second_largest_arr_sum = largest_arr_sum
            largest_arr_sum = array_sum
        elif array_sum > second_largest_arr_sum and array_sum != largest_arr_sum:
            second_largest_arr_sum = array_sum
            pos_second_largest = pos

    return pos_largest, pos_second_largest
               

def get_two_dimensional_array():
    """
    :return: 2D array
    """
    width = 0
    height = 0
    while(True):
        try:
            width = int(raw_input("Width of Array( > 0): "))
            height = int(raw_input("Height of Array( > 0): "))
        except:
            print "Enter a valid number"
            continue
        
        if width >= 1 and height >= 1:
            break
        else:
            print "Array is empty....!"
            
    array = [[random.randint(0, 1) for index in xrange(width)] for index2 in xrange(height)]

    return array


if __name__ == '__main__':
    main()
