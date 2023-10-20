# Data Jobs Analysis Project

## Overview

This collaborative project involves the analysis of data analyst job postings data collected from various websites in three distinct localities: USA, UAE, and Germany. The project encompasses web scraping to collect data, dataset standardization, translation of the German dataset, exploratory data analysis (EDA), and visualization using Power BI.

## Project Contributors

- **Eddie Nderitu**
- **Grace Musungu**
- **Ian Daniel Mathenge**
- **Alex Ndambuki**
- **Ngugi**

## Project Structure

- **Scraping:**
  - Data was scraped from job posting websites in the USA, UAE, and Germany.
  - Resulted in three datasets from the USA, two datasets from the UAE, and one dataset from Germany.

- **Translation:**
  - The German dataset required translation, which was achieved using Python.

- **EDA and Visualization:**
  - Power BI was used for exploratory data analysis and visualization.
  - A cumulative model was created by aggregating all datasets, standardizing columns, including:
    - City
    - Country
    - State
    - Date Posted
    - Industry
    - Job Description
    - Job ID
    - Job Title
    - Skill Requirements

## File Descriptions

- **Power BI Files:**
  - `Cumulative model.pbix`: Main Power BI file for analysis.
  - `Cumulative model.pbip`: Duplicate saved in .pbip format.

- **Python Translation Code:**
  - `Translation Code.ipynb`: Jupyter notebook containing the Python code for translating the German dataset.

## Key Findings

The Power BI dashboard provided insights into various aspects of data analyst job postings in the selected localities:

1. **Analyst Demographics by Country:**
   - Overview of the distribution of data analyst positions in the USA, UAE, and Germany.

2. **Analyst Jobs by Industry & Cities:**
   - Analysis of data analyst job distribution across different industries and cities.

3. **Data Analyst Postings by City:**
   - A breakdown of data analyst job postings in each city within the selected localities.

4. **Total Job Postings in Q3:**
   - Summarized data on the total number of job postings in the third quarter.

5. **Max Jobs by Industry:**
   - Identification of industries with the highest number of data analyst job postings.

## Usage

1. **Data Collection:**
   - Refer to the scraping scripts in the 'Scraping' folder for details on collecting data from job posting websites.

2. **Data Cleaning and Standardization:**
   - Use the 'DataCleaning.ipynb' notebook for cleaning and standardizing the datasets.

3. **Translation (if applicable):**
   - If dealing with non-English datasets, refer to the 'Translation Code.ipynb' notebook for guidance.

4. **EDA and Visualization:**
   - Open the Power BI file 'Cumulative model.pbix' to explore the visualizations and insights.

## Dependencies

- Python 3.x
  - Libraries: pandas, BeautifulSoup, requests, googletrans
- Power BI Desktop

## Acknowledgments

Special thanks to Eddie Nderitu, Grace Musungu, Ian Daniel Mathenge, Alex Ndambuki, and Ngugi for their valuable contributions to this analysis. Additionally, gratitude to all data sources that made this project possible.

Feel free to reach out for any clarifications or additional information. Happy analyzing!