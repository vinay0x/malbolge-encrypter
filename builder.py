from cx_Freeze import setup, Executable

setup(
    name = "Malbolge Encrypter",
    version = "v0.9",
    description = "A simple python program to do an even simpler encryption on entered text. Also has an option to decrypt the encrypted sentences.",
    exectuables = [Executable("malbolge.py", base = "Win32GUI")])
