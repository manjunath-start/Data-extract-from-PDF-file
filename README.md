# PDF Data Extraction

This project extracts data from PDF files, specifically targeting tables that contain company information, along with state names and dates. The extracted data can then be used for further processing or stored in a database.

## Features
- Extracts company data including Work Item, CIN, and Company Name.
- Identifies and extracts the current state and date from the PDF.
- Handles multi-page PDFs and ignore tables with Hindi content.
- Converts date formats from `DD-MM-YYYY` to `YYYY-MM-DD` for database compatibility.

## Requirements
To run this project, Please install the following libraries

- **pdfplumber**: For extracting text and tables from PDFs.
- **datetime**: To handle date formatting.

## Then requirements.txt file
   pip install -r requirements.txt
