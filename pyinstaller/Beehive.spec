# -*- mode: python -*-

block_cipher = None


a = Analysis(['BeehiveUI.py'],
             pathex=['C:\\Users\\Jstephens\\Desktop\\python\\Beehive'],
             binaries=[],
             datas=[('flower.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Beehive',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='flower.ico')
