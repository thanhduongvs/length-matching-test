import wx
import wx.grid

from . import dialog_base

class DialogMain(dialog_base.LengthMatchingDialog):
    def __init__(self, parent, version, data):
        dialog_base.LengthMatchingDialog.__init__(self, parent)
        self.SetTitle('Length Matching %s' % version)
        self.board = data.board
    
    def SetSizeHints(self, a, b, c=None):
        if c is not None:
            super(wx.Dialog, self).SetSizeHints(a,b,c)
        else:
            super(wx.Dialog, self).SetSizeHintsSz(a,b)


