#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: "Greemesh Basnet"
Semester: Summer

The python code in this file is original work written by
"Greemesh Basnet". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: Assignment 2 by Greemesh.

'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action='store_true', help="Print sizes in human-readable format.")
    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    ...
    num = int(percent * length) # This step calculates the number of characters in '#'.
    num2 = length - num # This step calculates the number of spaces in this. 
    return '#' * num + ' ' * num2
# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    ...
    total_memory = 0
    meminfo_file = open('/proc/meminfo', 'r')
    
    for line in meminfo_file:
        if 'MemTotal:' in line:
            total_memory = int(line.split()[1]) #This step extracts the total memory. 
            break
    
    meminfo_file.close()
    return total_memory

def get_avail_mem() -> int:
    "return total memory that is currently in use"
    ...
    available_memory = 0
    meminfo_file = open('/proc/meminfo', 'r')
    
    for line in meminfo_file:
        if 'MemAvailable:' in line:
            available_memory = int(line.split()[1]) #This line is similar as above used in get_sys_mem. It extracts the available memory. 
            break
    
    meminfo_file.close()
    return available_memory

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    ...
    result = os.popen(f'pidof {app_name}').read().strip() #This steps give us PID after using pidof command.
    if result:
        return result.split() #This line returns list of pid.
    return[]

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    ...
    try:
        f = open(f'/proc/{proc_id}/status', 'r')
        for line in f:
            if 'VmRSS:' in line:
                return int(line.split()[1])
    except FileNotFoundError:
        pass
    return #This line returns if the PID is not found.

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB'] # This the units of memory used in this code. 
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...

    # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print
    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.
