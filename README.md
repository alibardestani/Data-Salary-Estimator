# Data Science Salary Estimator: Project Overview
* Developed a tool to estimate data science salaries (Mean Absolute Error ~ $11K) to assist data scientists in salary negotiations during job offers.
* Collected over 1000 job descriptions from Glassdoor using Python and Selenium.
* Extracted features from each job description to quantify the value of Python, Excel, AWS, and Spark skills.
* Optimized Linear, Lasso, and Random Forest Regressors using GridSearchCV to identify the best-performing model.
* Built a user-facing API with Flask.

## Code and Resources Used
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**Web Framework Requirements:** ```pip install -r requirements.txt```  
**Scraper GitHub Repository:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Tutorial Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask API Deployment:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
Enhanced the GitHub scraper repository (above) to gather 1000 job listings from Glassdoor.com. Each job entry included the following:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Ownership Type
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
After scraping, I cleaned and prepared the data for modeling, making the following adjustments and adding variables:

* Parsed numerical data from the salary field
* Created columns for employer-provided salaries and hourly wages
* Removed rows without salary information
* Parsed ratings from company information
* Added a new column for the company’s state
* Added a column to indicate if the job was based at the company’s headquarters
* Transformed the company founding date into its age
* Created columns to detect listed skills in job descriptions:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
* Columns for simplified job titles and seniority levels
* Column for description length

## EDA
Examined data distributions and value counts for various categorical variables. Some highlights are shown in the pivot tables below.

## Project Visualizations
![alt text](https://github.com/alibardestani/Data-Salary-Estimator/blob/master/Top-20.jpg)
![alt text](https://github.com/alibardestani/Data-Salary-Estimator/blob/master/DistributionT.jpg)
![alt text](https://github.com/alibardestani/Data-Salary-Estimator/blob/master/Distribution.jpg)
![alt text](https://github.com/alibardestani/Data-Salary-Estimator/blob/master/WordFreq.jpg "Job Description WordCloud")
![alt text](https://github.com/alibardestani/Data-Salary-Estimator/blob/707199225d5a4234e0e3787217b79a7b8165e46e/corr.jpg "Correlations")


## Model Building

Converted categorical variables to dummy variables and split the data into train and test sets (test size: 20%).

Three different models were tested and evaluated using Mean Absolute Error (MAE), chosen for ease of interpretation and robustness to outliers:

* **Multiple Linear Regression** – Baseline model
* **Lasso Regression** – Used for the sparse data generated by many categorical variables
* **Random Forest** – Selected for its suitability with sparse data

## Model Performance
The Random Forest model performed best on both test and validation sets.
* **Random Forest**: MAE = 11.22
* **Linear Regression**: MAE = 18.86
* **Ridge Regression**: MAE = 19.67

## Productionization
Built a Flask API endpoint hosted on a local server, following a TDS tutorial. This API endpoint receives a job listing as input and returns an estimated salary."
