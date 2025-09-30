import sys
import os

## __file__ gives the full path to the current script file
current_script_path = __file__

## os.path.basename() extracts the filename from the full path
current_script_filename = os.path.basename(current_script_path)

## Check if enough arguments are provided
if len(sys.argv) < 4:
    print(f"Usage: Python {current_script_filename} name age address")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])
address = sys.argv[3]

print(f"You are {name}, {age} years old. \nYou lives in {address}.")
