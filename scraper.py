from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

columns = ["Rank", "Title"]

def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver = webdriver.Chrome()
    driver.get(url)

    # Rank & Title columns:
    rankings = driver.find_elements(By.XPATH, "//h3[@class='ipc-title__text']")
    movie_list = [rank.text for rank in rankings]
    movie_list = movie_list[1:251]

    movie_arrays = []
    for movie in movie_list:
        # Split at the first occurrence of a period followed by a space (this separates rank from title)
        rank, title = movie.split('.', 1)
        movie_arrays.append([rank.strip(), title.strip()])

    for movie in movie_arrays:
        print(f"['{movie[0]}', '{movie[1]}']")

    df = pd.DataFrame(movie_arrays, columns=columns)
    df.to_csv('Rank_Title.csv', index=False)

    print("CSV file 'Rank_Title.csv' has been created.")
    
    driver.close()
    return

if __name__ == "__main__":
    main()