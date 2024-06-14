#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QVBoxLayout, QPushButton, QRadioButton, 
                             QGroupBox, QHBoxLayout, QMessageBox, QCheckBox)
from PyQt5.QtGui import QClipboard
import qdarkstyle

class HashDecryptionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hashy')
        self.setGeometry(100, 100, 400, 400)

        self.hashLabel = QLabel('Enter your hash:')
        self.hashInput = QLineEdit()

        self.autoDetectCheckBox = QCheckBox('Auto Detect Hash Type')
        self.autoDetectCheckBox.stateChanged.connect(self.toggleAutoDetect)

        self.md5Radio = QRadioButton('MD5')
        self.sha1Radio = QRadioButton('SHA-1')
        self.sha256Radio = QRadioButton('SHA-256')
        self.sha384Radio = QRadioButton('SHA-384')
        self.sha512Radio = QRadioButton('SHA-512')

        self.radioGroupBox = QGroupBox('Hash Type')
        radioLayout = QVBoxLayout()
        radioLayout.addWidget(self.md5Radio)
        radioLayout.addWidget(self.sha1Radio)
        radioLayout.addWidget(self.sha256Radio)
        radioLayout.addWidget(self.sha384Radio)
        radioLayout.addWidget(self.sha512Radio)
        self.radioGroupBox.setLayout(radioLayout)

        self.decryptButton = QPushButton('Decrypt')
        self.decryptButton.clicked.connect(self.decrypt)

        self.copyButton = QPushButton('Copy to Clipboard')
        self.copyButton.clicked.connect(self.copyToClipboard)
        self.copyButton.setEnabled(False)

        self.resultLabel = QLabel('Result:')
        self.resultDisplay = QLineEdit()
        self.resultDisplay.setReadOnly(True)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.hashLabel)
        mainLayout.addWidget(self.hashInput)
        mainLayout.addWidget(self.autoDetectCheckBox)
        mainLayout.addWidget(self.radioGroupBox)
        mainLayout.addWidget(self.decryptButton)
        mainLayout.addWidget(self.resultLabel)
        mainLayout.addWidget(self.resultDisplay)
        mainLayout.addWidget(self.copyButton)
        
        self.setLayout(mainLayout)
        
        self.md5Radio.setChecked(True)
        self.autoDetectCheckBox.setChecked(True)
        self.toggleAutoDetect() 

        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
                background-color: #282828;
                color: #ffffff;
            }
            QLineEdit, QCheckBox, QLabel {
                font-size: 14px;
                padding: 4px;
            }
            QGroupBox {
                border: 2px solid #3a3a3a;
                border-radius: 5px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0066cc;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:disabled {
                background-color: #555555;
                color: #aaaaaa;
            }
            QPushButton:hover {
                background-color: #0055aa;
            }
        """)

    def toggleAutoDetect(self):
        auto_detect = self.autoDetectCheckBox.isChecked()
        self.radioGroupBox.setEnabled(not auto_detect)

    def get_selected_hash_type(self):
        if self.autoDetectCheckBox.isChecked():
            hashvalue = self.hashInput.text()
            length = len(hashvalue)
            if length == 32:
                return 'md5'
            elif length == 40:
                return 'sha1'
            elif length == 64:
                return 'sha256'
            elif length == 96:
                return 'sha384'
            elif length == 128:
                return 'sha512'
            else:
                QMessageBox.warning(self, 'Hash Error', 'Cannot auto-detect hash type. Please select manually.')
                return None
        else:
            if self.md5Radio.isChecked():
                return 'md5'
            elif self.sha1Radio.isChecked():
                return 'sha1'
            elif self.sha256Radio.isChecked():
                return 'sha256'
            elif self.sha384Radio.isChecked():
                return 'sha384'
            elif self.sha512Radio.isChecked():
                return 'sha512'
            else:
                return None

    def decrypt(self):
        hashvalue = self.hashInput.text()
        hashtype = self.get_selected_hash_type()

        if not hashvalue:
            QMessageBox.warning(self, 'Input Error', 'Please enter a hash value.')
            return

        if hashtype == 'md5':
            result = self.md5crack(hashvalue)
        elif hashtype:
            result = self.decrypter(hashvalue, hashtype)
        else:
            return

        if result:
            self.resultDisplay.setText(result)
            self.copyButton.setEnabled(True)
        else:
            self.resultDisplay.setText('Hash was not found in the database.')
            self.copyButton.setEnabled(False)

    def md5crack(self, hashvalue):
        try:
            r = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
            if r:
                return r
            else:
                return 'Hash was not found in the database.'
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Request Error', 'Error during request: ' + str(e))
            return None

    def decrypter(self, hashvalue, hashtype):
        try:
            r = requests.get(
                'https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=cybercroc@protonmail.com&code=c5ddc9bbd5b07c45' % (hashvalue, hashtype)).text
            if r:
                return r
            else:
                return 'Hash was not found in the database.'
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'Request Error', 'Error during request: ' + str(e))
            return None

    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.resultDisplay.text())
        QMessageBox.information(self, 'Copied', 'Result copied to clipboard.')

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = HashDecryptionGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
