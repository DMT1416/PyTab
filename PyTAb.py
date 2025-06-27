import wx
import wikipedia
import string

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(500, 300),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyTab")
        
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="""Hi, This is PyTab. Type any name, 
place, or topic to instantly get a short summary. 
How can I help you today?""")
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        lbl.SetFont(font)
        my_sizer.Add(lbl, 0, wx.ALL, 5)

        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(500, 30))
        font_input = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.txt.SetFont(font_input)
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.on_enter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)

        self.output_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY , size=(500, 150))
        font_output = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.output_box.SetFont(font_output)
        my_sizer.Add(self.output_box, 1, wx.ALL | wx.EXPAND, 5)


        panel.SetSizer(my_sizer)
        self.Show()

    def on_enter(self, event):
        input_text = self.txt.GetValue().strip().lower()
        input_text = input_text.translate(str.maketrans("", "", string.punctuation))
        try:
            summary = wikipedia.summary(input_text, sentences=2)
            self.output_box.SetValue(summary)
        except Exception as e:
            self.output_box.SetValue("Sorry, I couldn't find anything about that.")

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
