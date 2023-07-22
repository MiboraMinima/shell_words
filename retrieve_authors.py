from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Replace 'your_url_here' with the URL of the webpage containing the desired elements
url = 'https://fr.wikipedia.org/wiki/Liste_alphab%C3%A9tique_d%27%C3%A9crivains_de_langue_fran%C3%A7aise'
driver = webdriver.Chrome()  # Make sure you have Chrome WebDriver installed and in your PATH
driver.get(url)

# Find the <div class='colonnes'> element
colonnes_div = driver.find_elements(By.CSS_SELECTOR, 'div.colonnes')

# Find all <ul> elements under the <div class='colonnes'>
dict_list = {}
for col in colonnes_div:
    ul_elements = col.find_elements(By.CSS_SELECTOR, 'ul')
    for ul in ul_elements:
        li_elements = ul.find_elements(By.CSS_SELECTOR, 'li')
        for li_element in li_elements:
            a_elements = li_element.find_elements(By.CSS_SELECTOR, 'a')
            author = None
            birth = None
            death = None
            for i, a_element in enumerate(a_elements):
                if i == 0:
                    author = a_element.text
                elif i ==1:
                    birth = a_element.text
                elif i ==2:
                    death = a_element.text

            df = pd.DataFrame({
                'author': [author],
                'birth': [birth],
                'death': [death],
            })

            id = f"{author[:3]}_{birth}"
            dict_list[id] = df

driver.quit()

df_all = pd.concat(dict_list)
df_all.sort_values('author', inplace=True)
df_all.reset_index(inplace=True, drop=True)

df_all.to_csv('data/french_writers.csv', index=False)
