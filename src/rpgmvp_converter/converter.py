import logging
from pathlib import Path
from typing import Optional

from .constants import PNG_HEADER, RPGMVP_HEADER_SIZE

logger = logging.getLogger(__name__)


class RpgMvpConverter:
    """
    Handles the conversion of RPG Maker MV encrypted image files (.rpgmvp) to PNG format.
    """

    def convert_file(
        self, input_path: Path, output_path: Optional[Path] = None
    ) -> bool:
        """
        Converts a single .rpgmvp file to .png.

        Args:
            input_path: Path to the input .rpgmvp file.
            output_path: Path to the output .png file. If None, uses the same name as input.

        Returns:
            True if successful, False otherwise.
        """
        input_path = Path(input_path)
        if not input_path.exists():
            logger.error(f"Input file not found: {input_path}")
            return False

        if not input_path.suffix.lower() == ".rpgmvp":
            logger.warning(
                f"File {input_path} does not have .rpgmvp extension. Skipping."
            )
            return False

        if output_path is None:
            output_path = input_path.with_suffix(".png")
        else:
            output_path = Path(output_path)
            # Ensure the parent directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Converting '{input_path}' to '{output_path}'...")

        with input_path.open("rb") as f_in:
            data = f_in.read()

        if len(data) < RPGMVP_HEADER_SIZE:
            logger.error(f"File {input_path} is too small to be a valid RPGMVP file.")
            return False

        with output_path.open("wb") as f_out:
            f_out.write(PNG_HEADER)
            f_out.write(data[RPGMVP_HEADER_SIZE:])

        logger.info(f"Successfully converted: {output_path}")
        return True

    def convert_directory(
        self, input_dir: Path, output_dir: Optional[Path] = None
    ) -> None:
        """
        Recursively converts all .rpgmvp files in a directory.

        Args:
            input_dir: Path to the input directory.
            output_dir: Path to the output directory. If None, mirrors the structure in a sibling directory.
        """
        input_dir = Path(input_dir)
        if not input_dir.exists():
            logger.error(f"Input directory not found: {input_dir}")
            return

        # If output_dir is not specified, create a sibling directory named "dirname_png"
        # Or follow the original logic: "current_working_dir/basename"
        if output_dir is None:
            # Original logic: output_dir = os.path.join(os.getcwd(), base_dir)
            # We'll make it slightly more predictable: defaults to ./<name>
            output_dir = Path.cwd() / input_dir.name
        else:
            output_dir = Path(output_dir)

        logger.info(f"Scanning directory: {input_dir}")
        logger.info(f"Output directory: {output_dir}")

        count = 0
        for file_path in input_dir.rglob("*.rpgmvp"):
            # Calculate relative path to maintain structure
            relative_path = file_path.relative_to(input_dir)
            target_path = output_dir / relative_path.with_suffix(".png")

            if self.convert_file(file_path, target_path):
                count += 1

        logger.info(f"Directory conversion complete. Processed {count} files.")
