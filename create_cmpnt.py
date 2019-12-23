from maya import cmds

def set_outliner_color(node, outliner_color= [1, 1, 1]):

    cmds.setAttr(node+ '.useOutlinerColor', 1)
    cmds.setAttr(node+ '.outlinerColorR', outliner_color[0])
    cmds.setAttr(node+ '.outlinerColorG', outliner_color[1])
    cmds.setAttr(node+ '.outlinerColorB', outliner_color[2])

def create_multiple_cmpnt(cmpnt_list= cmds.ls(sl= 1)):

    for node in cmpnt_list:

        create_cmpnt(node)

def create_cmpnt(cmpnt_name):

    parent_node= None

    if cmds.objExists(cmpnt_name):

        cmds.delete(cmpnt_name)

    cmds.createNode('transform', n= '{0}:_cmpnt'.format(cmpnt_name), p= '__ctrl_grp' if cmds.objExists('__ctrl_grp') else None, ss= 1) if not cmds.objExists('{0}:_cmpnt'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_input'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_input'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_output'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_output'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_public'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_public'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_private'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_private'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_deform'.format(cmpnt_name), p= '{0}:_private'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_deform'.format(cmpnt_name)) else None
    cmds.createNode('transform', n= '{0}:_proxi'.format(cmpnt_name), p= '{0}:_private'.format(cmpnt_name), ss= 1) if not cmds.objExists('{0}:_proxi'.format(cmpnt_name)) else None

    set_outliner_color('{0}:_input'.format(cmpnt_name), [.5, .5, 1])
    set_outliner_color('{0}:_output'.format(cmpnt_name), [.5, .5, 1])
    set_outliner_color('{0}:_public'.format(cmpnt_name), [.5, 1, .5])
    set_outliner_color('{0}:_private'.format(cmpnt_name), [1, .5, .5])
    set_outliner_color('{0}:_deform'.format(cmpnt_name), [1, 1, .5])
    set_outliner_color('{0}:_proxi'.format(cmpnt_name), [1, 1, .5])
