import argparse

parser = argparse.ArgumentParser(description='Convert types of data')
parser.add_argument('infile')
parser.add_argument('outfile')
parser.add_argument('-i', '--input-format')
parser.add_argument('-o', '--output-format')
parser.add_argument(
    '-p', '--pretty-print', action='store_true',
    help='Pretty print if available')

args = parser.parse_args()
print(args)
