import pkgutil
from cx_Freeze import setup, Executable

# functions
def AllPackage(): 
    return [i.name for i in list(pkgutil.iter_modules()) if i.ispkg]
def notFound(A,v):
    try: 
        A.index(v) 
        return False
    except: 
        return True

# app settings
APPNAME = "Minesweeper"
DESCRIPTION = "Minesweeper written in Pygame."
VERSION = "1.1.2"
FILENAME = "minesweeper.py"
INCLUDEDFILES = ["icon.ico", "sprites/", "sounds/"]
ICONPATH = "icon.ico"
LIBRARIES = ["pygame"]
PACKAGES = ["re"]

# exclude unneed packages
BasicPackages = ["collections", "encodings", "importlib"] + LIBRARIES
build_exe_options = {
    "include_files": INCLUDEDFILES,
    "includes": BasicPackages,
    "excludes": [i for i in AllPackage() if notFound(BasicPackages, i)],
    "packages": PACKAGES
}

# setup
setup(name = APPNAME,
      description = DESCRIPTION,
      version = VERSION,
      options = {"build_exe": build_exe_options},
      executables = [Executable(FILENAME, base='Win32GUI', icon=ICONPATH)]
)
