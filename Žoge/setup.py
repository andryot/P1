from cx_Freeze import setup, Executable
setup(name='test',
	version='1.1',
	description='Testing',
	executables = [Executable("za9.py")])