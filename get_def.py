# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         get_def.py
# Purpose:      Retrieve definition from data/littre.txt and print it to the
#               terminal with a butch of nice cowsay's frogs.
#
# Authors:      Antoine Le Doeuff
#
# Copyright:    x
# License:      x
# ------------------------------------------------------------------------------

import os
import re
import random
import subprocess

# Set current dir
dir = os.path.dirname(os.path.abspath(__name__))

# Set littre dictionnary path
file_path = f'{dir}/data/littre.txt'  # Replace with the actual file path

# Open it
with open(file_path, 'r') as file:
    littre = file.read()

# ==========================================
# FIND RANDOM DEF
# ==========================================

all_def = r'_____\n\n(.*?)\n\n_____'
match_all = re.findall(all_def, littre, re.DOTALL)

def_num = len(match_all)
rd_def = random.randint(1, def_num)

current_def = match_all[rd_def]

# Write the file
with open(f'{dir}/result/def.txt', 'w') as def_res:
    def_res.write(current_def)

# ==========================================
# EDIT BASH
# ==========================================
#  head -n 1 '{dir}/result/def.txt' | figlet -f smslant | lolcat

with open(f'{dir}/show_def.sh', 'w') as def_res:
    def_res.write(
        f"""
#!/bin/bash
        
echo "\n" >> '{dir}/result/def.txt' 
        
head -n 1 '{dir}/result/def.txt' | cowsay -f bud-frogs | lolcat
 
cat '{dir}/result/def.txt'
        """
    )

exe = f"chmod +x {dir}/show_def.sh"
subprocess.run(exe, shell=True)

run = f"bash {dir}/show_def.sh"
subprocess.run(run, shell=True)
