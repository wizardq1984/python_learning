import wx


class TicTac(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='Tic Tac Toe', size=(400, 400))
        self.CreateStatusBar()

        # setup menu
        menu_menu = wx.Menu()
        menu_game = wx.Menu()
        # setup menu list items
        man_on_man = menu_game.Append(wx.ID_ANY, 'Man on Man', 'Start a game with your friend.')
        man_on_ai = menu_game.Append(wx.ID_ANY, 'Man on AI', 'Start a game with AI.')
        menu_menu.Append(wx.ID_ANY, 'New Game', menu_game)
        menu_menu.AppendSeparator()
        menu_exit = menu_menu.Append(wx.ID_EXIT, 'Exit', 'Exit this game and close the window.')
        # Setup event bind
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)
        # self.Bind(wx.EVT_MENU, self.game_button, man_on_man)
        # self.Bind(wx.EVT_MENU, self.game_button, man_on_ai)

        # setup game menu
        game_menu = wx.Menu()
        # setup game menu list items
        game_undo = game_menu.Append(wx.ID_ANY, 'Undo', 'Undo 1 step for current player.')
        game_menu.AppendSeparator()
        game_startnew = game_menu.Append(wx.ID_ANY, 'Start new game', 'Start new game')

        # setup help menu
        help_menu = wx.Menu()
        # setup help menu items
        help_about = help_menu.Append(wx.ID_ABOUT, 'About', 'About this Game.')
        # setup bind event
        self.Bind(wx.EVT_MENU, self.on_about, help_about)

        # setup menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(menu_menu, 'Menu')
        menu_bar.Append(game_menu, 'Game')
        menu_bar.Append(help_menu, 'Help')
        self.SetMenuBar(menu_bar)

        self.board = wx.Panel(self)
        self.btn1 = wx.Button(self.board, size=(100, 100))
        self.btn2 = wx.Button(self.board, size=(100, 100))
        self.btn3 = wx.Button(self.board, size=(100, 100))
        self.btn4 = wx.Button(self.board, size=(100, 100))
        self.btn5 = wx.Button(self.board, size=(100, 100))
        self.btn6 = wx.Button(self.board, size=(100, 100))
        self.btn7 = wx.Button(self.board, size=(100, 100))
        self.btn8 = wx.Button(self.board, size=(100, 100))
        self.btn9 = wx.Button(self.board, size=(100, 100))
        self.sizers = wx.GridSizer(3, 3, 5, 5)
        self.sizers.Add(self.btn1, 0, wx.EXPAND)
        self.sizers.Add(self.btn2, 0, wx.EXPAND)
        self.sizers.Add(self.btn3, 0, wx.EXPAND)
        self.sizers.Add(self.btn4, 0, wx.EXPAND)
        self.sizers.Add(self.btn5, 0, wx.EXPAND)
        self.sizers.Add(self.btn6, 0, wx.EXPAND)
        self.sizers.Add(self.btn7, 0, wx.EXPAND)
        self.sizers.Add(self.btn8, 0, wx.EXPAND)
        self.sizers.Add(self.btn9, 0, wx.EXPAND)
        self.btn1.Bind(wx.EVT_BUTTON, self.on_click1)

        self.board.SetSizer(self.sizers)
        self.sizers.Fit(self)

        self.Show(True)

    def on_click1(self, event):
        self.btn1.SetLabel('btn1 test')
        test_list[0] = 1
        print(test_list)

    def on_about(self, event):
        dlg = wx.MessageDialog(self, 'Game made by Kingwizard for Python learning.', 'About this Game', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_exit(self, event):
        self.Close(True)


test_list = [0]*9


if __name__ == '__main__':
    app = wx.App(False)
    frame = TicTac(None)
    app.MainLoop()
