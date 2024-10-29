from scripts.pdf_extractor import extract_pdf_data
from scripts.database_handler import create_table, insert_into_database

# Path to the PDF file
pdf_path = 'data/PDF-file.pdf'

# Extract data from the PDF
extracted_data = extract_pdf_data(pdf_path)

# Print the extracted data to verify
#print("Extracted Data:", extracted_data)

# Create the table in the database
create_table()

# Insert the extracted data into the SQL database
if extracted_data:
    insert_into_database(extracted_data)
    print("Data inserted successfully into the SQL table.")
else:
    print("No data to insert.")

