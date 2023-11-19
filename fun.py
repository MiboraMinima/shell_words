import re
import random
import pandas as pd
import wikiquote

# TODO: just on function for fetching def

def find_littre(dir):

    # Set littre dictionnary path
    rand_file = random.randint(1, 49)
    file_path = f'{dir}/data/littre/{rand_file}_littre.txt'

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
    with open(f'{dir}/result/def.txt', 'w') as def_res:
        def_res.write(current_def)


def get_french_writers(dir):
    # Get quote of the day
    fr_writer = pd.read_csv('data/french_writers_catch.csv')

    # Random inside the file
    rand_index = random.randint(0, len(fr_writer) - 1)  # Subtract 1 to avoid index out of range error
    author = fr_writer.loc[rand_index, 'author']
    birth = str(fr_writer.loc[rand_index, 'birth'])
    death = str(fr_writer.loc[rand_index, 'death'])

    quote_list = wikiquote.quotes(author, lang='fr')
    i = random.randint(0,len(quote_list) - 1)
    quote = quote_list[i]

    if not death:
        death = " "

    with open(f'{dir}/result/def.txt', 'w') as def_res:
        def_res.write(
            f"{quote}\n"
            f"\n"
            f"{author} ({birth} - {death})"
        )

def get_philosophers(dir):
    # Get quote of the day
    philo = pd.read_csv('data/philo_catch.csv')

    # Random inside the file
    rand_index = random.randint(0, len(philo) - 1)  # Subtract 1 to avoid index out of range error
    author = philo.loc[rand_index, 'author']
    birth_death = philo.loc[rand_index, 'birth_death']

    quote_list = wikiquote.quotes(author, lang='fr')
    if not quote_list:
        quote_list = wikiquote.quotes(author, lang='eng')

    i = random.randint(0,len(quote_list) - 1)
    quote = quote_list[i]

    if not birth_death:
        birth_death = " "

    with open(f'{dir}/result/def.txt', 'w') as def_res:
        def_res.write(
            f"{quote}\n"
            f"\n"
            f"{author} {birth_death}"
        )
