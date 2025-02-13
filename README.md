# simp2trad-epub

A simple Python tool to convert an EPUB's content from Simplified Chinese to Traditional Chinese using `opencc` and `ebooklib`.

## Features

- Converts text content within EPUB files from Simplified to Traditional Chinese.
- Saves the converted EPUB with `_traditional` appended to the original filename.

## Requirements

- Python 3.12 (or later)
- [opencc](https://pypi.org/project/opencc/)
- [EbookLib](https://pypi.org/project/EbookLib/)

## Setup

### 1. Clone or Download the Repository

Clone this repository or download the script files to your local machine.

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies locally.

Open a terminal in the project directory and run:

```bash
python3.12 -m venv venv
```

### 3. Activate the Virtual Environment

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```powershell
  .\venv\Scripts\activate
  ```

### 4. Install Required Packages

Install the necessary packages using pip. If you have a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, create one with the following content:

```
opencc
EbookLib
```

Then run the above command to install dependencies.

## Usage

To convert an EPUB file, run the script with the path to your EPUB file as an argument:

```bash
python simp2trad_epub.py path/to/your/book.epub
```

This will generate a new EPUB file in the same directory with `_traditional` appended to the original filename (e.g., `book_traditional.epub`).

## Troubleshooting

### EPUB Warnings
You might see some warnings from `ebooklib` regarding future changes. These warnings do not affect the conversion process.

### Encoding Issues
The script assumes the text content in the EPUB is UTF-8 encoded. If you encounter decoding errors, ensure your EPUB's HTML files are in UTF-8.


