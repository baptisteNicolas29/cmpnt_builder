from maya import cmds

def output_to_input():
	pass

def input_to_ctrl():
	pass

def ctrl_to_output(ctrl_nodes= cmds.ls(sl= 1)):

	for ctrl in ctrl_nodes:

		for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):
			print elem_node

			if elem_node.endswith(':_cmpnt'):
				cmpnt_namespace= elem_node.split(':')[0]
				cmds.createNode('transform', n= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), p= '{0}:_output'.format(cmpnt_namespace), ss= 1) if not cmds.objExists('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl)) else None

				cmds.addAttr('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ln= 'output_world_matrix', at= 'matrix') if not cmds.attributeQuery('output_world_matrix', node= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ex= 1) else None
				cmds.connectAttr('{0}.worldMatrix[0]'.format(ctrl), '{0}:_output_:{1}.output_world_matrix'.format(cmpnt_namespace, ctrl), f= 1)

def ctrl_to_input():
	pass
