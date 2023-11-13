from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [], 
    'excludes': [],
    'include_files': [
        ('./UI', 'UI'),
    ]
    }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('scripts/main.py', base=base)
]

setup(name='Readmate',
      version = '0.9',
      description = 'Beta release of our project',
      options = {'build_exe': build_options},
      executables = executables)
