
# Glassdoor - Data Scientist Salary Prediction

The objective of the project is to predict the average salary of a data scientist in the US according to the data on Glassdoor website.

## Overview

1. Created a tool that can estimate the data scientist salaries that can help data scientists determine the average salary according to the specifications, which may help them negotiate their salary.
2. Scrapped data from Glassdoor website using python and selenium.
3. Linear Regression, Lasso Regression and Random Forest Regressor models were created and evaluated. Optimised the model using GridsearchCV to get the best model.
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
Web Scrapping was done using selenium. The code available on the above mentioned github repo was modified according to the project's particular needs.

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

## Data Cleaning and Feature Engineering
Once the data was scrapped, data cleaning and feature Engineering was done in order to make suitable to create models.

- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
    * Python
    * R
    * Excel
    * AWS
    * Spark
- Column for simplified job title and Seniority
- Column for description length

## Exploratory Data Analysis
The data was explored for better understanding by creating plots and pivot tables. Here are some of the highlights that I found.
<img src="https://github.com/navi1910/Glassdoor-Data-Salary-Prediction/blob/main/Average%20Salary%20according%20to%20Job%20Position.png" width=25% height=25%>

<img src="https://github.com/navi1910/Glassdoor-Data-Salary-Prediction/blob/main/Average%20Salary%20according%20to%20Sector.png" width=25% height=25%>

<img src="https://github.com/navi1910/Glassdoor-Data-Salary-Prediction/blob/main/Correlation%20heatmap%20of%20the%20Attributes.png" width=30% height=30%>

<img src="https://github.com/navi1910/Glassdoor-Data-Salary-Prediction/blob/main/No.%20of%20job%20openings%20according%20to%20sector.png" width=30% height=30%>

## Model Building
- First we created dummy variables for the categorical variables. 
- The data was split into training data (80%) and testing data (20%).
- Three different models were created and they were evaluated using Mean Absolute Error.
- The Random Forest model was optimized using GridsearchCV to hypertune and obtain the best parameters for the model.

The three different models are:

* Multiple Linear Regression – Baseline for the model
* Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* Random Forest – Because of the sparsity associated with the data.

## Model Performance and Evaluation
The Random Forest Model which was optimized using GridsearchCV was the best model as it out-performed all the other models.

- Linear Regression: MAE - 826882167.7812284
- Lasso Regrssion: MAE - 24.265736178287195
- Random Forest Regressor - 17.919031712567097

## Productionization using Flask
In this step, a flask API endpoint was built(hosted on a local webserver).

The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

The reference used is mentioned above.
