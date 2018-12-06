import os, sys, argparse
import pandas as pd

def converter_folder(args):
	for file in os.listdir(args.input):
		finput = "{}{}".format(args.input,file)
		data_xls = pd.read_excel(finput, usecols="B,C,D,F,H,I")
		fname, fext = file.split(".")
		foutput = "{}{}.csv".format(args.output,fname)
		data_xls.to_csv(foutput, encoding='utf-8', index=False)

def converter(args):
	data_xls = pd.read_excel(args.input, usecols="B,C,D,F,H,I")
	data_xls.to_csv(args.output, encoding='utf-8', index=False)

parser = argparse.ArgumentParser(description="This script is used in order to convert xlsx files in csv files")
parser.add_argument('-f', '--folder', help="Set converter mode into folder instead of file", action="store_true")
parser.add_argument('-i', '--input', help="Set input file or folder that must contains only .xlsx files", required=True)
parser.add_argument('-o', '--output', help="Set output file or folder that will contains .csv files", required=True)
args = parser.parse_args()


if args.folder:
	converter_folder(args)
else:
	converter(args)

print("DONE")
