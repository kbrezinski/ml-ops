from pathlib import Path

from config import config
from mlops import main

args_fp = Path(config.CONFIG_DIR, "args.json")
