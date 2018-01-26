####################################################################################
### Convert Dexela format tif to raw
### Python 2.7 (uses xrange)
### Date: 1/25/2018
### Author: Robert Tang-Kong
### Version: 0.1
####################################################################################


import wx, wxdiff_api
import numpy as np
from diffimagewindow import DiffImageWindow
import os
import sys
from os.path import basename

from PIL import Image

try:
    dexelaPath = os.getcwd()
    dlg = wx.FileDialog(
            MDIRoot, message="Choose a Dexela tif Image to convert",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
    dlg.ShowModal()
    dlg.Destroy()
    filename = dlg.GetPath()

    # Import using Image pkg
    imDx = Image.open(filename)
    # Cast to array, dtype int16, save as raw
    imDxarr = np.array(imDx.getdata())

    dlgSave = wx.FileDialog(
            MDIRoot, message="Save as .raw",
            style=wx.FD_SAVE | wx.FD_CHANGE_DIR
            )
    dlgSave.ShowModal()
    dlgSave.Destroy()
    fileSavePath = dlgSave.GetPath()

    imDxarr.astype('int16').tofile(fileSavePath)

    wx.MessageBox("Open new file as .raw/.bin file.  Data type is \"16 bit integer\", image size is 3072px x 3888px")
    os.chdir(dexelaPath)

except Exception as e:
    print('failure, resetting path')
    os.chdir(dexelaPath)
    print(e)