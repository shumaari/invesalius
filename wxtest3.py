import wx
from wx.lib.agw.hypertreelist import HyperTreeList

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="HyperTreeList Example", size=(600, 400))

        # Create a HyperTreeList
        self.tree = HyperTreeList(self, style= wx.TR_HIDE_ROOT)

        # Add columns
        self.tree.AddColumn("Items")

        # Add a single root with categories
        category1 = self.tree.AddRoot("Category 1")
        self.tree.AppendItem(category1, "Item 1A")
        a = self.tree.AppendItem(category1, "Item 1B")

        self.tree.AppendItem(a, "Item 2A")
        self.tree.AppendItem(a, "Item 2B")

        # Expand categories
        self.tree.Expand(category1)

        # Set the sizer for layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

        # Show the frame
        self.Show()

app = wx.App(False)
frame = MyFrame()
app.MainLoop()