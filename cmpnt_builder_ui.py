from maya import cmds
from PySide2 import QtCore, QtGui, QtWidgets
import connections_setup
import create_cmpnt
import rig_initialiser

reload(rig_initialiser)
reload(create_cmpnt)
reload(connections_setup)

class Cmpnt_builder(QtWidgets.QDialog):

    def __init__(self, parent= None):

        super(Cmpnt_builder, self).__init__(parent)
        self.rig_initialiser= rig_initialiser.Rig_Initialiser()

        self.addItem()
        self.addLayout()
        self.addConnection()

    def addItem(self):

        self.menu_bar= QtWidgets.QMenuBar()
        self.file_menu= self.menu_bar.addMenu('File')
        self.help_menu= self.menu_bar.addMenu('Help')

        self.init_action= QtWidgets.QAction("Initialise Rig", self)
        self.finalise_action= QtWidgets.QAction("Finalise Rig", self)
        self.exit_action= QtWidgets.QAction("Exit", self)

        self.about_action= QtWidgets.QAction("About", self)
        self.api_action= QtWidgets.QAction("Go to API", self)

        self.file_menu.addAction(self.init_action)
        self.file_menu.addAction(self.finalise_action)
        self.file_menu.addAction(self.exit_action)

        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.api_action)

        self.list_btn= {
        'build_cmpnt': QtWidgets.QPushButton('Create\nCmpnt'),
        'output_to_input': QtWidgets.QPushButton('Output\nTo input'),
        'set_input': QtWidgets.QPushButton('Set as\nInput'),
        'set_output': QtWidgets.QPushButton('Set as\nOutput'),
        'buid_ctrl': QtWidgets.QPushButton('Spawn\nControler'),
        'build_buffer': QtWidgets.QPushButton('Create\nBuffer')
        }

        self.iconList= [
        '/home/baptiste_nicolas/maya/2018/prefs/icons/cmpnt.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/buffer.svg'
        ]

        for idx, btn_id in enumerate(self.list_btn):

            btn= self.list_btn[btn_id]

            #btn.setIcon(QtGui.QIcon(self.iconList[idx]))
            btn.setIconSize(QtCore.QSize(50,50))
            btn.setLayoutDirection(QtCore.Qt.RightToLeft)

            btn.setMaximumHeight(75)
            btn.setMaximumWidth(75)

            btn.setMinimumHeight(75)
            btn.setMinimumWidth(75)

    def addLayout(self):

        self.mainLayout= QtWidgets.QVBoxLayout()
        self.btnLayout= QtWidgets.QHBoxLayout()

        self.btnLayout.setMenuBar(self.menu_bar)


        self.btnLayout.addWidget(self.list_btn['build_cmpnt'])
        self.btnLayout.addWidget(self.list_btn['output_to_input'])
        self.btnLayout.addWidget(self.list_btn['set_input'])
        self.btnLayout.addWidget(self.list_btn['set_output'])
        self.btnLayout.addWidget(self.list_btn['buid_ctrl'])
        self.btnLayout.addWidget(self.list_btn['build_buffer'])

        self.setLayout(self.btnLayout)

    def addConnection(self):

        self.exit_action.triggered.connect(self.close)
        self.init_action.triggered.connect(lambda *arg: self.rig_initialiser.build_base_rig())
        self.finalise_action.triggered.connect(lambda *arg: self.rig_initialiser.rig_finaliser())

        self.list_btn['build_cmpnt'].clicked.connect(self.build_cmpnt)

        self.list_btn['output_to_input'].clicked.connect(lambda *arg: connections_setup.output_to_input(cmds.ls(sl= 1)[1:], cmds.ls(sl= 1)[0]))
        self.list_btn['set_input'].clicked.connect(lambda *arg: connections_setup.ctrl_to_input(cmds.ls(sl= 1)))
        self.list_btn['set_output'].clicked.connect(lambda *arg: connections_setup.ctrl_to_output(cmds.ls(sl= 1)))

        self.list_btn['buid_ctrl'].clicked.connect(self.build_ctrl)
        self.list_btn['build_buffer'].clicked.connect(lambda *arg: create_cmpnt.build_buffer(cmds.ls(sl= 1)))

    def build_cmpnt(self):

        value, is_ok = QtWidgets.QInputDialog.getText(self, "component name", "enter componenent name here")
        create_cmpnt.create_cmpnt(value) if is_ok == True else None


    def build_ctrl(self):

        value, is_ok = QtWidgets.QInputDialog.getText(self, "controler name", "enter controler name here")
        create_cmpnt.build_ctrl(value, cmds.ls(sl= 1)) if is_ok == True else None
