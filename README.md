# DS-SalaryPredictor
Predicting Data Scientist Job Salaries: A data science project focused on predicting salaries for data scientists using machine learning techniques and relevant job market data.

## Installation
1. Make sure you have Python installed on your system.
2. Install the necessary dependencies by running the following command: pip install selenium pandas
3. Download and install the appropriate web driver for Selenium (e.g., ChromeDriver for Google Chrome).
- Visit the official Selenium documentation for detailed instructions on driver installation: [Selenium WebDrivers]
- (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

## Usage (Folder: 'scraper_rawdata')
1. Open the data scraping notebook (glassdoor/Naukri) in a text editor.
2. Customize the script to specify your desired scraping parameters, such as the target website, search queries, or any additional options.
3. Run the script on VS code or Jupyter environment.
4. The script will launch a web browser controlled by Selenium and start scraping the job data.
5. After the scraping process is complete, the raw data will be saved to a CSV file (`job_data.csv`).
6. If you require access to the raw data, I have included two CSV files in this folder."

### Data Description
The raw data (`...csv` files) obtained from the scraping process includes the following fields:
- Job Title: The title or position of the job.
- Company: The company offering the job position.
- Location: The location of the job.
- Salary: The salary estimate or range (if available).

## Usage (Folder: 'Clean_data')

This folder contains the cleaned datasets and the script used to clean the raw data.

### Contents

- `cleaning_rawdata.ipynb`: This Python script was used to clean the raw data and generate the cleaned datasets. It includes the necessary data cleaning steps, such as removing duplicates, handling missing values, and transforming the data.

- `salary_clean_glassdoor.csv`: This file is the cleaned version of "datascientist_salary_glassdoor.csv" under the 'scrapper_raw_data' folder.

- `salary_clean_naukri.csv`:This file is the cleaned version of "datascientist_salary_naukri.csv" under the 'scrapper_raw_data' folder. It has been processed to address data quality issues and is ready for analysis.

Feel free to explore the cleaned datasets and use them for further analysis or research purposes.

## Acknowledgments
- Ken Jee for providing inspiration and project ideas through his YouTube videos. 
  Note: The scripts and data included in this repository are my own work.
- The Selenium project for providing a powerful web automation framework.
- The Pandas library for data manipulation and analysis.

## Contact Information
For any questions or feedback, please contact me at pritigupta.ds@gmail.com

