from PySide2 import QtCore, QtGui, QtWidgets
import connections_setup
import create_cmpnt
import rig_initialiser

reload(rig_initialiser)
reload(create_cmpnt)
reload(connections_setup)

class Cmpnt_builder(QtWidgets.QWidget):

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
        'output_to_input': QtWidgets.QPushButton('Output\nTo\nInput'),
        'set_input': QtWidgets.QPushButton('Set\nInput'),
        'set_output': QtWidgets.QPushButton('Set\nOutput'),
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
        self.init_action.triggered.connect(self.rig_initialiser.build_base_rig)
        self.finalise_action.triggered.connect(self.rig_initialiser.rig_finaliser)

        self.list_btn['build_cmpnt'].clicked.connect(create_cmpnt.create_multiple_cmpnt)

        self.list_btn['output_to_input'].clicked.connect(connections_setup.output_to_input)
        self.list_btn['set_input'].clicked.connect(connections_setup.ctrl_to_input)
        self.list_btn['set_output'].clicked.connect(connections_setup.ctrl_to_output)

        self.list_btn['build_buffer'].clicked.connect(create_cmpnt.build_buffer)
