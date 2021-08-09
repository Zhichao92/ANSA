import ansa
from ansa import base
from ansa import constants
import re
NASTRAN = constants.NASTRAN

#'issues' is a matrix that contains the selected entities
def _FixCheckPropertyNames(issues):
    for issue in issues:
        print(issue.has_fix)
        problem_description = issue.description
        ents = issue.entities
        for ent in ents:
            values = base.GetEntityCardValues(NASTRAN,ent,('Name',))
            name = values['Name']
            if 'numbers' in problem_description:
                name = re.sub('[0-9]','',name)
            if 'character' in problem_description:
                pattern = problem_description[32:33]
                name = name.replace(pattern,'_')
            success = base.SetEntityCardValues(NASTRAN,ent,{'Name':name})    
        if(success==0):
            issue.is_fixed = True
            issue.update()


def _ExecCheckPropertyNames(entities,params):
    for parameter_name,parameter_value in params.items():
        print('Parameter name:',parameter_name,' with value ',parameter_value)
        if parameter_name=='Special Character':
            pattern = parameter_value
        elif parameter_name=='Consider Numbers':
            consider_numbers = parameter_value

    # check
    to_report = []
    #Name of the header in the report list
    t = base.CheckReport(type = 'Properties with problematic names')
    t.has_fix = True
    for ent in entities:
        values = base.GetEntityCardValues(NASTRAN,ent,('Name',))
        name = values['Name']
        if pattern in name:
            if consider_numbers==True and re.search('[0-9]',name):
                t.add_issue(entities = [ent], status = 'Error', description = 'Name with identified character '+'\''+pattern+'\''+' and numbers')
            else:
                t.add_issue(entities = [ent], status = 'Error', description = 'Name with identified character '+'\''+pattern+'\'')
        else:
            if consider_numbers==True and re.search('[0-9]',name):
                t.add_issue(entities = [ent], status = 'Warning', description = 'Name with identified numbers')
    to_report.append(t)
    return to_report


def CheckUseInModel():
    options = { 'name':'CheckUseInModel', 
                'exec_action':('_ExecCheckPropertyNames', 'CheckUseInModel.py'), 
                'fix_action':('_FixCheckPropertyNames', 'CheckUseInModel.py'), 
                'deck' : NASTRAN, 
                'requested_types' : ('PSHELL', 'PSOLID' ,'PBEAM'),
                'info':'Check whether use in model in PID is enabled' 
               }
    my_check = base.CheckDescription(**options) 
   	descr = [my_check] 
    saved = base.CheckDescription.save(descriptions = descr, file = 'HP_Check.plist')
