import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_available_filename(output_file):
    # Check if the file already exists
    if os.path.isfile(output_file):
        # Split the filename and extension
        name, ext = os.path.splitext(output_file)
        # Initialize a counter
        counter = 1
        # Keep incrementing the counter until a filename is available
        while os.path.isfile(f"{name}_{counter}{ext}"):
            counter += 1
        return f"{name}_{counter}{ext}"
    else:
        return output_file

url = 'https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/punjab-kings-vs-delhi-capitals-2nd-match-1422120/full-scorecard'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
tables = soup.find_all('table', class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table")

# Initialize an empty DataFrame
df = pd.DataFrame()

for x in range(0, 2):  # Loop runs 2 times
    table_data = tables[x]

    # Extract headers
    table_title = table_data.find('tr')
    headers = [th.getText().strip() for th in table_title.find_all('th')]

    # Initialize a temporary DataFrame with headers
    temp_df = pd.DataFrame(columns=headers)

    # Extract player data
    players_data = table_data.find_all('tr')[1:]
    player_runs = []

    for player in players_data:
        td_elements = player.find_all('td')
        player_data = [td.get_text().strip() for td in td_elements]
        if player_data:
            player_runs.append(player_data)

    for data in player_runs:
        while len(data) < 8:
            data.append('')

        new_row = pd.DataFrame([{
            'BATTING': data[0],
            '': data[1],
            'R': data[2],
            'B': data[3],
            'M': data[4],
            '4s': data[5],
            '6s': data[6],
            'SR': data[7]
        }])
        temp_df = pd.concat([temp_df, new_row], ignore_index=True)
    
    # Append the temporary DataFrame to the main DataFrame
    df = pd.concat([df, temp_df], ignore_index=True)

# Excel file path
output_file = '/Users/gangasingh/Downloads/Cricket/Analysis.xlsx'

# Get an available filename
output_file = get_available_filename(output_file)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)
print(f'DataFrame saved to {output_file}')

# Drop all rows from the DataFrame
df.drop(df.index, inplace=True)

# Display the DataFrame after dropping all rows
df
