import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Add columns to dataframe A using B's information for annotation or other purpose")
parser.add_argument("-A", help="csv file A", dest="A", required=True)
parser.add_argument("-B", help="csv file B", dest="B", required=True)
parser.add_argument("-B-col", help="add this column in B to A", dest="colB", required=True)
parser.add_argument("-o", help="output file", dest="output", required=False)
parser.add_argument("-A-sep", help="column separator for A", dest="sepA", required=False, default=",")
parser.add_argument("-B-sep", help="column separator for B", dest="sepB", required=False, default=",")
parser.add_argument("-A-key", help="key column in A", dest="keyA", required=False, default=0)
parser.add_argument("-B-key", help="key column in B", dest="keyB", required=False, default=0)
parser.add_argument("-A-wheader", help="A has header row", dest="headerA", required=False, action="store_true", default=False)
parser.add_argument("-B-wheader", help="B has header row", dest="headerB", required=False, action="store_true", default=False)

args = parser.parse_args()

headerA = 0
headerB = 0
if (args.headerA):
  headerA = 1
if (args.headerB):
  headerB = 1 

keyA = args.keyA 
keyB = args.keyB

pdA = pd.from_csv(args.A, sep=args.sepA, header=headerA)
pdB = pd.from_csv(args.B, sep=args.sepB, header=headerB)[[keyB, args.colB]]

pdResult = pdA.merge(pdB, left_on=keyA, right_on = keyB)

print(pdResult)
