# Analyzing Sakai Development Project Email Archive Using Python

---
## Introduction
This project explores the Sakai Development Project's email archive data collected from gmane.org. The goal of this project is to derive insights and visualize the data using Python and D3 JavaScript libraries.

## Overview
In this project, I scraped, pre-cleaned, and stored the email data in a local database using Python's SQLite library. Then, I conducted further data cleaning and analysis to reveal important insights such as the top contributors, organizations, and frequently used words in email subjects.

To present my findings, I utilized the D3 JavaScript library to create dynamic visualizations, including word frequency plots and time-series line plots. This project showcases my skills in data scraping, cleaning, analysis, and visualization.

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine.

### Data
The email data was collected from the Sakai Development Project's email archive on gmane.org. To avoid overloading the gmane.org server, I used a copy of the messages from http://mbox.dr-chuck.net/.

## Results

 - Data Summary

![gbasic_data summary](https://github.com/Gopal564/Dynamic_Email_Analysis/assets/87975144/9f4da91a-99db-4dbd-947d-cc4767ac7198)
 
 - Gline Plot

![gline_visula](https://github.com/Gopal564/Dynamic_Email_Analysis/assets/87975144/75b1c119-f08a-4886-ab38-386d7f97efcc)

 - Gline Year Plot

![gline_year](https://github.com/Gopal564/Dynamic_Email_Analysis/assets/87975144/eed486f2-71a1-479b-8d9c-035af8626d38)

 - Word Cloud

![word_cloud](https://github.com/Gopal564/Dynamic_Email_Analysis/assets/87975144/2e1399d9-e5d1-47d0-9c1d-e819cbf22ea4)

## Conclusion
By analyzing the Sakai Development Project's email archive, I gained insights into the top contributors, organizations, and frequently used words in email subjects. These insights were visualized using D3 JavaScript library to create dynamic visualizations, including word frequency plots and time-series line plots. This project showcases my skills in data scraping, cleaning, analysis, and visualization and is a valuable addition to my portfolio.

### File Description
#### gmane.py
A Python script that retrieves and parses email data from a website and stores it in an SQLite database.
#### gmodel.py
A Python script used for cleaning email data, extracting information, and preparing it for further analysis.
#### ghistanalysis.py
A Python script that computes basic histogram data on the emails in the database and prints out top email list participants and organizations.
#### gword.py, gyear.py, gline.py
Scripts that generate JavaScript files for displaying word cloud and time-series line plot visualizations in web pages.

