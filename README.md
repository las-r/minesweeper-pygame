# Minesweeper Pygame
A Minesweeper game written in Python using the Pygame library.

Both a Python and Windows executable file are available. The python file only supports Python 3 and Windows executable file only supports Windows 8 to 11.

Feel free to use, modify, and distribute this however you like! :)

![image](https://github.com/user-attachments/assets/1c335293-99e8-45df-b0b7-2ab4477d5553)

## Compiling .py file to `.exe` or `.msi` file
In case you want to, here's a quick tutorial on how you can build a Windows executable or installer from Python.

### Step 1: Install cx-Freeze
Open a command prompt window  and type or paste the following in:
```
pip install cx-Freeze
```
It should download fine as long as you have [Python](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/) installed on your computer.

### Step 2: Build the program
There's a file included named `setup.py`. It should already have everything necessary to build an executable file, but I'd recommend you'd modify it to accomodate if you're not just building this game.

Put the `setup.py` file into the same directory as your Python file and open a command prompt window in it.\
Type or paste the following in if you want a `.exe` executable:
```
python setup.py build
```
If you want a `.msi` installer, type or paste this in instead:
```
python setup.py bdist_msi
```
If all of this succeeded, then you should have a folder in your directory called `build`. Inside of it, you should have a `.exe` or `.msi` file that does the same thing as your Python program, along with all the libraries and stuff. In case you somehow haven't noticed already. this tutorial is for Windows only. Sorry, Mac and Linux users!

If you had any issues with building, please contact the [cx-Freeze](https://github.com/marcelotduarte/cx_Freeze?tab=readme-ov-file) dev team, not me.

Yes, I copied and pasted this description from my [Connect 4](https://github.com/las-r/connect-4-pygame) game.
