### GUI
In here you can find all things related to the GUI. Run `window.py` to launch our beautiful GUI. Kivy will make use of the `layout.kv` file.
> Running the GUI will only work wenn run inside the repository and not standalone!

### Requirements
- Python 3.8
- Kivy 1.10.1

### Notes
Be careful to uncomment the lines inside `window.py` inside the methods `send_gesture` and `send_signal` accordingly to the comments inside those methods. The reason they exist is to make the gui work without connection. We suggest the user to test the connection calling the method move_hand in wrapper.py inside a python terminal before uncommenting those lines.  