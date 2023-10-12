import sys
import platform
import os
import subprocess


modules = []


if platform.system().lower() == "windows":
	clear = lambda:os.system("cls")
else:
	clear= lambda:os.system("clear")


def str_manage(stdin:str) -> str:
	"""Removes all useless chars
	"""
	stdin = stdin.replace("b", "").replace("\\n", " ").replace("=", " ").replace("'", "").split()
	
	for d in stdin:
		if stdin.index(d) % 2 == 0:
			yield d


def manage_file(f) -> list:
	"""Loding file function if user choose to update modules from requirements.txt file
	"""
	lst:list = []
	with open(f, "r") as file_:
		for row in file_:
			lst.append(row.strip())

	for i in lst:
		yield i.replace("=", " ").split()[0]
			


def manage_pip_out() -> list:
	"""Gets all modules from pip3 freeze output
	"""
	cmdout = subprocess.check_output("pip3 freeze", shell=True)
	cmdout = str(cmdout)
	cmdout = cmdout.replace("b", "").replace("\\n", " ").replace("=", " ").replace("'", "").split()
	
	lst:list = []
	
	for data in cmdout:
		if cmdout.index(data) % 2 == 0:
			lst.append(data)
			
	return lst


def upgrade_from_list(lst:list) -> None:
	"""Updates from global module list
	"""
	for module in lst:
		os.system("pip3 install --upgrade {}".format(module))

if __name__ == "__main__":
	if len(sys.argv) == 2:

		if sys.argv[1] != "--no-file":
			for module in manage_file(sys.argv[1]):
				modules.append(module)	
			
		else:
			modules = manage_pip_out()

		upgrade_from_list(modules)
	
	else:
		print("[*]: Use -> python3 update.py\n::OR::\n[*]: python3 update.py --no-file")

