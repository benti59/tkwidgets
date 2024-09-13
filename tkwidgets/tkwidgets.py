from tkinter import *
from windnd import hook_dropfiles


class HyperlinkLabel(Label):
    r"""
    这是一个继承自标签控件的自定义控件，实现了名为超链接的特殊功能
    Args:
        master：父控件
        text：要显示的文本
        font：显示文本的字体
        cursor：鼠标悬停的样式，默认为掌型
        command\url 绑定的回调函数，command和url只能指定一个，一个表示执行的函数，一个表示跳转的网页
        hover_fg：表示鼠标悬停时该控件的前景颜色
        font_style：显示字符的样式，列如加粗、下划线
        **kwargs: 传入Frame控件的关键字参数。
    """
    DEFAULT_HOVER_FG = "blue"
    DEFAULT_CURSOR = "hand2"
    DEFAULT_FONT_STYLE = "normal"

    def __init__(
            self,
            master=None,
            text: str = "",
            font: tuple = ("楷体", 12),
            cursor: str = DEFAULT_CURSOR,
            command=None,
            url: str = None,
            hover_fg: str = DEFAULT_HOVER_FG,
            font_style: str = DEFAULT_FONT_STYLE,
            **kwargs
    ):
        super().__init__(master, **kwargs)

        if command is not None and url is not None:
            raise ValueError("command and url cannot be set simultaneously")
        if len(font) > 2:
            raise ValueError(f"font={font} Parameter {font[2]} cannot be applied")

        self.command = command
        self.url = url
        self.hover_fg = hover_fg
        self.previous_fg = None
        self.config(text=text, font=(font[0], font[1], font_style), cursor=cursor)

        # 绑定事件
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_click(self, event):
        """处理点击事件"""
        if self.url:
            import webbrowser
            webbrowser.open(self.url)
        elif self.command:
            self.command()

    def on_enter(self, event):
        """处理鼠标悬停事件"""
        self.previous_fg = self["fg"]
        self.config(fg=self.hover_fg)

    def on_leave(self, event):
        """处理鼠标离开事件"""
        if self.previous_fg != self["fg"]:
            self.config(fg=self.previous_fg)


class DragDropFrame(Frame):
    """
    一个支持拖拽文件的框架控件。
    Args:
        master：父控件
        text：要显示的文本
        font：显示文本的字体
        borderwidth: 边框宽度
        relief: 边框样式 (flat, raised, sunken, groove, ridge)
        bg: 背景颜色
        fg: 前景颜色
        drop_callback: 拖拽文件时的回调函数
        **kwargs: 传入Frame控件的关键字参数。
    """
    def __init__(
            self,
            master=None,
            text="",
            font=("楷体", 12),
            borderwidth=2,
            relief="groove",
            bg="white",
            fg="black",
            drop_callback=None,
            **kwargs
    ):
        super().__init__(master, borderwidth=borderwidth, relief=relief, bg=bg, **kwargs)
        self.drop_callback = drop_callback
        self.label = Label(self, text=text, font=font, borderwidth=borderwidth, relief=relief, bg=bg, fg=fg)
        self.label.pack(fill=BOTH, expand=True, padx=borderwidth, pady=borderwidth)

        # 绑定拖拽事件
        hook_dropfiles(self, func=self.on_drop)

    def on_drop(self, files):
        """处理拖拽事件"""
        file_paths = [file.decode("gbk") for file in files][0].replace("\\", "/")
        if self.drop_callback:
            self.drop_callback(file_paths)


class DragDropLabelFrame(LabelFrame):
    """
    一个支持拖拽文件的框架控件。
    Args:
        master：父控件
        text_label：中间标签要显示的文本
        font_label：标签显示文本的字体
        bg: 背景颜色
        fg: 前景颜色
        drop_callback: 拖拽文件时的回调函数
        **kwargs: 传入LabelFrame控件的关键字参数。
    """
    def __init__(
            self,
            master=None,
            text_label="",
            font_label=("楷体", 12),
            bg="white",
            fg="black",
            drop_callback=None,
            **kwargs
    ):
        super().__init__(master,text="", font=("楷体", 12), bg=bg, **kwargs)
        self.drop_callback = drop_callback
        self.label = Label(self, text=text_label, font=font_label, bg=bg, fg=fg)
        self.label.pack(fill=BOTH, expand=True)

        # 绑定拖拽事件
        hook_dropfiles(self, func=self.on_drop)

    def on_drop(self, files):
        """处理拖拽事件"""
        file_paths = [file.decode("gbk") for file in files][0].replace("\\", "/")
        if self.drop_callback:
            self.drop_callback(file_paths)
