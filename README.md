
# Glassdoor - Data Scientist Salary Prediction

The objective of the project is to predict the average salary of a data scientist in the US according to the data in the Glassdoor website.



## Overview

1. Created a tool that can estimate the data scientist salaries that can help data scientists determine the average salary according to the specifications, which may help them negotiate their salary.
2. Scrapped data from Glassdoor website using python and selenium.
3. Linear Regression, Lasso Regression and Random Forest models were created and evaluated. Optimised the model using GridsearchCV to get the best model.
4. Built client facing API using Flask.

## Code and Resources used

Python Version: 3.7

Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

For Web Framework Requirements: ```pip install -r requirements.txt```

 - [Git Hub repo](https://github.com/PlayingNumbers/ds_salary_proj)
 - [Scraper Github](https://github.com/arapfaik/scraping-glassdoor-selenium)
 - [Scraper Article](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)
 - [Flask Productionization](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)
 
## Acknowledgements

 - [Ken Jee Youtube Channel](https://www.youtube.com/c/KenJee1)

## Web Scrapping
Web Scrapping was done using selenium. The code available on the above mentioned github repo was modified according to my particular needs.

 The following attributes were scrapped for each job posting on Glassdoor.

- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors
