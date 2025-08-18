# Data Processing Automation

## 🎯 Purpose

This repository is part of my continuous improvement as a Digital Analyst.
By automating repetitive reporting tasks, I can focus more on insights, strategy, and decision-making while ensuring data quality and consistency across analyses.

This repository contains Python scripts developed to **optimize and automate data processing tasks** related to subscription rebill tracking. The main goal is to improve efficiency in my daily work as a **Digital Analyst**, reducing manual steps and ensuring reproducible, clean, and structured outputs for further analysis and reporting.

## 🚀 Features

- **Automated Data Download**  
  - A function `descargar_rebill(year, month)` downloads rebill tracking data from a remote billing system.  
  - Files are automatically named with a timestamp and stored in the `/data/WR_Suivi_Rebill` folder.

- **Data Cleaning & Transformation** (`process_rebill`)  
  - Excludes test or unwanted email addresses (configurable filter).  
  - Extracts a unique identifier (`UID`) from the subscription contract ID.  
  - Creates a clean subset of partner contracts (`df_captured`) without duplicates.  
  - Adds a calculated column `Indicator`:
    - If the contract belongs to the selected partner → take the value of `isFirstRebillSuccess`.  
    - Otherwise → take the value of `Abo Unique`.  
  - Reorders columns into a consistent structure for easier analysis.

- **Flexibility**  
  - Supports filtering by one or multiple email substrings.  
  - Can work in strict mode (all expected columns must exist) or tolerant mode (skips missing ones).  
  - Results can be exported to `.csv` or `.xlsx` for reporting.