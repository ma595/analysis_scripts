import csv, sys
import os.path
import math

# get the pile up height and the impact depth by finding the maximum 
# and minimum values respectively

# filestr
def max_min_func(filestr, output, index):
    pile_y = 0; pile_x = -1; depth_y = 1; depth_x = -1

    with open(filestr, 'r') as file:
        reader = csv.reader(file, delimiter=' ') 
        for row in reader:
            try: 
                a = float(row[1])
                if a > pile_y:
                    pile_y = a 
                    pile_x = float(row[0]) 
                if a < depth_y:
                    depth_y = a
                    depth_x = float(row[0])
            except ValueError: 
                continue 
        file.close()

        string_out = "\n" + repr(index) + " " + repr(pile_x) + \
        " " + repr(pile_y)+ " " + repr(depth_x) + " " + repr(depth_y)

        # if(os.path.exists(output)):
        #     with open(output, "a") as myfile:
        #         myfile.write(string_out) 
        #         myfile.close()
        # else:
        #     print("file doesn't exist")
        #     with open(output, "a") as myfile:
        #         myfile.write("# columns:  \n" + \
        #                      "# 0 index   \n" + \
        #                      "# 1 pile_x  \n" + \
        #                      "# 2 pile_y  \n" + \
        #                      "# 3 depth_x \n" + \
        #                      "# 4 depth_y \n")
        #         myfile.write(string_out) 
        #         myfile.close()
    return pile_y, depth_y, pile_x, depth_x

# p_y, d_y = max_min_func("test0000.curve.out", 0, "minmaxDepthPile.txt")

# # use this data to calculate the volume of the sphere enclosed 
# # we can choose to use the pile-up height as well, but for now
# # we ignore it.

# pi = math.pi
# d_y = math.fabs(p_y)
# R = 4.76/1000/2

# vol = (1./3.)*pi*d_y*d_y*(3*R-d_y)
# print("Volume of spherical cap = " + str(vol))
