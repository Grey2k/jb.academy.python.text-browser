import argparse
import os

from engine import Browser

# Parser
parser = argparse.ArgumentParser()

parser.add_argument('dir', type=str, default=os.getcwd())
args = parser.parse_args()

# write your code here
browser = Browser(args.dir)

browser.run()
