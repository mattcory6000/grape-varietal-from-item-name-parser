# Wine Varietal Parser

This Python script parses wine names and identifies grape varietals based on a provided list. It processes a CSV of wine names from the AOC Distributors portfolio and matches grape varietals from another CSV list. The output is a new CSV file containing wine IDs, wine names, and the identified varietals.

## Files

- `wine_names.csv`: Contains wine IDs and full wine names.
- `varietals.csv`: Contains a list of grape varietals.
- `wine_varietal_parser.py`: The main script that parses wine names and identifies varietals.
- `wine_names_with_varietals.csv`: Output file with the original wine data and the identified varietals.

## Setup

### Requirements

- Python 3.x
- Pandas library

To install Pandas, run:

```bash
pip install pandas
