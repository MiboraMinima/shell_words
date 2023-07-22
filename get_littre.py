import re
import random
import pandas as pd
import wikiquote

def find_littre(dir):

    # Set littre dictionnary path
    file_path = f'{dir}/data/littre.txt'

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
    fr_writer = pd.read_csv('data/french_writers.csv')
    failed_authors_file = 'data/wiki_failed_fr_writers.txt'

    # Load the list of previously failed authors from the file
    try:
        with open(failed_authors_file, 'r') as file:
            failed_authors = [line.strip() for line in file]
    except FileNotFoundError:
        pass

    quote = None
    max_attempts = 50
    for _ in range(max_attempts):

        rand_index = random.randint(0, len(fr_writer) - 1)  # Subtract 1 to avoid index out of range error
        author = fr_writer.loc[rand_index, 'author']
        birth = fr_writer.loc[rand_index, 'birth']
        death = fr_writer.loc[rand_index, 'death']

        if author in failed_authors:
            continue

        first_try_successful = False
        try:
            # Perform the wikiquote search with the current author
            res_search = wikiquote.search(author)
            if res_search:
                if res_search[0] == author:
                    # Try getting quotes for the full author name
                    quote = wikiquote.quotes(author, max_quotes=1, lang='fr')
                    if quote:
                        # If quotes are successfully retrieved, set the boolean variable to True
                        first_try_successful = True

        except Exception as e:
            pass

        if not first_try_successful:
            try:
                # Perform the wikiquote search using only the last name
                last_name = author.split()[-1]
                res_search = wikiquote.search(last_name)
                if res_search:
                    res_split = res_search[0].split()
                    if last_name in res_split:
                        # If the search returns a result, get quotes for the last name
                        quote = wikiquote.quotes(res_search, max_quotes=1, lang='fr')
                    else:
                        with open(failed_authors_file, 'a') as failed:
                            failed.write(f"{author}\n")
                else:
                    with open(failed_authors_file, 'a') as failed:
                        failed.write(f"{author}\n")

            except Exception as e:
                # Catch any exception that may occur and add the author to the list of failed_authors
                with open(failed_authors_file, 'a') as failed:
                    failed.write(f"{author}\n")

        if quote:
            # If quotes are successfully retrieved, break out of the loop
            break

    if quote:
        if not death:
            death = " "

        with open(f'{dir}/result/def.txt', 'w') as def_res:
            def_res.write(
                f"{quote[0]}\n"
                f"\n"
                f"{author} ({birth} - {death})"
            )


def get_philosophers(dir):
    # Get quote of the day
    philo = pd.read_csv('data/philosophers.csv')
    failed_authors_file = 'data/wiki_failed_philo.txt'

    # Load the list of previously failed authors from the file
    try:
        with open(failed_authors_file, 'r') as file:
            failed_authors = [line.strip() for line in file]
    except FileNotFoundError:
        pass

    quote = None
    max_attempts = 50
    for _ in range(max_attempts):

        rand_index = random.randint(0, len(philo) - 1)  # Subtract 1 to avoid index out of range error
        author = philo.loc[rand_index, 'author']
        birth_death = philo.loc[rand_index, 'birth_death']

        if author in failed_authors:
            continue

        first_try_successful = False
        try:
            # Perform the wikiquote search with the current author
            res_search = wikiquote.search(author)
            if res_search:
                if res_search[0] == author:
                    # Try getting quotes for the full author name
                    quote = wikiquote.quotes(author, max_quotes=1, lang='fr')
                    if quote:
                        # If quotes are successfully retrieved, set the boolean variable to True
                        first_try_successful = True

        except Exception as e:
            pass

        if not first_try_successful:
            try:
                # Perform the wikiquote search using only the last name
                last_name = author.split()[-1]
                res_search = wikiquote.search(last_name)
                if res_search:
                    res_split = res_search[0].split()
                    if last_name in res_split:
                        # If the search returns a result, get quotes for the last name
                        quote = wikiquote.quotes(res_search, max_quotes=1, lang='fr')
                    else:
                        with open(failed_authors_file, 'a') as failed:
                            failed.write(f"{author}\n")
                else:
                    with open(failed_authors_file, 'a') as failed:
                        failed.write(f"{author}\n")

            except Exception as e:
                # Catch any exception that may occur and add the author to the list of failed_authors
                with open(failed_authors_file, 'a') as failed:
                    failed.write(f"{author}\n")

        if quote:
            # If quotes are successfully retrieved, break out of the loop
            break

    if quote:
        if not birth_death:
            birth_death = " "

        with open(f'{dir}/result/def.txt', 'w') as def_res:
            def_res.write(
                f"{quote[0]}\n"
                f"\n"
                f"{author} {birth_death}"
            )
