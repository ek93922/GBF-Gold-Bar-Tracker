import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
import sqlite3
import os


root = Tk()
root.title("Gold Bar Tracker v1.0 by Aria")
root.geometry("550x210")
root.resizable(False, False)

# -------------------------------------------------------------#
    # Creating custom style

# Set hex value of colors 
discord = "#36393F"
lighter_discord = "#747474"

style = ttk.Style()

style.theme_create(
    "darkmode",
    settings={
        "TNotebook": {"configure": {"background": discord}},
        "TNotebook.Tab": {
            "configure": {
                "padding": [7, 4],
                "background": discord,
                "foreground": "white",
            },
            "map": {"background": [("selected", lighter_discord)]},
        },
    },
)

style.theme_use("darkmode")

# -------------------------------------------------------------#

# Adds Frames to the root window
notebook = ttk.Notebook(root)
simple_tab = Frame(notebook, bg=discord)
detail_tab = Frame(notebook, bg=discord)

# Adds tabs at the top left of the window to swap frame views
notebook.add(simple_tab, text="Gold Bar Tracker")
notebook.add(detail_tab, text="Detailed Report")
notebook.pack(expand=True, fill="both")

# -------------------------------------------------------------#

# Databases

# Create a database or connect to one
conn = sqlite3.connect("drop_table.db")

# Create a cursor
c = conn.cursor()

# Create a table to store current data
c.execute(
    """CREATE TABLE IF NOT EXISTS current_data (
        misc integer,
        t1 integer,
        t2 integer,
        t3 integer,
        goldbar integer,
        raids_joined integer,
        total_gb integer
        )"""
)

# Create a table that keeps track of gb drops
c.execute(
    """CREATE TABLE IF NOT EXISTS data_table (
        totalgb int,
        time text,
        misc integer,
        t1 integer,
        t2 integer,
        t3 integer,
        raids_joined integer
        )"""
)

c.execute("SELECT * FROM current_data ORDER BY ROWID DESC")
data = c.fetchone()


# Define Values
date = datetime.now().strftime("%m/%d/%Y | %H:%M")

try:
    misc_count = data[0]
    t1_count = data[1]
    t2_count = data[2]
    t3_count = data[3]
    gb_count = data[4]
    raid_count = data[5]
    gb_total = data[6]

except TypeError:
    misc_count = 0
    t1_count = 0
    t2_count = 0
    t3_count = 0
    gb_count = 0
    raid_count = 0
    gb_total = 0

    # Insert into table
    c.execute(
        """INSERT INTO current_data VALUES (
            :misc, 
            :t1, 
            :t2, 
            :t3, 
            :goldbar, 
            :raids_joined, 
            :total_gb)""",
        {
            "misc": misc_count,
            "t1": t1_count,
            "t2": t2_count,
            "t3": t3_count,
            "goldbar": gb_count,
            "raids_joined": raid_count,
            "total_gb": gb_total,
        },
    )

# Commit Changes
conn.commit()

# Close Connection
conn.close()


# -------------------------------------------------------------#

# Database Update
def update():
    global misc_count
    global t1_count
    global t2_count
    global t3_count
    global gb_count
    global raid_count
    global gb_total

    # Create a database or connect to one
    conn = sqlite3.connect("drop_table.db")

    # Create a cursor
    c = conn.cursor()
    c.execute(
        """UPDATE current_data SET
        misc = :misc,
        t1 = :t1,
        t2 = :t2,
        t3 = :t3,
        goldbar = :goldbar,
        raids_joined = :raids_joined,
        total_gb = :total_gb

        WHERE ROWID=1""",
        {
            "misc": misc_count,
            "t1": t1_count,
            "t2": t2_count,
            "t3": t3_count,
            "goldbar": gb_count,
            "raids_joined": raid_count,
            "total_gb": gb_total
        },
    )
    conn.commit()
    conn.close()


# -------------------------------------------------------------#

# Sets the Folder the Script is Executed as Root/Base Folder
dirname = os.path.dirname(__file__)

# Set application icon
root.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "gb.ico"))))

# Import needed Images with Relative File Path
gb = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "Gold_Brick.png")))
t1_ring = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "T1_Ring.png")))
t2_ring = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "T2_Ring.png")))
t3_ring = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "T3_Ring.png")))
misc = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "trashdrop.png")))
raid = ImageTk.PhotoImage(Image.open(os.path.join(dirname, "Icons", "raidicon.png")))
# -------------------------------------------------------------#


# -------------------------------------------------------------#


class math:
    def add():
        # Increase Raid Count value and updates display
        global raid_count
        raid_count += 1
        raid_display.config(text=str(raid_count))

    def subtract():
        # Decrease Raid Count value and updates display
        global raid_count
        if raid_count == 0:
            None
        else:
            raid_count -= 1

        raid_display.config(text=str(raid_count))

    def misc_calc():
        global misc_count
        global raid_count
        if raid_count == 0:
            misc_rate.config(text=f"{0:.2f}" + "%")
        else:
            misc_percent = (misc_count / raid_count) * 100
            misc_rate.config(text=f"{misc_percent:.2f}" + "%")

    def t1_calc():
        global t1_count
        global raid_count
        if raid_count == 0:
            t1_rate.config(text=f"{0:.2f}" + "%")
        else:
            t1_percent = (t1_count / raid_count) * 100
            t1_rate.config(text=f"{t1_percent:.2f}" + "%")

    def t2_calc():
        global t2_count
        global raid_count
        if raid_count == 0:
            t2_rate.config(text=f"{0:.2f}" + "%")
        else:
            t2_percent = (t2_count / raid_count) * 100
            t2_rate.config(text=f"{t2_percent:.2f}" + "%")

    def t3_calc():
        global t3_count
        global raid_count
        if raid_count == 0:
            t3_rate.config(text=f"{0:.2f}" + "%")
        else:
            t3_percent = (t3_count / raid_count) * 100
            t3_rate.config(text=f"{t3_percent:.2f}" + "%")

        # Displays and Updates Gold Bar Rate

    def gb_calc():
        global gb_count
        global raid_count
        if raid_count == 0:
            gb_rate.config(text=f"{0:.2f}" + "%")
        else:
            gb_percent = (gb_count / raid_count) * 100
            gb_rate.config(text=f"{gb_percent:.2f}" + "%")

    def calc_all():
        math.misc_calc()
        math.t1_calc()
        math.t2_calc()
        math.t3_calc()
        math.gb_calc()
        update()

# -------------------------------------------------------------#

# Adds value when left click is used
class leftClick:

    # Adds and updates the counter on screen
    def misc_add(event):
        global misc_count
        misc_count += 1
        misc_display.config(text=misc_count)
        math.add()
        math.calc_all()

    def t1_add(event):
        global t1_count
        t1_count += 1
        t1_display.config(text=t1_count)
        math.add()
        math.calc_all()

    def t2_add(event):
        global t2_count
        t2_count += 1
        t2_display.config(text=t2_count)
        math.add()
        math.calc_all()

    def t3_add(event):
        global t3_count
        t3_count += 1
        t3_display.config(text=t3_count)
        math.add()
        math.calc_all()

    def gb_add(event):
        global gb_count
        global gb_total
        gb_count += 1
        gb_total += 1
        gb_display.config(text=gb_count)
        math.add()
        math.calc_all()
        db_add()

# -------------------------------------------------------------#

# Subtracts value when right click is used
class rightClick:

    # Adds and updates the counter on screen
    def misc_sub(event):
        global misc_count
        if misc_count == 0:
            return None
        misc_count -= 1
        misc_display.config(text=misc_count)
        math.subtract()
        math.calc_all()

    def t1_sub(event):
        global t1_count
        if t1_count == 0:
            return None
        t1_count -= 1
        t1_display.config(text=t1_count)
        math.subtract()
        math.calc_all()

    def t2_sub(event):
        global t2_count
        if t2_count == 0:
            return None
        t2_count -= 1
        t2_display.config(text=t2_count)
        math.subtract()
        math.calc_all()

    def t3_sub(event):
        global t3_count
        if t3_count == 0:
            return None
        t3_count -= 1
        t3_display.config(text=t3_count)
        math.subtract()
        math.calc_all()

    def gb_sub(event):
        global gb_count
        global gb_total
        if gb_count == 0:
            return None
        if gb_total == 0:
            return None
        undo()
        math.calc_all()


# -------------------------------------------------------------#
# Frame and TreeView in detail_tab
# Creates a frame for the Treeview and scrollbar to populate
tree_frame = Frame(detail_tab, bg=discord)
tree_frame.grid(row=1, column=1, columnspan=75, padx=2, pady=2)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


tree = ttk.Treeview(
    tree_frame,
    column=(
        "Gold Bar",
        "Date/Time",
        "Misc",
        "T1 Ring",
        "T2 Ring",
        "T3 Ring",
        "Raids Joined",
    ),
    show="headings",
    height=6,
    yscrollcommand=tree_scroll.set,
)

# Format Columns
tree.column("Gold Bar", anchor=E, minwidth=60, width=60)
tree.column("Date/Time", anchor=E, minwidth=120, width=120)
tree.column("Misc", anchor=E, minwidth=60, width=60)
tree.column("T1 Ring", anchor=E, minwidth=60, width=60)
tree.column("T2 Ring", anchor=E, minwidth=60, width=60)
tree.column("T3 Ring", anchor=E, minwidth=60, width=60)
tree.column("Raids Joined", anchor=E, minwidth=80, width=80)

# Create Headings
tree.heading("Gold Bar", text="Gold Bar", anchor=W)
tree.heading("Date/Time", text="Date/Time", anchor=W)
tree.heading("Misc", text="Misc", anchor=W)
tree.heading("T1 Ring", text="T1 Ring", anchor=W)
tree.heading("T2 Ring", text="T2 Ring", anchor=W)
tree.heading("T3 Ring", text="T3 Ring", anchor=W)
tree.heading("Raids Joined", text="Raids Joined", anchor=W)

tree.pack(padx=3, pady=3)

# Changes View of the table as you scroll
tree_scroll.config(command=tree.yview)

# -------------------------------------------------------------#

# Add Label to the Values
misc_display = Label(simple_tab, text=misc_count, bg=discord, fg="White")
t1_display = Label(simple_tab, text=t1_count, bg=discord, fg="White")
t2_display = Label(simple_tab, text=t2_count, bg=discord, fg="White")
t3_display = Label(simple_tab, text=t3_count, bg=discord, fg="White")
gb_display = Label(simple_tab, text=gb_count, bg=discord, fg="White")

# Need to separate the lines
raid_display = Label(simple_tab, text=str(raid_count), bg=discord, fg="White")

if raid_count == 0:
    misc_rate = Label(simple_tab, text="0.00%", bg=discord, fg="White")
    t1_rate = Label(simple_tab, text="0.00%", bg=discord, fg="White")
    t2_rate = Label(simple_tab, text="0.00%", bg=discord, fg="White")
    t3_rate = Label(simple_tab, text="0.00%", bg=discord, fg="White")
    gb_rate = Label(simple_tab, text="0.00%", bg=discord, fg="White")
else:
    misc_rate = Label(
        simple_tab,
        text=f"{(misc_count/raid_count) *100:.2f}" + "%",
        bg=discord,
        fg="White",
    )
    t1_rate = Label(
        simple_tab,
        text=f"{(t1_count/raid_count) *100:.2f}" + "%",
        bg=discord,
        fg="White",
    )
    t2_rate = Label(
        simple_tab,
        text=f"{(t2_count/raid_count) *100:.2f}" + "%",
        bg=discord,
        fg="White",
    )
    t3_rate = Label(
        simple_tab,
        text=f"{(t3_count/raid_count) *100:.2f}" + "%",
        bg=discord,
        fg="White",
    )
    gb_rate = Label(
        simple_tab,
        text=f"{(gb_count/raid_count) *100:.2f}" + "%",
        bg=discord,
        fg="White",
    )


# -------------------------------------------------------------#

# Database Interactions

# Create Function to Undo Last Gold Bar Entry
def undo():
    try:
        first_row = tree.get_children()[0]
        tree.delete(first_row)
    except:
        None

    conn = sqlite3.connect("drop_table.db")
    c = conn.cursor()

    # Delete the very last entry
    c.execute("DELETE from data_table WHERE oid = (SELECT MAX(oid) FROM data_table)")

    conn.commit()
    conn.close()

    global gb_total
    global gb_count
    global raid_count
    if gb_total == 0:
        return None
    gb_total -= 1
    if gb_count == 0:
        return None
    gb_count -= 1
    raid_count -= 1
    raid_display.config(text=raid_count)
    gb_display.config(text=gb_count)

    math.calc_all()


# Create Submit Function For database
def db_add():
    row_add = gb_total, date, misc_count, t1_count, t2_count, t3_count, raid_count
    tree.insert("", 0, values=row_add)

    conn = sqlite3.connect("drop_table.db")
    c = conn.cursor()

    # Insert into table
    c.execute(
        """INSERT INTO data_table VALUES (
            :totalgb, 
            :time, 
            :misc, 
            :t1, 
            :t2, 
            :t3, 
            :raids_joined)""",
        {
            "totalgb": gb_total,
            "time": date,
            "misc": misc_count,
            "t1": t1_count,
            "t2": t2_count,
            "t3": t3_count,
            "raids_joined": raid_count,
        },
    )

    conn.commit()
    conn.close()


def confirm_reset():
    global misc_count
    global t1_count
    global t2_count
    global t3_count
    global gb_count
    global raid_count

    misc_count = 0
    t1_count = 0
    t2_count = 0
    t3_count = 0
    gb_count = 0
    raid_count = 0

    misc_display.config(text=t1_count)
    t1_display.config(text=t1_count)
    t2_display.config(text=t1_count)
    t3_display.config(text=t1_count)
    gb_display.config(text=t1_count)

    misc_rate.config(text=f"{0:.2f}" + "%")
    t1_rate.config(text=f"{0:.2f}" + "%")
    t2_rate.config(text=f"{0:.2f}" + "%")
    t3_rate.config(text=f"{0:.2f}" + "%")
    gb_rate.config(text=f"{0:.2f}" + "%")

    raid_display.config(text=str(raid_count))

    math.calc_all

    # Create a database or connect to one
    conn = sqlite3.connect("drop_table.db")

    # Create a cursor
    c = conn.cursor()
    # Insert into table
    c.execute(
        """UPDATE current_data SET 
        misc= 0, 
        t1= 0, 
        t2= 0, 
        t3= 0, 
        goldbar= 0, 
        raids_joined= 0
        
        WHERE ROWID=1"""
    )

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

#  Creates a new window asking the user to confirm for resetting the count
def confirm_window():
    newWindow = Toplevel(simple_tab)
    newWindow.title("Reset Confirmation")
    newWindow.geometry("250x100")
    newWindow.configure(background=discord)
    Label(
        newWindow,
        text="This will reset every count to 0. \n This will not affect detailed view.",
        background=discord,
        foreground="white",
        padx=40,
        pady=14,
    ).grid(row=0, column=0, columnspan=4)
    y_button= Button(
                newWindow,
                text="Yes",
                command=lambda: [confirm_reset(), newWindow.destroy()],
                background=discord,
                activebackground=lighter_discord,
                foreground="white",
                activeforeground="white",
                width=10)
    y_button.grid(row=1, column=1)
    y_button.bind("<Enter>", on_enter)
    y_button.bind("<Leave>", on_leave)

    # Creates "No" button.
    # Terminates the confirmation pop-up window.
    n_button= Button(
                newWindow,
                text="No",
                command=newWindow.destroy,
                background=discord,
                activebackground=lighter_discord,
                foreground="white",
                activeforeground="white",
                width=10)
    n_button.grid(row=1, column=2)
    n_button.bind("<Enter>", on_enter)
    n_button.bind("<Leave>", on_leave)
    newWindow.attributes("-topmost", True)


# -------------------------------------------------------------#

# -------------------------------------------------------------#
# Define Buttons for simple_tab
raid_icon = Label(simple_tab, image=raid, width=72, height=72, background=discord)
raid_joined = Label(
    simple_tab, text="Raids Joined", background=discord, foreground="white"
)
misc_button = Button(
    simple_tab,
    image=misc,
    width=72,
    height=72,
    background=discord,
    activebackground=lighter_discord,
)
t1_button = Button(
    simple_tab,
    image=t1_ring,
    width=72,
    height=72,
    background=discord,
    activebackground=lighter_discord,
)
t2_button = Button(
    simple_tab,
    image=t2_ring,
    width=72,
    height=72,
    background=discord,
    activebackground=lighter_discord,
)
t3_button = Button(
    simple_tab,
    image=t3_ring,
    width=72,
    height=72,
    background=discord,
    activebackground=lighter_discord,
)
gb_button = Button(
    simple_tab,
    image=gb,
    width=72,
    height=72,
    background=discord,
    activebackground=lighter_discord,
)

def on_enter(event):
    event.widget['background'] = lighter_discord

def on_leave(event):
    event.widget['background'] = discord

# Bind Buttons to change colors on hover
misc_button.bind("<Enter>", on_enter)
misc_button.bind("<Leave>", on_leave)
t1_button.bind("<Enter>", on_enter)
t1_button.bind("<Leave>", on_leave)
t2_button.bind("<Enter>", on_enter)
t2_button.bind("<Leave>", on_leave)
t3_button.bind("<Enter>", on_enter)
t3_button.bind("<Leave>", on_leave)
gb_button.bind("<Enter>", on_enter)
gb_button.bind("<Leave>", on_leave)

# Bind Buttons to Left/Right Mouse Clicks
misc_button.bind("<Button-1>", leftClick.misc_add)
misc_button.bind("<Button-3>", rightClick.misc_sub)
t1_button.bind("<Button-1>", leftClick.t1_add)
t1_button.bind("<Button-3>", rightClick.t1_sub)
t2_button.bind("<Button-1>", leftClick.t2_add)
t2_button.bind("<Button-3>", rightClick.t2_sub)
t3_button.bind("<Button-1>", leftClick.t3_add)
t3_button.bind("<Button-3>", rightClick.t3_sub)
gb_button.bind("<Button-1>", leftClick.gb_add)
gb_button.bind("<Button-3>", rightClick.gb_sub)

# Exit Button in simple_tab
quit_button = Button(
    simple_tab,
    text="Exit",
    command=root.quit,
    bg=discord,
    activebackground=lighter_discord,
    fg="white",
    activeforeground="white",
    width=10,
)
quit_button.grid(row=6, column=6, sticky=W)
quit_button.bind("<Enter>", on_enter)
quit_button.bind("<Leave>", on_leave)

# Reset Button in simple_tab
reset_button = Button(
    simple_tab,
    text="Reset",
    command=confirm_window,
    bg=discord,
    activebackground=lighter_discord,
    fg="white",
    activeforeground="white",
    width=10,
)
reset_button.grid(row=5, column=6, sticky=W)
reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)


# Populate the Buttons in simple_tab
raid_icon.grid(row=0, column=0)
raid_display.grid(row=1, column=0)
raid_joined.grid(row=2, column=0)

misc_button.grid(row=0, column=1, pady=3)
misc_display.grid(row=1, column=1)
misc_rate.grid(row=2, column=1)

t1_button.grid(row=0, column=2, pady=3)
t1_display.grid(row=1, column=2)
t1_rate.grid(row=2, column=2)

t2_button.grid(row=0, column=3, pady=3)
t2_display.grid(row=1, column=3)
t2_rate.grid(row=2, column=3)

t3_button.grid(row=0, column=4, pady=3)
t3_display.grid(row=1, column=4)
t3_rate.grid(row=2, column=4)

gb_button.grid(row=0, column=5, pady=3)
gb_display.grid(row=1, column=5)
gb_rate.grid(row=2, column=5)


# -------------------------------------------------------------#

# Create and Populate a Undo Button in detail_tab
delete_btn = Button(
    detail_tab,
    text="Undo Last Gold Bar Entry",
    command=undo,
    bg=discord,
    activebackground=lighter_discord,
    fg="white",
    activeforeground="white",
    width=25,
)
delete_btn.grid(row=2, column=75, sticky=E)
delete_btn.bind("<Enter>", on_enter)
delete_btn.bind("<Leave>", on_leave)


# -------------------------------------------------------------#


def startup_table():
    conn = sqlite3.connect("drop_table.db")
    c = conn.cursor()

    # Query the database in reverse order
    c.execute("SELECT * FROM data_table ORDER BY totalgb DESC")
    records = c.fetchall()
    # print(records)

    # print_records = ''
    for record in records:
        row_add = (
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5],
            record[6],
        )
        tree.insert("", END, values=row_add)


startup_table()
# -------------------------------------------------------------#

# Window will always be on top
root.attributes("-topmost", True)

# Program must keep running
root.mainloop()