import pandas as pd
import wikiquote

# TODO: try a better method

who = "philo" # in [french, philo]

if who == "french":
    writer = pd.read_csv('data/french_writers.csv')
    failed_authors_file = 'data/wiki_failed_fr_writers.txt'
else:
    writer = pd.read_csv('data/philosophers.csv')
    failed_authors_file = 'data/wiki_failed_philo.txt'

languages = ['fr', 'en']
nb_aut = len(writer)
for i, row in writer.iterrows():
    author = row['author']

    if who == "french":
        birth = row['birth']
        death = row['death']
    else:
        birth_death = row["birth_death"]

    print(f"{author}, ({i + 1} / {nb_aut})")

    quote = None
    first_try_successful = False
    try:
        # Perform the wikiquote search with the current author
        res_search = False
        y = 0
        while not res_search and y < len(languages):
            try:
                res_search = wikiquote.search(author, lang=languages[y])
            except Exception as e:
                print(f"Not found for {languages[y]} due to exception: {e}")
            y += 1

        if res_search:
            if res_search[0] == author:
                # Try getting quotes for the full author name
                y = 0
                while not quote and y < len(languages):
                    try :
                        quote = wikiquote.quotes(author, max_quotes=1, lang=languages[y])
                    except Exception as e:
                        print(f"Not found for {languages[y]} due to exception: {e}")
                    y += 1

                if quote:
                    first_try_successful = True
                    print("first try was successful !!\n")

    except Exception as e:
        pass

    if not first_try_successful:
        try:
            # Perform the wikiquote search using only the last name
            last_name = author.split()[-1]

            # Find for an existing of the author in both fr and eng
            res_search = False
            y = 0
            while not res_search and y < len(languages):
                try:
                    res_search = wikiquote.search(last_name, lang=languages[y])
                except Exception as e:
                    print(f"Not found for {languages[y]} due to exception: {e}")
                y += 1

            if res_search:
                res_split = res_search[0].split()
                # Check if there is really a correspondance between the authors passed and the author
                # retrieved
                if last_name in res_split:
                    # If the search returns a result, try to get a quote
                    y = 0
                    while not quote and y < len(languages):
                        try:
                            quote = wikiquote.quotes(res_search, max_quotes=1, lang=languages[y])
                        except Exception as e:
                            print(f"Not found for {languages[y]} due to exception: {e}")
                        y += 1

                    if quote:
                        print("Second try was successful\n")
                    else:
                        print("Second try failed\n")
                else:
                    print("Second try failed\n")
                    with open(failed_authors_file, 'a') as failed:
                        failed.write(f"{author}\n")
            else:
                print("Second try failed\n")
                with open(failed_authors_file, 'a') as failed:
                    failed.write(f"{author}\n")

        except Exception as e:
            # Catch any exception that may occur and add the author to the list of failed_authors
            with open(failed_authors_file, 'a') as failed:
                failed.write(f"{author}\n")

    if quote:
        if not death:
            death = " "
        elif not birth_death:
            birth_death = " "

        # Write the data
        filename = f'data/{who}_catch.csv'
        with open(filename, 'a') as def_res:
            if who == "french":
                def_res.write(f"{author},{birth},{death}\n")
            else:
                def_res.write(f"{author},{birth_death}\n")
    else:
        print(f"Nothing find\n")
