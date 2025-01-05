# Excel Concatenator

A Python script designed to simplify the process of combining multiple Excel or CSV files into a single dataset. This tool reads files from a specified folder, concatenates the data, and generates a unified dataset as output. 

## Features

- **Read Multiple Files**: Automatically detects and processes `.csv` files from a specified directory.
- **Data Concatenation**: Combines data from multiple files into one seamless dataset.
- **Error Handling**: Ensures invalid or missing files are flagged appropriately.
- **Output Generation**: Saves the concatenated dataset as a new file in the specified location.

## Usage

1. Place the `.csv` files you want to combine into the same folder.
2. Update the script to point to the folder containing your files.
3. Run the script in your preferred Python environment.
4. The combined dataset will be saved in the same directory as `Combined_Dataset.csv`.

## Requirements

- Python 3.x
- Pandas Library (`pip install pandas`)

## How to Run

1. Clone or download this repository.
2. Ensure your `.csv` files are in a folder you can reference.
3. Run the script:
   ```bash
   python excel_concatenator.py
