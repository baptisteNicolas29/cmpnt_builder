from PySide2 import QtCore, QtGui, QtWidgets

class Cmpnt_builder(QtWidgets.QWidget):

    def __init__(self, parent= None):

        super(Cmpnt_builder, self).__init__(parent)

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

        self.file_menu.addAction(self.init_action)
        self.file_menu.addAction(self.finalise_action)
        self.file_menu.addAction(self.exit_action)


        self.list_btn= [
        QtWidgets.QPushButton('Create\nCmpnt'),
        QtWidgets.QPushButton('Set\nInput'),
        QtWidgets.QPushButton('Set\nOutput'),
        QtWidgets.QPushButton('Output\nTo\nInput'),
        QtWidgets.QPushButton('Create\nBuffer')
        ]

        self.iconList= [
        '/home/baptiste_nicolas/maya/2018/prefs/icons/cmpnt.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/input_output.svg',
        '/home/baptiste_nicolas/maya/2018/prefs/icons/buffer.svg'
        ]

        for idx, btn in enumerate(self.list_btn):

            #btn.setIcon(QtGui.QIcon(self.iconList[idx]))
            #btn.setIconSize(QtCore.QSize(50,50))
            #btn.setLayoutDirection(QtCore.Qt.RightToLeft)


            btn.setMaximumHeight(75)
            btn.setMaximumWidth(75)

            btn.setMinimumHeight(75)
            btn.setMinimumWidth(75)

    def addLayout(self):
        self.mainLayout= QtWidgets.QVBoxLayout()
        self.btnLayout= QtWidgets.QHBoxLayout()


        self.btnLayout.setMenuBar(self.menu_bar)
        for btn in self.list_btn:
            self.btnLayout.addWidget(btn)


        self.setLayout(self.btnLayout)

    def addConnection(self):

        self.exit_action.triggered.connect(self.close)
