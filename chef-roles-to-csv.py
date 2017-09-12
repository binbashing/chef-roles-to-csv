from commands import getoutput
import json
import unicodecsv as csv
import argparse


# Parse arguements
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile', '-o', help='Output File', required=True)
args = parser.parse_args()
output_csv = (args.outfile)


# Initialize master list
master_list = []


# Function to build header row
def get_keys(input_list):
    all_keys = []
    for dictionary in input_list:
        dict_keys = dictionary.keys()
        for key in dict_keys:
            all_keys.append(key)
    all_keys = list(set(all_keys))
    all_keys = sorted(all_keys)
    all_keys.remove('node_name')
    all_keys.insert(0, 'node_name')
    return all_keys


# Write node role data to CSV
def all_to_csv(input_list, out_file):
    keys = get_keys(input_list)
    with open(output_csv, 'wb') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(input_list)


# Function to return role data for a given node
def get_roles(node):
    node_dict = {}
    node_dict.update({'node_name': node})
    text = getoutput('knife node show -l --format=json %s' % (node))
    json_output = json.loads(text)
    for role in json_output['automatic']['roles']:
        node_dict.update({role: 'X'})
    return node_dict
    master_list.append(node_dict)


# Function to return all nodes in Chef
def get_all_nodes():
    text = getoutput('knife node list --format=json')
    json_output = json.loads(text)
    return json_output


# Main Function
all_nodes = get_all_nodes()
for node in all_nodes:
    node_roles = get_roles(node)
    master_list.append(node_roles)
all_to_csv(master_list, output_csv)
