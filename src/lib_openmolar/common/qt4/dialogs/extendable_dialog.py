#! /usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ##
##  Copyright 2010-2012, Neil Wallace <neil@openmolar.com>                   ##
##                                                                           ##
##  This program is free software: you can redistribute it and/or modify     ##
##  it under the terms of the GNU General Public License as published by     ##
##  the Free Software Foundation, either version 3 of the License, or        ##
##  (at your option) any later version.                                      ##
##                                                                           ##
##  This program is distributed in the hope that it will be useful,          ##
##  but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ##
##  GNU General Public License for more details.                             ##
##                                                                           ##
##  You should have received a copy of the GNU General Public License        ##
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.    ##
##                                                                           ##
###############################################################################

from PyQt4 import QtCore, QtGui
from lib_openmolar.common.qt4.dialogs import BaseDialog

class ExtendableDialog(BaseDialog):
    '''
    builds on BaseDialog, adding an area for advanced options
    unlike BaseDialog.. this dialog has no spacer item by default
    '''
    def __init__(self, parent=None, remove_stretch=True):
        BaseDialog.__init__(self, parent, remove_stretch)

        self.button_box.setCenterButtons(False)

        icon = QtGui.QIcon.fromTheme("go-down")
        #: a pointer to the Advanced button
        self.more_but = QtGui.QPushButton(icon, "&Advanced")
        self.more_but.setFlat(True)

        self.more_but.setCheckable(True)
        self.more_but.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_box.addButton(self.more_but, self.button_box.HelpRole)

        self.setOrientation(QtCore.Qt.Vertical)

        frame = QtGui.QFrame(self)
        layout = QtGui.QVBoxLayout(frame)
        self.setExtension(frame)

    def set_advanced_but_text(self, txt):
        self.more_but.setText(txt)

    def _clicked(self, but):
        '''
        overwrite :doc:`BaseDialog` _clicked
        checking to see if addvanced panel is to be displayed.
        '''
        if but == self.more_but:
            self.showExtension(but.isChecked())
            return
        BaseDialog._clicked(self, but)

    def add_advanced_widget(self, widg):
        self.extension().layout().addWidget(widg)

if __name__ == "__main__":
    app = QtGui.QApplication([])
    dl = ExtendableDialog()
    label = QtGui.QLabel("Test")
    dl.insertWidget(label)
    cb = QtGui.QCheckBox("advanced option")
    dl.add_advanced_widget(cb)
    dl.exec_()
    app.closeAllWindows()
