import os,sys,argparse

parser = argparse.ArgumentParser(description="This script is used in order to check files extract from blueliv and detect which are new")
parser.add_argument('-f', '--folder', help="Set check mode into folder instead of file", action="store_true")
parser.add_argument('-i', '--input', help="Set input file or folder (that must contains only .csv files) we want to check", required=True)
parser.add_argument('-o', '--output', help="Set global output file where new input data will be added near data collected in the past", required=True)
parser.add_argument('-n', '--new-data', help="Set ouput file where new input data will be added", required=True)
args = parser.parse_args()


def check_data(data, global_data_file):
	global_data_list = open(global_data_file, "r")
	is_new_data = True
	for global_data in global_data_list:
		if (data[1] in global_data) and (data[3] in global_data):
			is_new_data = False
	global_data_list.close()
	return is_new_data

def checker(args):
	temp_file = open("/tmp/checker_temp_data", "w")
	leak_list = open(args.input, "r")
	for leak in leak_list:
		data = leak.split(",")
		is_new = check_data(data, args.output)
		if is_new:
			temp_file.write(leak)
	leak_list.close()
	temp_file.close()
	os.system('cat /tmp/checker_temp_data > {}'.format(args.new_data))
	os.system('cat /tmp/checker_temp_data >> {}'.format(args.output))
	os.system('rm /tmp/checker_temp_data')

def checker_folder(args):
	print(" ")
	#TODO

if args.folder:
	checker_folder(args)
else:
	checker(args)

os.system('date')
print("DONE")
