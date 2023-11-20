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
from fun import *

if __name__ == "__main__":
    # Set current dir
    current_dir = os.path.dirname(os.path.abspath(__name__))

    # Randomly choose in a cowsay list of ascii
    ascii_list = ['bunny', 'duck', 'bud-frogs', 'tux']
    ascii = random.choice(ascii_list)

    # Create an instance of DefinitionGenerator
    definition_generator = DefinitionGenerator(current_dir)

    # Generate definition script
    definition_generator.generate_definition_script(ascii)

    # Execute the script
    definition_generator.execute_script()
