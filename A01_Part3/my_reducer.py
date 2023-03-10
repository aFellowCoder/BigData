#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs
import re

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):

    current_station = -1
    arrival_count = 0
    depart_count = 0


    # Check if the below algorithm can be made more efficient.

    while True:
        line = my_input_stream.readline().rstrip().split("\t")
        #print(current_station)

        if current_station != -1 and current_station != line[0]:
            my_output_stream.write(str(current_station) + "\t" + "(" + str(arrival_count) + ", " + str(depart_count)
                                   + ")" + "\n")

            arrival_count, depart_count = 0, 0

        current_station = line[0]

        if line[0] == '':
            break

        dirty_res = (re.sub(r'[^a-zA-Z0-9]', ' ', line[1])).split(" ")
        clean_res = [w for w in dirty_res if w != ""]  # ----> Credit: Nacho's code

        arrival_count += int(clean_res[0])
        depart_count += int(clean_res[1])





    pass

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    my_reducer_input_parameters = []

    # 5. We call to my_reduce
    my_reduce(my_input_stream,
              my_output_stream,
              my_reducer_input_parameters
             )
