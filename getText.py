import os
from bs4 import BeautifulSoup

html_dir = 'html_snapshots'  
text_dir = 'text_output' 
os.makedirs(text_dir, exist_ok=True)  # Ensure the text output directory exists
print("hi")
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        # Construct full paths
        html_path = os.path.join(html_dir, filename)
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_path = os.path.join(text_dir, text_filename)

        # Open and parse the HTML file
        with open(html_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)

        # Save the extracted text
        with open(text_path, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Extracted text from {filename} to {text_filename}")
