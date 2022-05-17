:: surpress variable
@echo off 
set folder_path=..\fonts\TTF
::make folder
if not exist %folder_path% (
    mkdir %folder_path%
    echo Folder created at %folder_path%
)

:: For UFO directory %D in folder
For /D %%D in (.\*.ufo) do (
    echo === Building font %%D ===
    fontmake %%D --keep-overlaps --keep-direction --no-generate-GDEF --no-production-names -o ttf --output-dir %folder_path%
    echo === END ===
    echo
)