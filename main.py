# Before running
# ---- pip install PyQt6 ----
# See More: https://medium.com/analytics-vidhya/how-to-build-your-first-desktop-application-in-python-7568c7d74311

import sys
import os

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtGui import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

QQuickWindow.setSceneGraphBackend('software')

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')

sys.exit(app.exec())

#Add to main.qml:
#import QtQuick
#import QtQuick.Controls.Basic

#ApplicationWindow {
#    visible: true
#    width: 600
#    height: 500
#    title: "HelloApp"
#
#    Text{
#        anchors.centerIn: parent
#        text: "Hello World"
#        font.pixelSize: 24
#    }
#}