from __future__ import print_function

from argparse import ArgumentParser
from io import open
from sys import stdout

from .scte_55_1_address import mac_to_ua, ua_to_mac

# Accept arguments from the command line
parser = ArgumentParser(
    prog='python -m terminal_address',
    description=(
        'Supply a file with MAC or Unit Addresses (one per line) using '
        '--mac-file or --ua-file . The program will produce a file with '
        'the original address and the converted address (separated by a '
        'comma).'
    )
)
parser.add_argument(
    '--mac-file', help='Specify the path to a file with MAC addresses'
)
parser.add_argument(
    '--ua-file', help='Specify the path to a file with unit addresses'
)
parser.add_argument(
    '--output-file', help='Specify the path of the output file'
)
args = parser.parse_args()


def main(converter, infile_path, outfile):
    with open(infile_path, 'rt') as infile:
        for line in infile:
            addr = line.strip()
            converted = converter(addr)
            print(addr, converted, sep=',', file=outfile)


if __name__ == "__main__":
    if (args.mac_file is None) and (args.ua_file is None):
        raise RuntimeError(
            'No input file specified (need --mac-file or --ua-file)'
        )
    infile_path = args.mac_file if args.mac_file else args.ua_file
    converter = mac_to_ua if args.mac_file else ua_to_mac
    outfile = open(args.output_path, 'wt') if args.output_file else stdout
    try:
        main(converter, infile_path, outfile)
    finally:
        outfile.close()
