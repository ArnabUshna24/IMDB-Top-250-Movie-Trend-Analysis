# Trend Analysis: IMDB - Top 250 Movies of All Time

## Overview
This project was focused on IMDB's [Top 250 Movies](https://www.imdb.com/chart/top/?ref_=nv_mv_250) of all time to gain insights on movie genre preference of the audiences. It serves the following concerns:
* Scraping a dynamic website and retrieving data.
* Finding and handling missing data properly.
* Investigating interesting trends or patterns from the data by creating visualizations in Tableau.

## Dynamic Web Scraping
Selenium was used to build web scrapers to retrieve data on top 250 movies of all time from IMDB website. Six (6) columns were considered for this dataset, i.e., `Rank`, `Title`, `Release`, `Runtime`, `Rated`, and `Ratings`. Since the columns do not have same number of entries, data were scraped separately (by making 3 separate scrapers) considering the uneven number of column entries.
* `scraper.py`: `Rank`, `Title`
* `scraper_2.py`: `Release`, `Runtime`, `Rated`
* `scraper_3.py`: `Ratings`

## Data Preprocessing, Transformation and Manipulation
After generating three (3) `.csv` files from VS Code, column entries were manually adjusted in MS Excel as every column does not have same number of entries. Then, the missing values were handled in Google Colab using Python.

## [Dashboard Preview](https://public.tableau.com/app/profile/arnab.naha.ushna/viz/Top250IMDBMovies_17382266796240/Top250IMDBMovies)
![Tableau Visualization](https://github.com/ArnabUshna24/IMDB-Top-250-Movies-of-All-Time/blob/main/dashboard_screenshot.jpg)

## Interesting Findings
* Among the 250 movies, the most number of movies (8) were released in 1995.
* The highest average rating for the released movie(s) in a calendar year (9.2) was in 1972.
* Most of the movies (101) are R-rated, having an average rating of approximately 8.33.
* The Shawshank Redemption, Star Wars: Episode V - The Empire Strikes Back, and The Dark Knight are the highest ranked movies in R, PG and PG-13 categories, respectively.

## Build from Source
1. Clone repository
   ```python
   git clone https://github.com/ArnabUshna24/IMDB-Top-250-Movie-Trend-Analysis.git
2. Initialize virtual environment
   ```python
   virtualenv venv
3. Activate virtual environment
   ```python
   source ./venv/bin/activate
4. Install dependencies
   ```python
   pip install -r requirements.txt
5. Run `scraper.py`, `scraper_2.py`, and `scraper_3.py` files to scrape the data and generate the `.csv` files.


For any queries, contact me: arnabnushna24@gmail.com
