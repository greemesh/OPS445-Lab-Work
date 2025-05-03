#!/usr/bin/env python3
#Author ID:GBASNET

import subprocess
def free_space():
    outcome = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    output = outcome.stdout.decode("utf-8")
    lines = output.split("\n")
    for line in lines:
        if line.endswith("/"):
            return line.split()[3].strip()
        
if __name__ == '__main__':
     print(free_space())

        
    