import wx
import wx.grid

from .dialog_base import LengthMatchingDialog, CreatePanel, DisplayPanel

class DialogMain(LengthMatchingDialog):
    def __init__(self, parent, version, data):
        LengthMatchingDialog.__init__(self, parent)
        self.SetTitle('Length Matching %s' % version)
        self.board = data.board

        self.createPanel = CreatePanel(self.notebook)
        self.displayPanel = DisplayPanel(self.notebook)
        self.notebook.AddPage(self.createPanel, "Create Class")
        self.notebook.AddPage(self.displayPanel, "Display")
    
    def SetSizeHints(self, a, b, c=None):
        if c is not None:
            super(wx.Dialog, self).SetSizeHints(a,b,c)
        else:
            super(wx.Dialog, self).SetSizeHintsSz(a,b)

    def OnUpdateClick(self, event):
        self.labelStatus.LabelText = 'OnUpdate Pressed'
    
    def OnSaveClick(self, event):
        self.labelStatus.LabelText = 'OnSave Pressed'






