from close import authenticate_user
import wx

class MainPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)
        self.parent=parent
        self.box=wx.BoxSizer(wx.VERTICAL)
        self.box.AddSpacer(30)
        login_label=wx.StaticText(self,wx.ID_ANY,"please login to continue")

        self.box.Add(login_label,0,flag=wx.ALIGN_CENTER)
        login_form=wx.FlexGridSizer(rows=3,cols=2,hgap=5,vgap=25)
        username_label=wx.StaticText(self,wx.ID_ANY,"username")
        password_label = wx.StaticText(self, wx.ID_ANY, "password")
        self.username_text=wx.TextCtrl(self,size=(170,-1))
        self.password_text=wx.TextCtrl(self,size=(170,-1),style=wx.TE_PASSWORD)
        login_button=wx.Button(self,wx.ID_ANY,"login")
        #login_button.Bind(wx.EVT_BUTTON)
        login_form.Add(username_label,0,wx.LEFT,0)
        login_form.Add(self.username_text,0,wx.LEFT,50)
        login_form.Add(password_label,0,wx.LEFT,0)
        login_form.Add(self.password_text,0,wx.LEFT,50)
        login_form.Add(login_button,0,wx.LEFT,50)
        self.box.AddSpacer(200)
        self.box.Add(login_form,0,flag=wx.ALIGN_LEFT)
        self.SetSizer(self.box)
    def Login_button_clicked(self,event):
        username = self.username_text.GetValue
        password=self.password_text.GetValue
        if not authenticate_user(username,password):
            dialogue=wx.MessageDialog(self,"Invalid cred","Invaliduname",wx.OK)
            dialogue.ShowModal()
            dialogue.Bind(wx.OK, self.Destroy())
            dialogue.Destroy()
