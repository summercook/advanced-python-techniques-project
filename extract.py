
"""Extract data on near-Earth objects and close approaches from CSV and JSON files.
The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.
The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.
The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach
def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.
    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(r'C:\Users\summe\advanced-python-techniques\data\neos.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            neo = NearEarthObject(**row) #designation = row['pdes'], name = row['name'], diameter = row['diameter'], hazardous = row['pha'])
            neos.append(neo)
    print(len(neos))
    return neos
            # TODO: Load NEO data from the given CSV file.


def load_approaches(cad_json_path = 'data /cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    with open('data\cad.json') as f:
        approaches = []
        json_data = json.load(f)
        for row in json_data['data']:
            row = dict(zip(json_data['fields'], row))
            approaches.append(CloseApproach(**row))
        print(len(approaches))
        return approaches
