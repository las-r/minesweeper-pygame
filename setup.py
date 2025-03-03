from cx_Freeze import setup, Executable

setup(
    name="Minesweeper",
    version="1.1.1",
    description="Minesweeper written in Pygame.",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["sprites/", "sounds/"],
        }
    },
    executables=[Executable("minesweeper.py", base="Win32GUI", icon="icon.ico")]
)
