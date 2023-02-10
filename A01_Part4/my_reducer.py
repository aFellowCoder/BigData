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


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    previous_stop_station = -1
    previous_station_log_time = -1

    count = 0

    while True:
        line = my_input_stream.readline().rstrip(")\n").lstrip("universal\t(").split(' @ ')

        # Here I check to see when end of file happens. Since variable "line" turns into a list when using split,
        # I check the first element
        if line[0] == '':
            break

        #print(line)
        #print(len(line))
        #print("\n")
        station_index = 2
        log_time_index = 1
        for i in range((int(len(line) / 4))):
            current_start_station = line[station_index]
            current_stop_station = line[station_index+1]
            current_log_time = line[log_time_index - 1]

            if (previous_stop_station != -1 and current_start_station != previous_stop_station):
                my_output_stream.write("By_Truck" + '\t' + "(" + previous_station_log_time + ", "
                                       + previous_stop_station + ", " + current_log_time + ", "
                                       + current_start_station + ")" + "\n")
                #print("current station:", current_start_station, "log time:", current_log_time)



            previous_stop_station = current_stop_station
            previous_station_log_time = line[log_time_index]

            station_index += 4
            log_time_index += 4


# print(count)
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
