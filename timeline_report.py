
import argparse
import json
from datetime import datetime
from tqdm import tqdm
from geopy.geocoders import Photon

def getCountry(lat, long):
    geolocator = Photon(user_agent="measurements")
    try:
        country = geolocator.reverse(str(lat)+","+str(long)).raw['properties']['country']
    except:
        return 'Unknown'
    else:
        return country
    
def convertTimestamp(timestamp):
    format_string = '%Y-%m-%dT%H:%M:%S.%fZ' if '.' in timestamp else '%Y-%m-%dT%H:%M:%SZ'
    return datetime.strptime(timestamp, format_string)

def convertCoords(coord):
    return coord / 1e7

def main():
    parser = argparse.ArgumentParser(description='Process some variables from the command line.')

    # Define command-line arguments
    parser.add_argument('--path', type=str, help='Path to the Google Takeout timeline file. e.g. Takeout/Sijantihistoria/Records.json')
    parser.add_argument('--step_hours', type=int, help='Minimum houts between two location checks, recommended: 24')
    parser.add_argument('--start_year', type=str, help='Start year')
    parser.add_argument('--end_year', type=str, help='End year')


    # Parse command-line arguments
    args = parser.parse_args()

    # Access the variables
    path = args.path
    step_hours = args.step_hours
    start_year = int(args.start_year)
    end_year = int(args.end_year)

    # Define step in seconds
    step = step_hours * 60 * 60

    print(f"Converting raw timeline data from year {start_year} to year {end_year} with step {step_hours} hours.\nThis may take some time.")

    with open(path) as f:
        data = json.load(f)

    data_timeline = []
    prev_timestamp = convertTimestamp('1970-02-09T10:30:46.085Z')
    for entry in tqdm(data['locations']):
        timestamp = convertTimestamp(entry['timestamp'])
        # Pick a timestamp once a step
        if ((timestamp - prev_timestamp).total_seconds() >= step) and (start_year <= timestamp.year <= end_year):
            country = getCountry(convertCoords(entry['latitudeE7']), convertCoords(entry['longitudeE7']))
            if country != 'Unknown':
                prev_timestamp = timestamp                             
                data_timeline.append({'lat': convertCoords(entry['latitudeE7']), 'long': convertCoords(entry['longitudeE7']), 'country': country, 'timestamp': entry['timestamp']})

    
    trip_start = data_timeline[0]
    prev_entry = data_timeline[0]
    trips = []
    for entry in data_timeline:
        if entry['country'] != trip_start['country']:
            start = convertTimestamp(trip_start['timestamp'])
            end = convertTimestamp(prev_entry['timestamp'])
            formatted_start = start.strftime('%d/%m/%Y')
            formatted_end = end.strftime('%d/%m/%Y')
            country = prev_entry['country']
            formatted_string = f'{country}: {formatted_start} -- {formatted_end} ({(end - start).days} days)'

            trips.append({
                'destination': trip_start['country'],
                'length_days': (end - start).days,
                'start': start,
                'end': end,
                'description': formatted_string
            })
            trip_start = entry
        prev_entry = entry

    print("Saving output to 'output_timeline.json'")
    file_path = 'output_timeline.json'
    with open(file_path, 'w') as output_file:
        for index, trip in enumerate(trips, start=1):
            output_file.write(f"{index}. {trip['destination']}\n")
            print(f"{index}. {trip['destination']}\n")

if __name__ == "__main__":
    main()