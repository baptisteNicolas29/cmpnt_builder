from maya import cmds
import create_cmpnt

class Rig_Initialiser:

	def __init__(self):
		self.list_cmpnt= {
		'base':['master_M'],
		'biped':['master_M', 'head_M', 'body_M', 'arm_L', 'hand_L', 'arm_R', 'hand_R', 'leg_L', 'foot_L', 'leg_R', 'foot_R'],
		'quadruped':['master_M', 'head_M', 'body_M', 'tail_M', 'arm_L', 'hand_L', 'arm_R', 'hand_R', 'leg_L', 'foot_L', 'leg_R', 'foot_R']
		}

	def build_base_rig(self):

		cmds.createNode('transform', n= '__grp') if not cmds.objExists('__grp') else None
		cmds.createNode('transform', n= '__geo_grp', p= '__grp') if not cmds.objExists('__geo_grp') else None
		cmds.createNode('transform', n= '__result_grp', p= '__grp') if not cmds.objExists('__result_grp') else None
		cmds.createNode('transform', n= '__ctrl_grp', p= '__grp') if not cmds.objExists('__ctrl_grp') else None

		cmds.setAttr('__geo_grp.inheritsTransform', 0)
		cmds.setAttr('__result_grp.inheritsTransform', 0)
		cmds.setAttr('__ctrl_grp.inheritsTransform', 0)

	def build_chose_cmpnt(self, cmpnt_list_name):

		create_cmpnt.create_multiple_cmpnt(self.list_cmpnt[cmpnt_list_name])

	def rig_finaliser(self, elem= cmds.ls(sl= 1)):

		if isinstance(elem, (list, tuple)):

			for node in elem:

				print node

				for value in cmds.listRelatives(node, ad= 1):
					cmds.rename(value, value.replace(':', ''))

		elif isinstance(elem, str):

			print 'is string'
			print cmds.listRelatives(elem, ad= 1)
			for node in cmds.listRelatives(elem, ad= 1):
				cmds.rename(node, node.replace(':', ''))
