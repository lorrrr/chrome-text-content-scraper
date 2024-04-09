#!/bin/bash

# Directory where the HTML files will be saved
output_dir="html_snapshots"
mkdir -p "$output_dir"

# File containing the list of URLs
urls_file="url.txt"

# Read each line in urls.txt as a URL
while IFS= read -r url; do
  if [[ ! -z "$url" ]]; then
    echo "Processing $url"
    # Create a filename from the URL by replacing slashes with underscores
    filename=$(echo "$url" | sed 's|https\?://||; s|/|_|g').html
    # Path for the output HTML file
    output_path="$output_dir/$filename"
    # Use headless Chrome to get the HTML content and save it to the file
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --dump-dom "$url" > "$output_path"
    echo "Saved to $output_path"
  fi
done < "$urls_file"
