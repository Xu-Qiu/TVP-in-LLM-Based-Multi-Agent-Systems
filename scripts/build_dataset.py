#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path('/Users/qiu/Desktop/dataset')


def main():
    """Build the canonical English open-source dataset package."""
    export_script = ROOT / 'scripts' / 'export_english_package.py'
    if not export_script.exists():
        raise FileNotFoundError(f'Missing script: {export_script}')

    cmd = [sys.executable, str(export_script)]
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    print(f'Dataset files generated under {ROOT}')


if __name__ == '__main__':
    main()
