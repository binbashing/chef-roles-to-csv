# chef-roles-to-csv

## Description
A simple python script to inventory what Chef roles are applied to what nodes and exporting to CSV

## Dependencies
Dependencies include:

- commands
- json
- unicodecsv
- argparse

These should be available via pip/easy_install.

A configured [knife](https://docs.chef.io/config_rb_knife.html) command 
## Usage
```
python chef-roles-to-csv.py -h
usage: chef-roles-to-csv.py [-h] -o OUTFILE

optional arguments:
  -h, --help                     show this help message and exit
  -o OUTFILE, --outfile OUTFILE  Output File
```
