#!/bin/bash

name='sascrapper'
src_files='__main__.py SAScrapper'

out_folder='bin'
out_name="$name"
zip_name="$name"'.zip'

find . -name '__pycache__' -type d -exec rm -rf {} +
mkdir -p "$out_folder"
python3 -m zipfile -c "$out_folder"'/'"$zip_name" $src_files
echo '#!/usr/bin/env python3' > "$out_folder"'/'"$out_name"
cat "$out_folder"'/'"$zip_name" >> "$out_folder"'/'"$out_name"
chmod +x "$out_folder"'/'"$out_name"
