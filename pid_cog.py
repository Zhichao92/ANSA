"""
This script will print the pid name and its cog. It will also write it to csv file.
"""
import os
import ansa
from ansa import constants
from ansa import base
from ansa import utils
deck = constants.RADTHERM

def main():
	pids = base.CollectEntities(deck, None, "SHELL_PART")
	m = utils.SelectSaveFile("*.csv")
	with open(m[0], 'w') as f:
		for pid in pids:
			cog = base.Cog(pid)
			print(pid._name+','+str(cog[0])+','+str(cog[1])+','+str(cog[2]))
			f.write(pid._name+','+str(cog[0])+','+str(cog[1])+','+str(cog[2])+'\n')


if __name__ == '__main__':
	main()
