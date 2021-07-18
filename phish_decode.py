#!/usr/bin/python3

import base64
import argparse
import re

def getArgs():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="Input file")
    ap.add_argument("-r", "--rounds", required=False, help="Maximum rounds to try", default=100)
    return vars(ap.parse_args())

def extract_b64(full_string):
    pattern_match = re.search("atob\(\'(.*)\'", full_string)
    return pattern_match.group(1)

def decode_b64(enc_string):
    enc_bytes = enc_string.encode('ascii')
    dec_bytes = base64.b64decode(enc_bytes)
    return dec_bytes.decode('ascii')

def main():

    # Get command line arguments
    my_args = {}
    my_args = getArgs()
    malfile = my_args['file']
    max_rounds = int(my_args['rounds'])

    # Get file contents
    malfile_contents = open(malfile, "r")
    full_string = malfile_contents.read()

    while(max_rounds >= 0):

        # Extract base64 encoded string
        enc_string = extract_b64(full_string)

        # Decode base64 string
        dec_string = decode_b64(enc_string)

        # Decode embedded JS
        if(re.match("\<\!DOCTYPE html\>", dec_string)):
            enc_string = extract_b64(dec_string)
            last_string = decode_b64(enc_string)
            break;

        # Prepare for next round
        full_string = dec_string
        max_rounds-=1

    # Print result, substituting the decoded JS
    print(re.sub("atob.*=\'\)",last_string,dec_string))


if __name__ == "__main__":
    main()
