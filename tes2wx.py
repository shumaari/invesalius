import wx
import wx.dataview as dv

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython TreeListCtrl with Columns and Subitems", size=(500, 400))
        panel = wx.Panel(self)

        # Create TreeListCtrl
        tree_list_ctrl = dv.TreeListCtrl(panel, style=wx.TR_MULTIPLE | wx.TR_FULL_ROW_HIGHLIGHT)

        # Add columns
        tree_list_ctrl.AppendColumn("Column 1")
        tree_list_ctrl.AppendColumn("Column 2")
        tree_list_ctrl.AppendColumn("Column 3")

        # Add root item
        root = tree_list_ctrl.GetRootItem()

        # Add data to the tree list control
        for i in range(1, 4):
            item = tree_list_ctrl.AppendItem(root, f"Item {i}")
            tree_list_ctrl.SetItemText(item, 1, f"Subitem {i}-2")
            tree_list_ctrl.SetItemText(item, 2, f"Subitem {i}-3")
            for j in range(1, 4):
                sub_item = tree_list_ctrl.AppendItem(item, f"Subitem {i}-{j}-1")
                tree_list_ctrl.SetItemText(sub_item, 1, f"{i}-{j}-2")
                tree_list_ctrl.SetItemText(sub_item, 2, f"{i}-{j}-3")

        # Resize columns to fit content
        tree_list_ctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        tree_list_ctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        tree_list_ctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)

        # Layout using sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(tree_list_ctrl, 1, wx.EXPAND)
        panel.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()