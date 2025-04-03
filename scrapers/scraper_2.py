from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ["Release_Runtime_Rated"]

def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    
    movies = driver.find_elements(By.XPATH, "//span[@class='sc-ad5a2436-7 cJVQtZ cli-title-metadata-item']")
    movie_ratings = [ratings.text for ratings in movies]

    for ratings in movie_ratings:
        print(ratings)
    
    df = pd.DataFrame(movie_ratings, columns=columns)
    df.to_csv('Release_Runtime_Rated.csv', index=False, encoding='utf-8')

    print("CSV file 'Release_Runtime_Rated.csv' has been created.")

    driver.close()

if __name__ == "__main__":
    main()
