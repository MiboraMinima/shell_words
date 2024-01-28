import re
import random
import pandas as pd
import wikiquote
import subprocess
from urllib import request

# FIXME: inplace of generating find, return strings

class DefinitionGenerator:
    def __init__(self, dir):
        self.dir = dir

    def find_littre(self):
        # Set littre dictionnary path
        rand_file = random.randint(1, 49)
        file_path = f'{self.dir}/data/littre/{rand_file}_littre.txt'

        # Open it
        with open(file_path, 'r') as file:
            littre = file.read()

        # Find random def
        all_def = r'_____\n\n(.*?)\n\n_____'
        match_all = re.findall(all_def, littre, re.DOTALL)

        def_num = len(match_all)
        rd_def = random.randint(1, def_num)

        current_def = match_all[rd_def]

        # Write the file
        with open(f'{self.dir}/result/def.txt', 'w') as def_res:
            def_res.write(current_def)

    # FIXME: death consider as float
    def get_wikiquote(self, scope):
        # Load data
        data = pd.read_csv(
            f'data/{scope}_catch.csv', 
            dtype={
               'author': 'string',
               'birth': 'string',
               'death': 'string',
       })

        # Subtract 1 to avoid index out of range error
        rand_index = random.randint(0, len(data) - 1)  

        author = data.loc[rand_index, 'author']
        if scope == "french_writers":
            birth = data.loc[rand_index, 'birth']
            death = data.loc[rand_index, 'death']
        else:
            birth_death = data.loc[rand_index, 'birth_death']

        quote_list = wikiquote.quotes(author, lang='fr')
        if not quote_list:
            quote_list = wikiquote.quotes(author, lang='eng')

        i = random.randint(0,len(quote_list) - 1)
        quote = quote_list[i]

        if scope == "french_writers":
            if not death:
                death = " "
        else:
            if not birth_death:
                birth_death = " "

        with open(f'{self.dir}/result/def.txt', 'w') as def_res:
            if scope == "french_writers":
                def_res.write(
                    f"{quote}\n"
                    f"\n"
                    f"{author} ({birth} - {death})"
                )
            else:
                def_res.write(
                    f"{quote}\n"
                    f"\n"
                    f"{author} {birth_death}"
                )

    def generate_definition_script(self, ascii, con):
        # Based on luck and if there is a connexion, generate the definition
        # script
        if con:
            luck = random.randint(1, 9)
            if luck <= 3:
                self.get_wikiquote(scope="french_writers")
                get_type = "wiki"
            elif 3 < luck <= 6:
                self.get_wikiquote(scope="philo")
                get_type = "wiki"
            else:
                self.find_littre()
                get_type = "littre"
        else:
            self.find_littre()
            get_type = "littre"

        with open(f'{self.dir}/show_def.sh', 'w') as def_res:
            if get_type == "littre":
                def_res.write(
                    f"#!/bin/bash \n"
                    f"echo -e '\n' >> '{self.dir}/result/def.txt' \n"
                    f"head -n 1 '{self.dir}/result/def.txt' | cowsay -f {ascii} | lolcat \n"
                    f"cat '{self.dir}/result/def.txt'"
                )
            else:
                def_res.write(
                    f"#!/bin/bash \n"
                    f"echo -e '\n' >> '{self.dir}/result/def.txt' \n"
                    f"cat '{self.dir}/result/def.txt' | cowsay -f {ascii} | lolcat \n"
                )

    def execute_script(self):
        # Add execution to the file
        exe = f"chmod +x {self.dir}/show_def.sh"
        subprocess.run(exe, shell=True)

        # Run the command
        run = f"bash {self.dir}/show_def.sh"
        subprocess.run(run, shell=True)

def test_connection():
    try:
        request.urlopen('https://google.com', timeout=1)
        return True
    except request.URLError as err: 
        return False

