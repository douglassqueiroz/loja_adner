# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/home/douglas/Área de Trabalho/projeto_Adner/ambiente_adner/backend.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/douglas/Área de Trabalho/projeto_Adner/ambiente_adner/templates', 'templates'), ('/home/douglas/Área de Trabalho/projeto_Adner/ambiente_adner/produto', 'produto'), ('/home/douglas/Área de Trabalho/projeto_Adner/ambiente_adner/usuario', 'usuario'), ('/home/douglas/Área de Trabalho/projeto_Adner/ambiente_adner/venv/Lib/site-packages', 'site-packages')],
    hiddenimports=[],
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
    [],
    name='backend',
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
