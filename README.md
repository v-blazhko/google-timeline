# Google Takeout Timeline Analyzer

This Python script analyzes location data from the Google Takeout timeline file and identifies trips with their start and end dates, destination, and duration.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install package_name`):
  - tqdm
  - geopy

## Installing the dependencies

```bash
pip3 install tqdm geopy
```

## How to download Google Timeline data
1. Visit the Google Takeout website: [Google Takeout](https://takeout.google.com/).
2. Log in with your Google account.
3. Scroll down to find "Location History" or "Location Services" in the list of available services.
4. Select "Deselect All" and then enable only the "Location History" or "Location Services" option.
5. Scroll to the bottom and click on "Next."
6. Choose your preferred export settings, including the file format and delivery method.
7. Click on "Create export." Google will prepare your data, and you'll receive a notification once it's ready.
8. Download the ZIP file containing your location history.
9. Extract the contents and locate the JSON file (e.g., `'./Takeout/Sijantihistoria/Records.json'`) for use with the script. You can move the script to the same folded with this script for simplicity.

## Usage

Run the script from the command line with the following options:

```bash
python3 timeline_report.py --path <path_to_timeline_file> --step_hours <minimum_hours_between_location_checks> --start_year <start_year> --end_year <end_year>
```
- path: Path to the Google Takeout timeline JSON file (e.g., `'./Takeout/Sijantihistoria/Records.json'`).
- step_hours: Minimum hours between two location checks (recommended: 24).
- start_year: Start year for analyzing location data.
- end_year: End year for analyzing location data.

For example:
```bash
python3 timeline_report.py --path './Takeout/Sijantihistoria/Records.json' --step_hours 24 --start_year 2023 --end_year 2024
```

## Output

The script generates an `output_timeline.txt` file containing information about identified trips, including the destination, length in days, start and end dates, and a description, as well as outputs the result in the terminal.

Example script output in the command line:
```
1. Suomi: 01/01/2015 -- 04/02/2018 (34 days)
2. Eesti: 11/12/2021 -- 13/12/2021 (2 days)
...
99. Ísland: 01/08/2022 -- 27/08/2022 (26 days)
```
## Additional notes

The script utilizes the `geopy` library to reverse geocode latitude and longitude coordinates into country names.
The `output_timeline.txt` file contains details about each identified trip, and `output_raw.json` contains raw timeline data, which can be further processed or used for analysis.
Feel free to customize the script according to your specific requirements.