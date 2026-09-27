# Text Statistics Analyzer using Python

A Python-based text analysis project developed using fundamental Python libraries to analyze and visualize text statistics.

## Project Overview

This project analyzes the text of *Alice's Adventures in Wonderland* and extracts useful statistical information about the document.

The project covers text cleaning, basic statistics, pattern extraction, numerical analysis, data analysis, and visualization.

## Features

- Load and clean text files
- Calculate basic text statistics
  - Character count
  - Word count
  - Sentence count
  - Average word length
  - Average sentence length
- Extract text patterns using Regular Expressions
  - Emails
  - Phone numbers
  - URLs
  - Dates
  - Currencies
  - Hashtags
  - Mentions
- Perform numerical analysis using NumPy
- Analyze word frequency using Pandas
- Generate visualizations using Matplotlib
- Export results as CSV and JSON files

## Technologies Used

- Python
- Regular Expressions (`re`)
- NumPy
- Pandas
- Matplotlib

## Dataset

The project uses *Alice's Adventures in Wonderland* by Lewis Carroll from Project Gutenberg.

## Project Structure

```text
python-based-text-statistic-analyzer/
│
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── PLOTS/
│
├── REPORT/
│
├── SRC/
│   ├── data_cleaning.py
│   ├── main.py
│   └── text_analyzer.py
│
└── .gitignore
