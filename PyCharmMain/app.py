import eel
import os
from files import filesFun
from pyqadmin import admin
from learning import callNewNeroModel
from audioProccessing import audioProc


eel.init("web")
@admin
@eel.expose #декортаор позволяет запускать функции питона внутри js
def reinitFiles():
    filesFun()

@eel.expose
def addLearnMach():
    callNewNeroModel()

@eel.expose
def audioProcjs(pathToFile):
    print(pathToFile)
    audioProc(pathToFile)




eel.start("layout.html", size = (600,400))

