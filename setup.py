from cx_Freeze import setup, Executable

setup(name='calculator', version='0.1', description='Calculator',
      executables = [Executable("hel.py")] )