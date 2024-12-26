import tkinter as tk

def fix_window(root, width=300, height=369):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# Functions to manage hovering on MENU elements (topbar)
def on_enter_menu(e, page, widget_page):
    # Hover only if the widget is not selected
    if page != widget_page:
        if not hasattr(e.widget, "original_bg"):
            e.widget.original_bg = e.widget.cget("bg")
        e.widget.config(bg="#ebdbb2", cursor="@res/hand.cur")

def on_leave_menu(e, page, widget_page):
    # Restore original color only if the widget is not selected
    if page != widget_page:
        e.widget.config(bg=e.widget.original_bg)

# hovering everywhere else
def on_enter(e):
    # Save original attribute to restore on_leave
    if not hasattr(e.widget, "original_bg"):
        e.widget.original_bg = e.widget.cget("bg")
    e.widget.config(bg="#ebdbb2", cursor="@res/hand.cur")

def on_leave(e):
    e.widget.config(bg=e.widget.original_bg)  # Restore original color

def create_gui(root, page, set_page):
    root.title("spruceUI Control Panel")

    root.resizable(False, False)

    # Set app background color
    root.configure(bg="#282828")

    # Set app icon
    icon = tk.PhotoImage(file="res/icon.png")
    root.iconphoto(False, icon)

    # Keep references to images to avoid garbage collection
    root.device_image = tk.PhotoImage(file="res/miyooa30.png")
    root.settings_image = tk.PhotoImage(file="res/settings-uns.png")
    root.sd_image = tk.PhotoImage(file="res/sd.png")
    root.connect_image = tk.PhotoImage(file="res/connect.png")

    def on_icon_click(new_page):
        set_page(new_page)  # Use the set_page function from main.py

    def generate_top_bar():
        topbar_container = tk.Frame(root, bg="#242424", height=25, pady=0)
        topbar_container.pack(side='top', fill="x", padx=0)

        selected_col = "#323232"
        unselected_col = "#242424"

        # Section we'll use to change between different devices
        device_icon = tk.Label(topbar_container, bg=unselected_col, image=root.device_image)
        device_icon.pack(side="left")
        device_icon.bind("<Enter>", lambda e: on_enter_menu(e, page, "device"))
        device_icon.bind("<Leave>", lambda e: on_leave_menu(e, page, "device"))

        # Icons attached to the right are the app icons
        settings_icon = tk.Label(topbar_container, bg=selected_col if page == "settings" else unselected_col, image=root.settings_image)
        sd_icon = tk.Label(topbar_container, bg=selected_col if page == "sd" else unselected_col, image=root.sd_image)
        connect_icon = tk.Label(topbar_container, bg=selected_col if page == "connect" else unselected_col, image=root.connect_image)

        # Assign callbacks to click events
        settings_icon.bind("<Button-1>", lambda e: on_icon_click("settings"))
        sd_icon.bind("<Button-1>", lambda e: on_icon_click("sd"))
        connect_icon.bind("<Button-1>", lambda e: on_icon_click("connect"))

        settings_icon.pack(side="right", padx=0)
        settings_icon.bind("<Enter>", lambda e: on_enter_menu(e, page, "settings"))
        settings_icon.bind("<Leave>", lambda e: on_leave_menu(e, page, "settings"))

        sd_icon.pack(side="right", padx=0)
        sd_icon.bind("<Enter>", lambda e: on_enter_menu(e, page, "sd"))
        sd_icon.bind("<Leave>", lambda e: on_leave_menu(e, page, "sd"))

        connect_icon.pack(side="right", padx=0)
        connect_icon.bind("<Enter>", lambda e: on_enter_menu(e, page, "connect"))
        connect_icon.bind("<Leave>", lambda e: on_leave_menu(e, page, "connect"))

    generate_top_bar()