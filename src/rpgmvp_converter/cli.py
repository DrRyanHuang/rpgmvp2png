import argparse
import logging
import sys
from pathlib import Path

from .converter import RpgMvpConverter


def setup_logging(verbose: bool = False) -> None:
    """Configures the logging output."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert RPG Maker MV encrypted images (.rpgmvp) to PNG."
    )
    parser.add_argument("path", type=Path, help="Input file or directory path.")
    parser.add_argument(
        "output", type=Path, nargs="?", help="Output file or directory path. Optional."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging."
    )

    args = parser.parse_args()

    setup_logging(args.verbose)

    converter = RpgMvpConverter()
    input_path = args.path

    if not input_path.exists():
        logging.error(f"Error: Path '{input_path}' does not exist.")
        sys.exit(1)

    if input_path.is_file():
        output_file = args.output

        # If output not provided, default to changing suffix
        if output_file is None:
            output_file = input_path.with_suffix(".png")
        # If output is a directory, put the file inside it
        elif output_file.is_dir():
            output_file = output_file / input_path.with_suffix(".png").name

        success = converter.convert_file(input_path, output_file)
        sys.exit(0 if success else 1)

    elif input_path.is_dir():
        converter.convert_directory(input_path, args.output)


if __name__ == "__main__":
    main()
