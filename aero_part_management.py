# PYTHON script
import os
import ansa
from ansa import constants
from ansa import base
from ansa import mesh
from ansa import utils
deck = constants.OPENFOAM
body_attachments = ['010804', '011411', '011413', '011418', '011601', '011608', '150201']
front_bumper = ['011901']
front_end = ['010203', '010204', '010205', '010801', '170101']
front_suspension = ['020104', '040101', '040102', '040104', '040105', '040301']
mirrors = ['010902']
rear_bumper = ['011902']
rear_end = ['010107', '170304']
rear_suspension = ['020105', '040201', '040202', '040203', '040204', '040205', '040302']
under_engine_closures = ['010202', '010208', '010210']
underbody_shields = ['010207', '010603']

def aero_pm():
	pass

def ub_shields_lock(ub_cpsc):
	base.SetViewButton({"LOCK": "off"})
	base.All()
	ent_to_lock = []
	for cpsc in underbody_shields:
		ent_to_lock.append(base.NameToEnts(cpsc+".*")[0])
	print(ent_to_lock)
	base.Or(ent_to_lock)
	closed_body_lock = base.SetViewAngles(f_key="F10")
	lock = base.StoreLockView("underbody_shields", overwrite=True)
	lock.set_entity_values(deck, {'ID':2})

def closed_body_lock(vol_list):
	vals = ('Volume',)
	max_volume = 0
	for volume in volume_list:
		get_volume = base.GetEntityCardValues(deck, volume, vals)
		if get_volume['Volume'] > max_volume:
			max_volume = get_volume['Volume']
			closed_body = volume
	if max_volume > 10 ** 9:
		base.Or(closed_body)
		#print(max_volume)
		closed_body_lock = base.SetViewAngles(f_key="F10")
		lock = base.StoreLockView("10_Closed_body", overwrite=True)
		return lock
	else:
		print("\nClosed Body can't be detected using volume autodetect function\nCreate a closed body volume manually and run this script again\n")


if __name__ == '__main__':
	#base.SetViewButton({"LOCK": "off"})
	"""base.All()	
	volume_list = mesh.VolumesDetect(1, return_volumes=True, whole_db=True)	
	if volume_list is None:
		volume_list = base.CollectEntities(deck, None, 'VOLUME')
	to_hide = closed_body_lock(volume_list)
	base.SetViewButton({"LOCK": "off"})
	base.All()
	base.Not(to_hide)"""
	ub_shields_lock(underbody_shields)
