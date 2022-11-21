#!/bin/bash

export folder_path=../fonts/TTF

[ -d "${folder_path}" ] || mkdir -p "${folder_path}" && echo "Folder created at ${folder_path}"

for f in *.ufoz; do
    echo "=== Building font ${f} ==="
    python extract_ufoz.py ${f}

    fontmake "${f%.*}.ufo" --keep-overlaps --keep-direction --no-generate-GDEF --no-production-names -o ttf --output-dir "${folder_path}"
    rm -rf "${f%.*}.ufo"
    echo "=== END ==="
done;

echo "=== Modifying MONO average width... ==="
python fix_mono.py "${folder_path}"
echo "=== END ==="
