from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base)
]

setup(name='ADHD-Reader',
      version = '0.5',
      description = 'Alpha release of an ADHD document reading assistant',
      options = {'build_exe': build_options},
      executables = executables)
