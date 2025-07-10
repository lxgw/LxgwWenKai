:: surpress variable
@echo off

set folder_path=..\fonts\TTF
::make folder
if not exist %folder_path% (
    mkdir %folder_path%
    echo Folder created at %folder_path%
)

:: For UFOZ file %F in folder
For %%F in (.\*.ufoz) do (
    echo === Building font %%F ===
    py extract_ufoz.py %%F
    :: remove extension then add .ufo
    fontmake %%~nF.ufo --keep-overlaps --keep-direction --no-generate-GDEF --no-production-names -o ttf --output-dir %folder_path%
    @RD /S /Q %%~nF.ufo
    echo === END ===
    echo
)

echo === Modifying MONO average width... ===
py fix_mono.py %folder_path%
echo === END ===
echo
