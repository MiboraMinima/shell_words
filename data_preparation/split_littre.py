# Split littre for efficience

import re

file_path = f'data/littre.txt'

with open(file_path, 'r') as file:
    littre = file.read()

# Find random def
all_def = r'_____\n\n(.*?)\n\n_____'
match_all = re.findall(all_def, littre, re.DOTALL)

n_file = 50
range_file = len(match_all) // n_file

for i in range(n_file):
    start_idx = i * range_file
    end_idx = start_idx + range_file if i < n_file - 1 else len(match_all)

    filename = f"data/littre/{i}_littre.txt"

    with open(filename, "a") as file:
        for y in range(start_idx, end_idx):
            file.write("\n\n_____\n\n")
            file.write(match_all[y])
