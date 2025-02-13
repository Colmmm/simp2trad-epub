#!/usr/bin/env python3
import argparse
import os
import opencc
from ebooklib import epub

def convert_epub(input_file, output_file):
    # Initialize the converter for Simplified-to-Traditional conversion
    converter = opencc.OpenCC('s2t.json')
    
    try:
        book = epub.read_epub(input_file)
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        exit(1)
    
    # Iterate over items in the EPUB
    for item in book.get_items():
        # Check if the item is an HTML document
        if isinstance(item, epub.EpubHtml):
            try:
                # Decode the content assuming UTF-8 encoding
                content = item.get_content().decode('utf-8')
            except Exception as e:
                print(f"Error decoding content for item {item.get_id()}: {e}")
                continue
            
            # Convert the content using OpenCC
            converted_content = converter.convert(content)
            # Set the converted content back to the item
            item.set_content(converted_content.encode('utf-8'))
    
    try:
        epub.write_epub(output_file, book)
    except Exception as e:
        print(f"Error writing EPUB file: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Convert an EPUB's content from Simplified to Traditional Chinese."
    )
    parser.add_argument("input_file", help="Path to the input EPUB file.")
    args = parser.parse_args()

    input_file = args.input_file
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        exit(1)

    # Create output filename by appending '_traditional' before the file extension
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_traditional{ext}"

    convert_epub(input_file, output_file)
    print(f"Conversion complete. Converted EPUB saved as: {output_file}")

if __name__ == "__main__":
    main()

