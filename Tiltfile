# -*- mode: Python -*-

# Tilt is a dev tool that speeds up your inner loop.
# I use this Tiltfile to auto-run the Python file I'm
# currently iterating on, whenever I save.
# To learn more about Tilt: https://tilt.dev/

py_files = [f.split('/')[-1] for f in listdir('.') if f.endswith('.py')]
for f in py_files:
	basename = f.split('.')[0]
	local_resource(basename, 'python {}'.format(f), deps=[f])