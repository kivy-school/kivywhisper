# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata

from kivy_deps import sdl2, glew

datas = []
datas += copy_metadata('openai-whisper', recursive=True)
'''
>>> import sys
>>> sys.executable
'F:\\CODING\\kivywhisper\\.venv\\Scripts\\python.exe'
pathlib example
https://stackoverflow.com/a/44420462/16355112
from pathlib import Path
path = Path('/my/path/to/my/directory').parents[2]
print(path)

>>> /my/path
'''
import sys, pathlib
dataspath = pathlib.Path(sys.executable) 

basevenv = pathlib.PurePath(*pathlib.Path(sys.executable).parts[:-2])
filterspath = pathlib.PurePath(basevenv, "Lib", "site-packages", "whisper", "assets", "mel_filters.npz")
filterspath2 = pathlib.PurePath(basevenv, "Lib", "site-packages", "whisper", "assets", "multilingual.tiktoken")
datas += [(filterspath, 'whisper\\assets'), (filterspath2, 'whisper\\assets'),]
#datas += [('.venv\\Lib\\site-packages\\whisper\\assets\\mel_filters.npz', 'whisper\\assets\\mel_filters.npz'), ()]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['win32timezone'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='KivyWhisper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
