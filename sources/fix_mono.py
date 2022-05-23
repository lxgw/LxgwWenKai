from fontTools.ttLib import TTFont
import os, sys

folder = sys.argv[1]

for file in os.listdir(folder):
    if "Mono" not in file:
        continue

    font_path = os.path.join(folder, file)
    font = TTFont(font_path)
    font["OS/2"].xAvgCharWidth = 500
    font.save(font_path, reorderTables=False)
    
