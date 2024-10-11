import wx
import csv

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="ListCtrl with Subitems")

        # Main List Control
        self.main_list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.main_list.InsertColumn(0, "Main Item")
        self.main_list.InsertItem(0, "Item 1")
        self.main_list.InsertItem(1, "Item 2")

        # Sub List Control
        self.sub_list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.sub_list.InsertColumn(0, "Sub Item")
        self.sub_list.Hide()  # Start hidden

        # Sub-items stored directly
        self.sub_items_for_item_1 = ["Sub Item 1.1", "Sub Item 1.2"]

        # Export Button
        self.export_button = wx.Button(self, label="Export to CSV")
        self.export_button.Bind(wx.EVT_BUTTON, self.on_export)

        # Bind event to the main list
        self.main_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.main_list, 1, wx.EXPAND)
        sizer.Add(self.sub_list, 1, wx.EXPAND)
        sizer.Add(self.export_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(sizer)
        self.Show()

        # Initialize sub list for Item 1
        self.populate_sub_list()

    def populate_sub_list(self):
        """Populate the sub list for Item 1."""
        self.sub_list.DeleteAllItems()
        for sub_item in self.sub_items_for_item_1:
            self.sub_list.InsertItem(self.sub_list.GetItemCount(), sub_item)
        self.sub_list.Show()

    def on_item_selected(self, event):
        self.sub_list.DeleteAllItems()
        selected_index = event.GetIndex()

        if selected_index == 0:  # Item 1 selected
            self.populate_sub_list()  # Show sub-items for Item 1
        else:  # Item 2 selected
            self.sub_list.Hide()  # Hide sub list

        self.Layout()  # Refresh layout

    def on_export(self, event):
        with wx.FileDialog(self, "Save CSV file", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_OK:
                path = file_dialog.GetPath()
                self.export_to_csv(path)

    def export_to_csv(self, path):
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow(["Main Item", "Sub Item"])

            # Always write Item 1 and its stored sub-items
            main_item_1 = self.main_list.GetItemText(0)
            for sub_item in self.sub_items_for_item_1:
                writer.writerow([main_item_1, sub_item])

            # Write Item 2 with empty sub-item
            main_item_2 = self.main_list.GetItemText(1)
            writer.writerow([main_item_2, ""])  # No sub items for Item 2

        wx.MessageBox("Exported successfully!", "Info", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()