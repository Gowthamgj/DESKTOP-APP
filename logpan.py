import wx
class LoginPanel(wx.Panel):
    def __init__(selfself,parent):
        wx.panel.__init__(self.parent=parent)
        self.box=wx.BoxSizer(wx.VERTICAL)
        self.box.AddSpacer(30)
        Login_label=wx.StaticText(self,wx.ID_ANY),""