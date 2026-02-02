#!/usr/bin/env python3
import sys
from pathlib import Path

src_path = str(Path(__file__).parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from rpgmvp_converter.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
