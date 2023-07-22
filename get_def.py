# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         get_def.py
# Purpose:      Retrieve definition from data/littre.txt and print it to the
#               terminal at start with a butch of nice cowsay's frogs.
#
# Authors:      Antoine Le Doeuff
#
# Copyright:    x
# License:      x
# ------------------------------------------------------------------------------

import os
import subprocess
from get_littre import *

# Set current dir
dir = os.path.dirname(os.path.abspath(__name__))

luck = random.randint(1, 5)

if luck <= 2:
    get_french_writers(dir)

    with open(f'{dir}/show_def.sh', 'w') as def_res:
        def_res.write(
            f"#!/bin/bash \n"
            f"echo -e '\n' >> '{dir}/result/def.txt' \n"
            f"cat '{dir}/result/def.txt' | cowsay -f bud-frogs | lolcat \n"
        )

else:
    find_littre(dir)

    with open(f'{dir}/show_def.sh', 'w') as def_res:
        def_res.write(
            f"#!/bin/bash \n"
            f"echo -e '\n' >> '{dir}/result/def.txt' \n"
            f"head -n 1 '{dir}/result/def.txt' | cowsay -f bud-frogs | lolcat \n"
            f"cat '{dir}/result/def.txt'"
        )

# ==========================================
# EDIT BASH
# ==========================================


# Add execution to the file
exe = f"chmod +x {dir}/show_def.sh"
subprocess.run(exe, shell=True)

# Run the command
run = f"bash {dir}/show_def.sh"
subprocess.run(run, shell=True)
