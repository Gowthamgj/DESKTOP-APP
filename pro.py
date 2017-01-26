import wx
from panels import MainPanel

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent)
        self.Login_panel=MainPanel(self)
        #self.second_panel=SecondPanel(self)
        self.Bind(wx.EVT_CLOSE,self.on_close)
        self.Show()
    def hide_all(self):
        self.login_panel.Hide()
        self.second_panel.Hide()

    def on_close(self,event):
        try:
            dialogue=wx.MessageDialog(self,"Do you want to close?","close window",wx.OK)
            dialogue.ShowModal()
            dialogue.Bind(wx.OK,self.Destroy())
            dialogue.Destroy()
        except Exception as e:
            print "exception"
            print e
app = wx.App(False)
frame = MainFrame(None, "Sample application")
app.MainLoop()