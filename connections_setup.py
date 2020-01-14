from maya import cmds
from maya.api.OpenMaya import MMatrix

def output_to_input():
	pass

def input_to_ctrl():
	pass

def ctrl_to_output(ctrl_nodes):

	for ctrl in ctrl_nodes:
		print cmds.ls(ctrl, l= 1)[0].split('|')
		for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):

			if elem_node.endswith(':_cmpnt'):

				cmpnt_namespace= elem_node.split(':')[0]
				cmds.createNode('transform', n= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), p= '{0}:_output'.format(cmpnt_namespace), ss= 1) if not cmds.objExists('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl)) else None

				cmds.addAttr('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ln= 'output_world_matrix', at= 'matrix') if not cmds.attributeQuery('output_world_matrix', node= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ex= 1) else None

				cmds.addAttr(ctrl, '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ln= 'output_cmpnt', at= 'message') if  not cmds.attributeQuery('output_cmpnt', node= ctrl, ex= 1)else None
				cmds.addAttr('{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ln= 'output_cmpnt', at= 'message') if  not cmds.attributeQuery('output_cmpnt', node= '{0}:_output_:{1}'.format(cmpnt_namespace, ctrl), ex= 1)else None

				cmds.connectAttr('{0}.output_cmpnt'.format(ctrl), '{0}:_output_:{1}.output_cmpnt'.format(cmpnt_namespace, ctrl), f= 1)
				cmds.connectAttr('{0}.worldMatrix[0]'.format(ctrl), '{0}:_output_:{1}.output_world_matrix'.format(cmpnt_namespace, ctrl), f= 1)

def ctrl_to_input(ctrl_nodes):
	for ctrl in ctrl_nodes:

		for elem_node in cmds.ls(ctrl, l= 1)[0].split('|'):

			if elem_node.endswith(':_cmpnt'):

				cmpnt_ns= elem_node.split(':')[0]

				ctrlBuffer= cmds.listConnections('{0}.{1}'.format(ctrl, 'buffer_cmpnt'), s= 1)[0] if cmds.connectionInfo('{0}.{1}'.format(ctrl, 'buffer_cmpnt'), id= True) else ctrl
				print ctrlBuffer

				inputNode= cmds.createNode('transform', n= '{0}:_input_:{1}'.format(cmpnt_ns, ctrl), p= '{0}:_input'.format(cmpnt_ns), ss= 1) if not cmds.objExists('{0}:_input_:{1}'.format(cmpnt_ns, ctrl)) else '{0}:_input_:{1}'.format(cmpnt_ns, ctrl)
				multMat= cmds.createNode('multMatrix', n= '{0}_input_multMat'.format(ctrl), ss= 1) if not cmds.objExists('{0}_input_multMat'.format(ctrl)) else '{0}_input_multMat'.format(ctrl)
				decMat= cmds.createNode('decomposeMatrix', n= '{0}_input_decMat'.format(ctrl), ss= 1) if not cmds.objExists('{0}_input_decMat'.format(ctrl)) else '{0}_input_decMat'.format(ctrl)

				cmds.addAttr(inputNode, ln= 'input_cmpnt', at= 'message') if not cmds.attributeQuery('input_cmpnt', node= inputNode, ex= 1) else None
				cmds.addAttr(inputNode, ln= 'input_world_matrix', at= 'matrix') if not cmds.attributeQuery('input_world_matrix', node= inputNode, ex= 1) else None

				cmds.addAttr(ctrlBuffer, ln= 'input_cmpnt', at= 'message') if not cmds.attributeQuery('input_cmpnt', node= ctrlBuffer, ex= 1) else None
				cmds.addAttr(ctrlBuffer, ln= 'input_offset_world_matrix', at= 'matrix') if not cmds.attributeQuery('input_offset_world_matrix', node= ctrlBuffer, ex= 1) else None

				cmds.connectAttr('{0}.{1}'.format(inputNode, 'input_cmpnt'), '{0}.{1}'.format(ctrlBuffer, 'input_cmpnt'), f= 1)

				offset_matrix= MMatrix(cmds.getAttr('{0}.input_world_matrix'.format(inputNode))).inverse()* MMatrix(cmds.getAttr('{0}.worldMatrix[0]'.format(ctrlBuffer)))

				cmds.setAttr('{0}.{1}'.format(ctrlBuffer, 'input_offset_world_matrix'), offset_matrix, typ= 'matrix')

				#cmds.connectAttr('{0}.{1}'.format(), '{0}.{1}'.format(), f= 1)

				cmds.connectAttr('{0}.{1}'.format(ctrlBuffer, 'input_offset_world_matrix'), '{0}.{1}'.format(multMat, 'matrixIn[0]'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(inputNode, 'input_world_matrix'), '{0}.{1}'.format(multMat, 'matrixIn[1]'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(ctrlBuffer, 'parentInverseMatrix[0]'), '{0}.{1}'.format(multMat, 'matrixIn[2]'), f= 1)

				cmds.connectAttr('{0}.{1}'.format(multMat, 'matrixSum'), '{0}.{1}'.format(decMat, 'inputMatrix'), f= 1)

				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputTranslate'), '{0}.{1}'.format(ctrlBuffer, 't'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputRotate'), '{0}.{1}'.format(ctrlBuffer, 'r'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputScale'), '{0}.{1}'.format(ctrlBuffer, 's'), f= 1)
				cmds.connectAttr('{0}.{1}'.format(decMat, 'outputShear'), '{0}.{1}'.format(ctrlBuffer, 'shear'), f= 1)

def output_to_input(input, output):
	output_node= ''
	input_node= []

	for node in input:

		if ':_input_:' in node:

			input_node+= [node]

		elif cmds.attributeQuery('input_cmpnt', n= node, ex= 1):

			if ':_input_:' in cmds.listConnections('{0}.{1}'.format(node, 'input_cmpnt'), s= 1, d= 0)[0]:

				input_node+= [cmds.listConnections('{0}.{1}'.format(node, 'input_cmpnt'), s= 1, d= 0)[0]]

		elif cmds.attributeQuery('buffer_cmpnt', n= node, ex= 1):

			if cmds.listConnections('{0}.{1}'.format(node, 'buffer_cmpnt')):

				buffer= cmds.listConnections('{0}.{1}'.format(node, 'buffer_cmpnt'))[0]

				if cmds.attributeQuery('input_cmpnt', n= buffer, ex= 1):

					input_node+= [cmds.listConnections('{0}.{1}'.format(buffer, 'input_cmpnt'))[0]]

	if ':_output_:' in output:
		output_node= output

	elif cmds.attributeQuery('output_cmpnt', n= output, ex= 1):

		if ':_output_:' in cmds.listConnections('{0}.{1}'.format(output, 'output_cmpnt'))[0]:
			output_node= cmds.listConnections('{0}.{1}'.format(output, 'output_cmpnt'))[0]
	else:
		print None
		#raise error: 'no valid output selected'

	print output_node

	for node in input_node:

		for destination in cmds.listConnections('{0}.{1}'.format(node, 'input_cmpnt'), s= 0, d= 1):
			print destination
			print MMatrix(cmds.getAttr('{0}.worldMatrix[0]'.format(destination)))
			offset_matrix= MMatrix(cmds.getAttr('{0}.worldMatrix[0]'.format(destination)))* MMatrix(cmds.getAttr('{0}.output_world_matrix'.format(output_node))).inverse()

			cmds.setAttr('{0}.{1}'.format(destination, 'input_offset_world_matrix'), offset_matrix, typ= 'matrix')

			cmds.connectAttr('{0}.{1}'.format(output_node, 'output_cmpnt'), '{0}.{1}'.format(node, 'input_cmpnt'), f= 1)
			cmds.connectAttr('{0}.{1}'.format(output_node, 'output_world_matrix'), '{0}.{1}'.format(node, 'input_world_matrix'), f= 1)
