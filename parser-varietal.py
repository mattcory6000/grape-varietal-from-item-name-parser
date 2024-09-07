import pandas as pd
import re

# Load the wine_names and varietals CSV files
wine_names_file = 'wine_names.csv'
varietals_file = 'varietals.csv'

wine_names_df = pd.read_csv(wine_names_file)
varietals_df = pd.read_csv(varietals_file)

# Prepare the list of grape varietals
varietals = varietals_df['Name'].tolist()


def find_varietals(wine_name):
    found_varietals = []

    # Normalize the wine name (lowercase for better matching)
    wine_name_lower = wine_name.lower()

    # Handle special case for Montepulciano
    if "di montepulciano" in wine_name_lower:
        # Do not include Montepulciano as it's the region here
        pass
    elif "montepulciano" in wine_name_lower:
        found_varietals.append("Montepulciano")

    # Search for any other varietals in the wine name
    for varietal in varietals:
        varietal_lower = varietal.lower()
        if varietal_lower in wine_name_lower and varietal not in found_varietals:
            found_varietals.append(varietal)

    return ", ".join(found_varietals) if found_varietals else None


# Apply the find_varietals function to each wine name
wine_names_df['Varietals'] = wine_names_df['Name'].apply(find_varietals)

# Save the result to a new CSV file
output_file = 'wine_names_with_varietals.csv'
wine_names_df.to_csv(output_file, index=False)

print(f"Processed file saved as {output_file}")
