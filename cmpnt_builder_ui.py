from PySide2 import QtCore, QtGui, QtWidgets

class Cmpnt_builder(QtWidgets.QWidget):

    def __init__(self, parent= None):

        super(Cmpnt_builder, self).__init__(parent)

        self.addItem()
        self.addLayout()
        self.addConnection(self)

    def addItem(self):

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

        self.btnLayout= QtWidgets.QHBoxLayout()

        for btn in self.list_btn:
            self.btnLayout.addWidget(btn)


        self.setLayout(self.btnLayout)

    def addConnection(self):

        pass
