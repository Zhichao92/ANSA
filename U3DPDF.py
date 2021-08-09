# Script to create 3D PDF file from ansa
# Need to give file path as input. Since 3D PDF don't have an option export visible parts, an workaround is created to achieve that.
# Visible part is saved in separate file and open in separate model to save it as pdf. Then the temporary file will be deleted by this script.
# This script will be obsolete when ansa will make this function available in their menu

import os
import ansa
from ansa import guitk
from ansa import constants 
from ansa import base
from ansa import utils
from ansa import session

@session.defbutton('TSE', '3DPDF', 'Export 3D PDF from ansa')
def pdf3d():
	CVals_22 = ["All", "Visible"]
	TopWindow = guitk.BCWindowCreate("3D PDF Output", guitk.constants.BCOnExitDestroy)
	BCHBox_1 = guitk.BCHBoxCreate(TopWindow)
	BCLabel_1 = guitk.BCLabelCreate(BCHBox_1, "Output")
	BCComboBox_1 = guitk.BCComboBoxCreate(BCHBox_1, CVals_22)	
	BCDialogButtonBox_1 = guitk.BCDialogButtonBoxCreate(TopWindow)	
	guitk.BCWindowAdjustSize(TopWindow)
	guitk.BCWindowSetAcceptFunction(TopWindow, _OkPressed, BCComboBox_1)
	guitk.BCWindowSetRejectFunction(TopWindow, _CancelPressed, None)
	guitk.BCComboBoxSetSizePolicy(BCComboBox_1, guitk.constants.BCMinimum, guitk.constants.BCFixed)
	guitk.BCShow(TopWindow)
	
def _OkPressed(w, data):
	required_parts = guitk.BCComboBoxCurrentText(data)
	
	if required_parts == 'All':
		filename = utils.SelectSaveFile("*.pdf")
		print('\n Please Wait. Saving File')		
		base.OutputU3DPDF(filename[0])
		print('Save Completed')
		print(filename[0])
	else:		
		filename = utils.SelectSaveFile("*.pdf")		
		dir_name = filename[0].split('/')[:-1]
		dir_name.append('file_to_delete.ansa')
		temp_ansa_file = '/'.join(dir_name)		
		base.SaveVisibleAs(temp_ansa_file)
		old_model = base.GetCurrentAnsaModel()
		temp_model = base.CreateNewAnsaModel()
		base.SetCurrentAnsaModel(temp_model)
		utils.Merge(temp_ansa_file)
		print('\n Please Wait. Saving File')
		base.OutputU3DPDF(filename[0])
		base.SetCurrentAnsaModel(old_model)
		base.DestroyAnsaModel(temp_model)
		os.remove(temp_ansa_file)
		print('Save Completed')
		print(filename[0])
		#print(temp_ansa_file)
		#base.OutputU3DPDF(filename)	
	return 1
	
def _CancelPressed(w, data):
	print("\n Output is Cancelled \n")
	return 1
