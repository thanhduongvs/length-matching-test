# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class LengthMatchingDialog
###########################################################################

###########################################################################
## Class LengthMatchingDialog
###########################################################################

class LengthMatchingDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Length Matching", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP|wx.BORDER_DEFAULT )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		boxNotebook = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_TOP|wx.BORDER_DEFAULT )

		boxNotebook.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

		self.labelStatus = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelStatus.Wrap( -1 )

		boxNotebook.Add( self.labelStatus, 0, wx.ALL, 5 )

		boxButton = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonUpdate = wx.Button( self, wx.ID_ANY, u"Update from Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButton.Add( self.buttonUpdate, 0, wx.ALL, 5 )


		boxButton.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonSave = wx.Button( self, wx.ID_ANY, u"Save Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButton.Add( self.buttonSave, 0, wx.ALL, 5 )


		boxNotebook.Add( boxButton, 0, wx.EXPAND, 5 )


		self.SetSizer( boxNotebook )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.buttonUpdate.Bind( wx.EVT_BUTTON, self.OnUpdateClick )
		self.buttonSave.Bind( wx.EVT_BUTTON, self.OnSaveClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnUpdateClick( self, event ):
		event.Skip()

	def OnSaveClick( self, event ):
		event.Skip()



###########################################################################
## Class CreatePanel
###########################################################################

class CreatePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass

###########################################################################
## Class DisplayPanel
###########################################################################

class DisplayPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass

