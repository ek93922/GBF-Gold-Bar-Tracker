# GBF-Gold-Bar-Tracker

Thank you for using my very first program since learning the basics of python.

Source code (prototype.py) is definitely a jumbled mess, and it's something I'd like to revisit once I accumulate experience with Python.

There will certainly be bugs, and I hope you let me know if you run across them.

**Important** Current version of the gold bar tracker might be flagged as a virus. Looked into using Pyinstaller with a bootloader, but that process didn't work.


------------------------------------------------------
Features
------------------------------------------------------

* Set to stay as top window at all times.

* Keeps track of player's count of drops.
    * Drop icons have left/right mouse click interactions. (Details in "How to Use" section)

* Upon adding count to gold bar, a snapshot of the counts on "Gold Bar Tracker" tab will be added to "Detailed Report" tab.
    * Gold Bar displays total amount of gold bar obtained since using the tracker.
      * Will display gold bar in descending order with recent gold bar drops displayed at the top.
    * Date/Time will read as MM/DD/YYYY 24:00

* Stores and reads relavant data from drop_table.db
    * If drop_table.db does not exist, it'll generate a new table on startup of program.
    * Deleting drop_table.db will wipe all saved data. (Basically hard reset)


------------------------------------------------------
**How to Use**
------------------------------------------------------

Gold Bar Tracker Window
  * **Loot Buttons**
    * Left click on appropriate loot icon to add 1 to the count.
      * Left click on gold bar will add an entry to "Detailed Report"

    * Right click on appropriate loot icon to subtract 1 to the count.
      * Right click on gold bar will delete the latest gold bar entry made in "Detailed Report"
        * Nothing will happen if the gold bar count on "Gold Bar Tracker" window is at 0.
        
  * **Reset Button**
    * Resets the count tabulated on "Gold Bar Tracker" window.
      * A confirmation window will pop up to prevent accidental clicks.
    
Detailed Report
  * **Undo Last Gold Bar Entry Button**
    * "Undo Last Gold Bar Entry" will delete the record of latest gold bar entry.
      * The button will also subtract 1 gold bar count from "Gold Bar Tracker" window if the count is more than 1. 
      * If the gold bar count from "Gold Bar Tracker" window is at 0, it'll still delete the entry from "Detailed Report" tab, but values in "Gold Bar Tracker" will remain unchanged. 
      

