from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

columns = ["Ratings"]

def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Scraping ratings
    ratings = driver.find_elements(By.XPATH, "//span[@class='ipc-rating-star--rating']")
    rating_texts = [rate.text for rate in ratings]  # Extract text from WebElement

    # Print each rating
    for rate in rating_texts:
        print(rate)
    
    print(f"Total number of ratings: {len(rating_texts)}")

    df = pd.DataFrame(rating_texts, columns=columns)
    df.to_csv('Ratings.csv', index=False, encoding='utf-8')

    print("CSV file 'Ratings.csv' has been created.")

    driver.close()
    return

if __name__ == "__main__":
    main()
