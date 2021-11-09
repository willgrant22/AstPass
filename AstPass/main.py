import wx
import AstPass as ap

class Main(wx.App):
    def OnInit(self):
        self.frame = ap.App(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    main = Main(0)
    main.MainLoop()