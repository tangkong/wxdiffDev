####################################################################################
### Convert Dexela format tif to raw
### Python 2.7 (uses xrange)
### Date: 1/25/2018
### Author: Robert Tang-Kong
### Version: 0.2
####################################################################################


import wx, wxdiff_api
import numpy as np
from diffimagewindow import DiffImageWindow
import os
import sys
from os.path import basename
import struct

try:
    # grab original path to reset later
    dexelaPath = os.getcwd()
    # prompt for file to convert
    dlg = wx.FileDialog(
            MDIRoot, message="Choose a Dexela tif Image to convert",
            style=wx.FD_OPEN
            )
    dlg.ShowModal()
    dlg.Destroy()
    filename = dlg.GetPath()

    # Open file
    im = open(filename, 'rb')
    im.seek(8) # remove first 8 bytes of header
    arr = [] 
    for i in range(int(23887872/2)): # Count knowing image size apriori
        try:
            buff = struct.unpack_from("<H",im.read(2))[0]
            arr.append(buff)
            # `<` means little endian; `H` means unsigned short aka int16 (2 bytes) 
        except Exception as e:
            print('error occured')
            print(e)
            break

    nparr = np.array(arr)
    print(nparr.shape)
    print(nparr.dtype)
    dlgSave = wx.FileDialog(
            MDIRoot, message="Save as .raw",
            style=wx.FD_SAVE
            )
    dlgSave.ShowModal()
    dlgSave.Destroy()
    fileSavePath = dlgSave.GetPath()

    nparr.astype('int16').tofile(fileSavePath)

    wx.MessageBox("Open new file as .raw/.bin file.  Data type is \"16 bit integer\", image size is 3072px x 3888px")

except Exception as e:
    print('failure, resetting path')
    print(e)