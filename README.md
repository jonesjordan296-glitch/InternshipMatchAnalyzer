# InternshipMatchAnalyzer

A Python-based internship recommendation tool that helps Computer Science students identify internship opportunities based on their technical skills.

## Project Overview

InternshipMatchAnalyzer compares a student's technical skills against internship requirements and calculates compatibility percentages.

The goal is to help students identify opportunities that align with their current abilities and understand which technical skills they should develop.

## Problem Statement

Finding internships can be challenging for students who are still developing their programming skills.

InternshipMatchAnalyzer provides a simple way to compare technical abilities against internship requirements using a rule-based matching algorithm.

## Technologies Used

- Python
- Pandas
- CSV
- Matplotlib (Exploratory Data Analysis)

## Current Features

- Reads internship information from a CSV dataset.
- Processes 15 simulated internship listings.
- Compares student skills against internship requirements.
- Calculates internship compatibility percentages.
- Displays matching results in the terminal.
- Includes a separate exploratory data analysis script.

## How It Works

1. Internship data is loaded using Pandas.
2. A student skill profile is defined.
3. The program compares student skills against each internship's requirements.
4. A compatibility percentage is calculated.
5. Results are displayed in the terminal.

The compatibility scores represent the percentage of listed skills matched, not the probability of receiving an internship offer.

## Example Output

    Ex Tech match percentages: 67 %
    Nova Tech match percentages: 67 %
    Pioneer Research match percentages: 67 %
    NextGen Automation match percentages: 100 %

## Installation

1. Download or clone this repository.
2. Install the required Python libraries:

    pip install pandas matplotlib

3. Run the application:

    python main.py

4. To run the exploratory data analysis:

    python eda.py

## Future Improvements

- Develop an interactive web application using Streamlit.
- Allow users to enter their own technical skills.
- Display internship recommendations in ranked order.
- Identify missing skills for each internship.
- Expand the internship dataset.
- Incorporate real internship opportunities.

## Project Status

In Development — Python prototype completed.

## Developer

Computer Science student at Winston-Salem State University interested in software engineering, artificial intelligence, and data science.
