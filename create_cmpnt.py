from maya import cmds

class CreateCmpnt:

    def __init__(self):
        pass

    def set_outliner_color(self, node, outliner_color= [1, 1, 1]):

        cmds.setAttr(node+ '.useOutlinerColor', 1)
        cmds.setAttr(node+ '.outlinerColorR', outliner_color[0])
        cmds.setAttr(node+ '.outlinerColorG', outliner_color[1])
        cmds.setAttr(node+ '.outlinerColorB', outliner_color[2])

    def create_multiple_cmpnt(self, cmpnt_list= cmds.ls(sl= 1)):

        for node in cmpnt_list:

            self.create_cmpnt(node)

    def create_cmpnt(self, cmpnt_name):

        parent_node= None

        if cmds.objExists(cmpnt_name):

            cmds.delete(cmpnt_name)
            parent_node= cmds.listRelatives(cmpnt_name, p= 1)[0]

        cmds.createNode('transform', n= '{0}:_cmpnt'.format(cmpnt_name), p= '__ctrl_grp' if cmds.objExists('__ctrl_grp') else None, ss= 1)
        cmds.createNode('transform', n= '{0}:_input'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1)
        cmds.createNode('transform', n= '{0}:_output'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1)
        cmds.createNode('transform', n= '{0}:_public'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1)
        cmds.createNode('transform', n= '{0}:_private'.format(cmpnt_name), p= '{0}:_cmpnt'.format(cmpnt_name), ss= 1)
        cmds.createNode('transform', n= '{0}:_deform'.format(cmpnt_name), p= '{0}:_private'.format(cmpnt_name), ss= 1)
        cmds.createNode('transform', n= '{0}:_proxi'.format(cmpnt_name), p= '{0}:_private'.format(cmpnt_name), ss= 1)

        self.set_outliner_color('{0}:_input'.format(cmpnt_name), [.5, .5, 1])
        self.set_outliner_color('{0}:_output'.format(cmpnt_name), [.5, .5, 1])
        self.set_outliner_color('{0}:_public'.format(cmpnt_name), [.5, 1, .5])
        self.set_outliner_color('{0}:_private'.format(cmpnt_name), [1, .5, .5])
        self.set_outliner_color('{0}:_deform'.format(cmpnt_name), [1, 1, .5])
        self.set_outliner_color('{0}:_proxi'.format(cmpnt_name), [1, 1, .5])
