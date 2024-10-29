import pdfplumber
import re
from datetime import datetime

def extract_pdf_data(pdf_path):
    extracted_data = []
    current_state = "Unknown State"
    current_date = "Unknown Date"

    with pdfplumber.open(pdf_path) as pdf:
        # Process all pages in the PDF
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]

            # Extract text to find state and date
            text = page.extract_text()

            # ignoring the table in hindi content
            if re.search(r'[\u0900-\u097F]', text):
                continue  

            # Extract State Name
            state_match = re.search(r'\b(\w+)\s+State\b', text)
            if state_match:
                current_state = state_match.group(1).strip()
                #print(f"Extracted State Name: {current_state}")

            # Extract Date
            date_match = re.search(r'Date:\s*(\d{2}-\d{2}-\d{4})', text)
            if date_match:
                # Convert date format from DD-MM-YYYY to YYYY-MM-DD
                original_date = date_match.group(1)
                current_date = datetime.strptime(original_date, '%d-%m-%Y').strftime('%Y-%m-%d')

            # Extract tables from the page
            tables = page.extract_tables()
            for table in tables:
                # Skip header row
                for row in table[1:]:  # Starting from the second row
                    if len(row) >= 6:  # Ensuring the columns
                        work_item = row[3].strip() if row[3] and isinstance(row[3], str) else None
                        cin = row[4].strip() if row[4] and isinstance(row[4], str) else None
                        company_name = row[5].strip() if row[5] and isinstance(row[5], str) else None

                        # Ensuring all parts are valid before appending
                        if work_item and cin and company_name:
                            extracted_data.append((current_state, current_date, work_item, cin, company_name))
                            print(f"Added Company Data: {current_state}, {current_date}, {work_item}, {cin}, {company_name}")

    # Print final extracted data
    #print("Final Extracted Data:", extracted_data)

    return extracted_data