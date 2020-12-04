def read_file(f):
	with open(f) as infile:
		return infile.read().strip().split('\n')