def read_file(f, typ=str, sep='\n'):
	with open(f) as infile:
		return [typ(x) for x in infile.read().strip().split(sep)]
