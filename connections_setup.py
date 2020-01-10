from maya import cmds
from maya.api.OpenMaya import MMatrix

def output_to_input():
	pass

def input_to_ctrl():
	pass

def ctrl_to_output(ctrl_nodes= cmds.ls(sl= 1)):

	for ctrl in ctrl_nodes:
		print cmds.ls(ctrl, l= 1)[0].split('|')
		for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):

			if elem_node.endswith(':_cmpnt'):

				cmpnt_namespace= elem_node.split(':')[0]
				cmds.createNode('transform', n= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), p= '{0}:_output'.format(cmpnt_namespace), ss= 1) if not cmds.objExists('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl)) else None

				cmds.addAttr('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ln= 'output_world_matrix', at= 'matrix') if not cmds.attributeQuery('output_world_matrix', node= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ex= 1) else None
				cmds.connectAttr('{0}.worldMatrix[0]'.format(ctrl), '{0}:_output_:{1}.output_world_matrix'.format(cmpnt_namespace, ctrl), f= 1)

def ctrl_to_input(ctrl_nodes= cmds.ls(sl= 1)):
	for ctrl in ctrl_nodes:

		for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):

			if elem_node.endswith(':_cmpnt'):
				cmpnt_namespace= elem_node.split(':')[0]

				ctrl_buffer= cmds.listRelatives(ctrl, p= 1)[0] if cmds.listRelatives(ctrl, p= 1)[0]== ctrl+ '_buffer' else ctrl

				cmds.createNode('transform', n= '{0}:_input_:{1}'.format(cmpnt_namespace, ctrl), p= '{0}:_input'.format(cmpnt_namespace), ss= 1) if not cmds.objExists('{0}:_input_:{1}'.format(cmpnt_namespace, ctrl)) else '{0}:_input_:{1}'.format(cmpnt_namespace, ctrl)
				multMat= cmds.createNode('multMatrix', n= '{0}_input_world_multMat'.format(ctrl),ss= 1) if not cmds.objExists('{0}_input_world_multMat'.format(ctrl)) else '{0}_input_world_multMat'.format(ctrl)
				decMat= cmds.createNode('decomposeMatrix', n= '{0}_input_world_decMat'.format(ctrl),ss= 1) if not cmds.objExists('{0}_input_world_decMat'.format(ctrl)) else '{0}_input_world_decMat'.format(ctrl)


				cmds.addAttr('{0}:_input_:{1}'.format(cmpnt_namespace, ctrl), ln= 'input_msg', at= 'message') if not cmds.attributeQuery('input_msg', node= '{0}:_input_:{1}'.format(cmpnt_namespace, ctrl), ex= 1) else None
				cmds.addAttr(ctrl_buffer, ln= 'input_msg', at= 'message') if not cmds.attributeQuery('input_msg', node= ctrl_buffer, ex= 1) else None

				cmds.addAttr(ctrl_buffer, ln= 'input_offset_world_matrix', at= 'matrix') if not cmds.attributeQuery('input_offset_world_matrix', node= ctrl_buffer, ex= 1) else None

				cmds.addAttr('{0}:_input_:{1}'.format(cmpnt_namespace, ctrl), ln= 'input_world_matrix', at= 'matrix') if not cmds.attributeQuery('input_world_matrix', node= '{0}:_input_:{1}'.format(cmpnt_namespace, ctrl), ex= 1) else None

				offset_matrix= MMatrix(cmds.getAttr('{0}:_input_:{1}.input_world_matrix'.format(cmpnt_namespace, ctrl))).inverse()* MMatrix(cmds.getAttr('{0}.worldMatrix[0]'.format(ctrl_buffer)))
				cmds.setAttr('{0}.input_offset_world_matrix'.format(ctrl_buffer), offset_matrix, typ= 'matrix')


				cmds.connectAttr('{0}:_input_:{1}.input_msg'.format(cmpnt_namespace, ctrl), '{0}.input_msg'.format(ctrl_buffer), f= 1)

				cmds.connectAttr('{0}:_input_:{1}.input_world_matrix'.format(cmpnt_namespace, ctrl), '{0}.matrixIn[1]'.format(multMat), f= 1)
				cmds.connectAttr('{0}.input_offset_world_matrix'.format(ctrl_buffer), '{0}.matrixIn[1]'.format(multMat), f= 1)
				cmds.connectAttr('{0}.parentInverseMatrix[0]'.format(ctrl_buffer), '{0}.matrixIn[2]'.format(multMat), f= 1)

				cmds.connectAttr('{0}.matrixSum'.format(multMat), '{0}.inputMatrix'.format(decMat), f= 1)

				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputTranslate'), '{0}.{1}'.format(ctrl_buffer, 't'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputRotate'), '{0}.{1}'.format(ctrl_buffer, 'r'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputScale'), '{0}.{1}'.format(ctrl_buffer, 's'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputShear'), '{0}.{1}'.format(ctrl_buffer, 'shear'), f= 1)

def output_to_input(input= cmds.ls(sl= 1)[1:], output= cmds.ls(sl= 1)[0]):
	output= cmds.ls(sl= 1)[-1]
	input= cmds.ls(sl= 1)[:-1]
