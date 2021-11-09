import wx
# noinspection PyPep8Naming
import AstPass as ap


# noinspection PyPep8Naming,PyUnusedLocal
class App(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style",
                                 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("AstPass")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridBagSizer(10, 5)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 1)

        grid_sizer_1.Add(0, 15, (0, 6), (1, 1), wx.EXPAND, 0)

        grid_sizer_1.Add(10, 0, (1, 0), (1, 1), wx.EXPAND, 0)

        static_text_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "  Password ")
        grid_sizer_1.Add(static_text_1, (1, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        self.main_text_ctrl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_LEFT | wx.TE_RICH2)
        self.main_text_ctrl.SetMaxLength(120)
        grid_sizer_1.Add(self.main_text_ctrl, (1, 2), (1, 8), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        grid_sizer_1.Add(20, 0, (1, 10), (1, 1), wx.EXPAND, 0)

        static_text_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Length ")
        grid_sizer_1.Add(static_text_2, (2, 1), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        self.length_spin = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "8", min=8, max=120,
                                       style=wx.ALIGN_LEFT | wx.SP_ARROW_KEYS)
        grid_sizer_1.Add(self.length_spin, (2, 2), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.symbols_checkbox = wx.CheckBox(self.panel_1, wx.ID_ANY, "Symbols  ", style=wx.CHK_2STATE)
        grid_sizer_1.Add(self.symbols_checkbox, (2, 5), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.numbers_checkbox = wx.CheckBox(self.panel_1, wx.ID_ANY, "Numbers ", style=wx.CHK_2STATE)
        grid_sizer_1.Add(self.numbers_checkbox, (2, 6), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.uppercase_checkbox = wx.CheckBox(self.panel_1, wx.ID_ANY, "Uppercase", style=wx.CHK_2STATE)
        grid_sizer_1.Add(self.uppercase_checkbox, (2, 7), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.lowercase_checkbox = wx.CheckBox(self.panel_1, wx.ID_ANY, "Lowercase", style=wx.CHK_2STATE)
        grid_sizer_1.Add(self.lowercase_checkbox, (2, 8), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        self.all_toggle = wx.ToggleButton(self.panel_1, wx.ID_ANY, "All ")
        grid_sizer_1.Add(self.all_toggle, (2, 9), (1, 1), wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        sizer_2 = wx.GridBagSizer(0, 10)
        grid_sizer_1.Add(sizer_2, (3, 7), (2, 3), wx.ALL | wx.EXPAND, 0)

        self.submit_button = wx.Button(self.panel_1, wx.ID_ANY, "Submit ", style=wx.BU_AUTODRAW)
        self.submit_button.Bind(wx.EVT_BUTTON, lambda event: self.onSubmit(event, self.length_spin.GetValue(),
                                                                           self.symbols_checkbox.GetValue(),
                                                                           self.numbers_checkbox.GetValue(),
                                                                           self.uppercase_checkbox.GetValue(),
                                                                           self.lowercase_checkbox.GetValue()))
        self.submit_button.SetDefault()
        sizer_2.Add(self.submit_button, (0, 0), (1, 1), wx.EXPAND, 0)

        self.clear_button = wx.Button(self.panel_1, wx.ID_ANY, "Clear ", style=wx.BU_AUTODRAW)
        self.clear_button.Bind(wx.EVT_BUTTON, self.onClear)
        sizer_2.Add(self.clear_button, (0, 1), (1, 1), wx.EXPAND, 0)

        grid_sizer_1.Add(0, 20, (4, 10), (1, 1), wx.EXPAND, 0)

        sizer_2.AddGrowableRow(0)
        sizer_2.AddGrowableCol(0)
        sizer_2.AddGrowableCol(1)

        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableRow(2)
        grid_sizer_1.AddGrowableRow(3)
        grid_sizer_1.AddGrowableRow(4)

        self.panel_1.SetSizer(sizer_1)

        sizer_1.Fit(self)
        self.Layout()
        self.Centre()

    # Submit button event
    @staticmethod
    def onSubmit(event, Length: int, Symbols: bool, Numbers: bool, Uppercase: bool, Lowercase: bool):
        # Initializing dataclass instance
        control_state = ap.CurrentState(Length, Symbols, Numbers, Uppercase, Lowercase)
        # Initializing Password class & object instance
        pVar = ap.Password()
        print(control_state)

    # Clear button event
    def onClear(self, event):
        pass
# ToDo create window focus function
