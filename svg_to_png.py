import argparse
from pathlib import Path

from cairosvg import svg2png


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert SVG files to transparent PNG assets.")
    parser.add_argument("--input-dir", default="svg_in", help="Directory with source SVG files")
    parser.add_argument("--output-dir", default="png_out", help="Directory for converted PNG files")
    parser.add_argument("--size", type=int, default=1624, help="Square output size in pixels")
    return parser.parse_args()


def convert_svg_to_png(input_dir: Path, output_dir: Path, size: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg_files = sorted(path for path in input_dir.iterdir() if path.suffix.lower() == ".svg")

    for svg_file in svg_files:
        output_path = output_dir / f"{svg_file.stem}.png"
        try:
            svg2png(url=str(svg_file), write_to=str(output_path), output_width=size, output_height=size)
            print(f"Converted: {svg_file.name} -> {output_path.name}")
        except Exception as exc:
            print(f"Failed to convert {svg_file.name}: {exc}")


if __name__ == '__main__':
    args = parse_args()
    convert_svg_to_png(Path(args.input_dir), Path(args.output_dir), args.size)
