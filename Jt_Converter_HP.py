import os
import ansa
from ansa import base
from ansa import utils
from ansa import session

"""
This script will convert jt files into ansa and copy the material properties to corresponding pid from cad data
"""

def jt_converter():
   base.SetANSAdefaultsValues({
   'TRANSL_FLATTEN_ASSEMBLIES_JT_WITH_JTOPEN' : 'true',
   'TRANSL_FILTERS_STATUS_JT_WITH_JTOPEN' : 'all',
   'TRANSL_PREVIEW_JT_WITH_JTOPEN' : 'false',
   'TRANSL_FILTERS_INCLUSIVE_JT_WITH_JTOPEN' : '',
   'TRANSL_NAME_BASED_INSTANTIATION_JT_WITH_JTOPEN' : 'false',
   'TRANSL_SINGLE_PART_JT_WITH_JTOPEN' : 'false',
   'TRANSL_HIDDEN_JT_WITH_JTOPEN' : 'false',
   'TRANSL_FREE_GEOMETRY_JT_WITH_JTOPEN' : 'true',
   'TRANSL_FILTERS_OR_JT_WITH_JTOPEN' : '',
   'TRANSL_REFERENCE_SETS_STATUS_JT_WITH_JTOPEN' : 'all',
   'TRANSL_REFERENCE_SETS_INCLUSIVE_JT_WITH_JTOPEN' : '',
   'TRANSL_REFERENCE_SET_OR_JT_WITH_JTOPEN' : '',
   'TRANSL_READ_MODE_JT_WITH_JTOPEN' : 'both',
   'TRANSL_GEOM_MODE_JT_WITH_JTOPEN' : 'both',
   'TRANSL_FACETTED_DATA_JT_WITH_JTOPEN' : '1, 0, 0',
   'TRANSL_LOD_JT_WITH_JTOPEN' : 0,
   'TRANSL_WIREFRAME_JT_WITH_JTOPEN' : 'true',
   'TRANSL_PMI_JT_WITH_JTOPEN' : 'true',
   'TRANSL_GENERATE_3D_CURVES_JT_WITH_JTOPEN' : 'false',
   'TRANSL_CONSTRUCTION_SURFACES_JT_WITH_JTOPEN' : 'true',
   'TRANSL_BODY2PID_JT_WITH_JTOPEN' : 'true',
   'TRANSL_COLOR2PID_JT_WITH_JTOPEN' : 'false',
   'TRANSL_PART2PID_JT_WITH_JTOPEN' : 'false',
   'TRANSL_SINGLEPID_JT_WITH_JTOPEN' : 'false',
   'TRANSL_SINGLEPID_VALUE_JT_WITH_JTOPEN' : 1,
   'TRANSL_CREATE_VOLUMES_JT_WITH_JTOPEN' : 'false',
   'TRANSL_CREATE_SETS_JT_WITH_JTOPEN' : 'false',
   'TRANSL_PERFORM_TOPOLOGY_JT_WITH_JTOPEN' : 'true',
   'TRANSL_TOPO_BETWEEN_LAYERS_JT_WITH_JTOPEN' : 'true',
   'TRANSL_TOPO_BETWEEN_PARTS_JT_WITH_JTOPEN' : 'false',
   'TRANSL_RESPECT_FILE_TOPO_JT_WITH_JTOPEN' : 'true',
   'TRANSL_GEOMETRY_CLEAN_UP_JT_WITH_JTOPEN' : 'false',
   'TRANSL_TIMEOUT_JT_WITH_JTOPEN' : 'false',
   'TRANSL_TIMEOUT_VALUE_JT_WITH_JTOPEN' : 1,
   'TRANSL_OPEN_SETTINGS_BEFORE_TRANSLATION' : 'false',
   'TRANSL_EXTRA_OPTIONS' : 'false',
   'TRANSL_EXTRA_OPTIONS_VALUE' : '',
   'TRANSL_LOG' : 'true',
   'TRANSL_LOG_VALUE' : '',
   'TRANSL_ASSOCIATION_JT_WITH_JTOPEN' : 'true',
   'TRANSL_ASSOCIATION_NEUTRAL_FILES' : 'true',
   'TRANSL_ASSOCIATION_NX_WITH_CT' : 'true',
   'TRANSL_ASSOCIATION_PARASOLID_WITH_CT' : 'true',
   'TRANSL_POST_ACTIONS_PER_PART' : 'false',
   'TRANSL_SCRIPT_PER_PART' : '',
   'TRANSL_FUNCTION_PER_PART' : '',
   'TRANSL_POST_ACTIONS_ALL_PARTS' : 'false',
   'TRANSL_SCRIPT_ALL_PARTS' : '',
   'TRANSL_FUNCTION_ALL_PARTS' : '',
   'TRANSL_NTOLERANCE' : '0.05',
   'TRANSL_CTOLERANCE' : '0.2',
   'TRANSL_TOLERANCE_MODE' : 'middle',
   'TRANSL_CURVES_RESOLUTION' : '5',
   'TRANSL_PERIMETER_LENGTH' : '20',
   'TRANSL_DISTORTION_DISTANCE' : '15%',
   'TRANSL_DISTORTION_ANGLE' : '0',
   'TRANSL_UNITS' : 'millimeter',
   })   
   jt_files = utils.SelectOpenFile(1, 'JT file (*.jt)')
   for i in jt_files:
   	session.New("discard")
   	print(i)
   	base.Open(i)
   	import radtherm_mat_from_cad
   	radtherm_mat_from_cad.material()
   	base.Save()

if __name__ == '__main__':
   jt_converter()
