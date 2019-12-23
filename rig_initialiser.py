from maya import cmds
import create_cmpnt

class Rig_Initialiser:

	def __init__(self):
		self.list_cmpnt= {
		'base':['master_M_'],
		'biped':['master_M_', 'head_M_', 'body_M_', 'arm_L_', 'hand_L_', 'arm_R_', 'hand_R_', 'leg_L_', 'foot_L_', 'leg_R_', 'foot_R_'],
		'quadruped':['master_M_', 'head_M_', 'body_M_', 'tail_M_', 'arm_L_', 'hand_L_', 'arm_R_', 'hand_R_', 'leg_L_', 'foot_L_', 'leg_R_', 'foot_R_']
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
