# 01_judgments_list.ipynb

## Overview

The `01_judgments_list.ipynb` notebook is designed to process and manage judicial judgment data. It reads raw judgment files, performs data cleaning, and extracts relevant information for further analysis. The notebook handles various data formats and structures, leveraging configuration settings defined in an external `config.yml` file.

## Key Features

- **Data Import and Configuration:** Utilises configuration settings to manage input and output directories, file extensions, and processing parameters.
- **Data Parsing:** Employs BeautifulSoup for parsing and extracting structured data from raw judgment files.
- **Data Cleaning:** Cleans and formats the extracted data to ensure consistency and readiness for analysis.
- **Output Generation:** Saves the processed data into specified directories for downstream tasks.

## Dependencies

- `pandas`
- `BeautifulSoup`
- `pathlib`
- `datetime`
- `config_reader` (local module)

## Usage

1. Ensure the `config.yml` file is correctly configured with paths to raw judgment files and output directories.
2. Run the notebook to process the judgment files.
3. The cleaned and processed data will be saved in the designated output folder.

## Configuration

The notebook relies on the `config.yml` file to specify:
- Input directory for raw judgments
- Output directory for cleaned data
- File extensions to process
- Specific markers for data extraction (e.g., `PQM` markers)

## Notes

- Make sure all dependencies are installed in your Python environment.
- Adjust the configuration file as needed to match your dataset and directory structure.