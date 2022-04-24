"""Program to run the bCNC software for different CNCs connected to the same computer.
Copyright (C) 2022  Angel Maldonado

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>. """

import configparser
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon
import subprocess
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class ConfigManagement():
    def __init__(self):
        self.dir = Path("./profiles")
       
    #Method to get the profiles from the profiles directory and return them as a list
    def getProfiles(self):
        return list(self.dir.glob('*.ini'))

    def getConfigFilePath(self):
        return Path.home() / ".bCNC"

    #Method to update the config file with the new settings from profile
    def updateConfigFile(self, srcpath ):
        cfg_dest = configparser.ConfigParser()
        cfgpath = self.getConfigFilePath()
        cfg_dest.read(cfgpath)

        cfg_src = configparser.ConfigParser()
        cfg_src.read(srcpath)

        logging.debug("Fields to be updated: ")
        for section in cfg_src.sections():
            for option in cfg_src.options(section):
                try:
                    cfg_dest[section][option] = cfg_src[section][option]
                    logging.debug("   " + option + " : " + cfg_dest[section][option] + " -> " + cfg_src[section][option] )
                except:
                    logging.error("Error, section or option not found")
        
        #Update .bCNC configuration file
        with open(cfgpath, 'w') as configfile: 
            cfg_dest.write(configfile)
            logging.info("Configuration .bCNC file updated")

class laucherApp(QWidget):
    def __init__(self):
        super(laucherApp,self).__init__()
        self.config = ConfigManagement()
        self.initUI( )
        self.show()

    # method for creating the ui window
    def initUI(self):
        self.icon_dir = Path("./icons")
        self.setWindowIcon(QIcon( str(self.icon_dir / "icons8-cnc-machine-52.png")))
        self.setWindowTitle("bCNC Launcher")
        self.setFixedSize(450, 100)
        self.centerWindow()
        
        self.initComponents()
        
    # method for centering the window
    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # method for creating the ui components
    def initComponents(self):

        height = 30
        ypos = 40
        # Creating a label
        label = QLabel("Select CNC:", self)
        label.move(20, ypos)
        label.setFixedHeight( height)

        # creating a dropdown box widget
        self.dropdown = QComboBox(self)
        self.dropdown.move(100, ypos ) # setting geometry of combo box
        self.dropdown.setFixedSize(200, height) # setting the width of combo box
        for i in self.config.getProfiles():
            self.dropdown.addItem(i.with_suffix('').name)

        # Creating a button
        button = QPushButton(self)
        button.setText("Launch bCNC")
        button.move( 300, ypos )
        button.setFixedHeight(height)
        button.setIcon(QIcon( str( self.icon_dir / "icons8-play-96.png")) ) #icon
        button.clicked.connect(self.launch)

    def launch(self):
        name = self.dropdown.currentText()
        path = self.config.dir / (name + ".ini")
        self.config.updateConfigFile( path )
        subprocess.Popen("python -m bCNC", shell=True)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = laucherApp()
    sys.exit(app.exec_()) 