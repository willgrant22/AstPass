import wx
# noinspection PyPep8Naming
import AstPass as ap


# noinspection PyAttributeOutsideInit
class Main(wx.App):
    def OnInit(self):
        self.frame = ap.App(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# Beginning of main
if __name__ == '__main__':
    main = Main(0)
    main.MainLoop()
