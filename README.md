# Google Takeout Timeline Analyzer

This Python script analyzes location data from the Google Takeout timeline file and identifies trips with their start and end dates, destination, and duration.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install package_name`):
  - tqdm
  - geopy

Install the dependencies:

## Usage
```bash
pip3 install tqdm geopy
```
Run the script from the command line with the following options:

```bash
python3 timeline_report.py --path <path_to_timeline_file> --step_hours <minimum_hours_between_location_checks> --start_year <start_year> --end_year <end_year>
```
- path: Path to the Google Takeout timeline file (e.g., './Takeout/Sijaintihistoria/Records.json').
- step_hours: Minimum hours between two location checks (recommended: 24).
- start_year: Start year for analyzing location data.
- end_year: End year for analyzing location data.

For example:
```bash
python3 timeline_report.py --path './Takeout/Sijaintihistoria/Records.json' --step_hours 24 --start_year 2023 --end_year 2024
```

## Output

The script generates an output_timeline.json file containing information about identified trips, including the destination, length in days, start and end dates, and a description, as well as outputs the result in the terminal.

## Additional Notes

The script utilizes the geopy library to reverse geocode latitude and longitude coordinates into country names.
The output_timeline.json file contains details about each identified trip, which can be further processed or used for analysis.
Feel free to customize the script according to your specific requirements.