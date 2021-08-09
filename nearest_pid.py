# This script will save the point name and its nearest pid user attribute to csv file
import os
import ansa
from ansa import base
from ansa import constants
from ansa import utils
deck = constants.RADTHERM

def nearest_pid():
	file_name = utils.SelectSaveFile("*.csv")
	points = base.CollectEntities(deck, None, 'POINT')
	pids = base.CollectEntities(deck, None, '__PROPERTIES__')
	vals = ('X', 'Y', 'Z')
	pid_val = ('PID',)
	with open(file_name[0], 'w') as fn:
		for i in points:
			ret = base.GetEntityCardValues(deck, i, vals)
			coords = [(ret['X'], ret['Y'], ret['Z'])]
			shell_list = base.NearestShell(coordinates= coords, tolerance = 5, search_entities = pids)			
			nearest_pid_id = base.GetEntityCardValues(deck, shell_list[0], pid_val)		
			pid = base.GetEntity(deck, '__PROPERTIES__', nearest_pid_id['PID'])		
			fn.write(i._name+', '+base.GetEntityCardValues(deck, pid, ('User/fluent_name',))['User/fluent_name']+'\n')
	print("\n CSV file saved \n")

if __name__ == '__main__':
	nearest_pid()
