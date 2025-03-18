#!/bin/bash
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:/opt/homebrew/opt/cairo/lib/pkgconfig"
export DYLD_LIBRARY_PATH="/opt/homebrew/lib"
python svg_to_png.py 