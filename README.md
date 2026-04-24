# SVG to PNG Converter

Convert batches of SVG assets into transparent PNG files.

## Requirements

- Python 3.9+
- CairoSVG runtime dependencies

On macOS:

```bash
brew install cairo pango libpng jpeg giflib librsvg
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Place source files into `svg_in/` and run:

```bash
python svg_to_png.py
```

Custom directories or output size:

```bash
python svg_to_png.py --input-dir svg_in --output-dir png_out --size 1624
```

## Notes

- output PNG files keep transparent backgrounds
- the default output is square `1624x1624`
- source SVG files are left unchanged
