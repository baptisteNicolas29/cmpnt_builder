from maya import cmds

def set_outliner_color(node, outliner_color= [1, 1, 1]):

    cmds.setAttr(node+ '.useOutlinerColor', 1)
    cmds.setAttr(node+ '.outlinerColorR', outliner_color[0])
    cmds.setAttr(node+ '.outlinerColorG', outliner_color[1])
    cmds.setAttr(node+ '.outlinerColorB', outliner_color[2])

def create_multiple_cmpnt(cmpnt_list= cmds.ls(sl= 1)):

    if len(cmpnt_list)== 0:

        create_cmpnt(input())

    else:

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

"""
name: build_buffer
argument: drived_selec array nodes used to be buffered
return: None
"""
def build_buffer(drived_selec = cmds.ls(sl=True)):

    for node in drived_selec:

        parent_node= cmds.listRelatives(node, p= 1)[0] if cmds.listRelatives(node, p= 1) else None


        buffer= cmds.createNode('transform', n= node+ '_buffer', p= parent_node, ss= 1) if not cmds.objExists( node+ '_buffer') else node+ '_buffer' #create buffer on node if not already exist

        if not cmds.attributeQuery('buffer_cmpnt', node= buffer, ex= True): cmds.addAttr(buffer, at= 'message', ln= 'buffer_cmpnt')   #create msg attr for buffer if not already exist


        if not cmds.attributeQuery('buffer_cmpnt', node= node, ex= True): cmds.addAttr(node, at= 'message', ln= 'buffer_cmpnt')       #create msg attr for node if not already exist


        cmds.matchTransform(buffer, node, rot= True, pos= True)                         #match buffer translate/rotate to node

        cmds.parent(node, buffer)                                                       #parent node to buffer

        cmds.connectAttr(buffer + '.buffer_cmpnt', node + '.buffer_cmpnt', f= True)     #connect both msg attr

'''
name: build_ctrl
arg: ctrl_name string is the name ctrl how's gon a be created
arg: sel string:array is the curent selection in maya
return: 0 if ctrl name exist or _public transform not exist
'''
def build_ctrl(ctrl_name= '', sel= cmds.ls(sl= 1)):
    cmpnt_namespace= ''
    for ctrl in sel:

        for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):

            if elem_node.endswith(':_cmpnt'):

                cmpnt_namespace= elem_node.split(':')[0]

    parent_node= '{0}:_public'.format(cmpnt_namespace)

    if not cmds.objExists('{0}_{1}'.format(cmpnt_namespace, ctrl_name)) and cmds.objExists(parent_node):

        ctrl_node= cmds.createNode('transform', n= '{0}_{1}'.format(cmpnt_namespace, ctrl_name), p= parent_node)

    else:

        return False

    cmds.setAttr('{0}.{1}'.format(ctrl_node, 'displayHandle'), 1)
    return True
