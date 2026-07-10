import tomllib
import os
from pathlib import Path

CONF_PATH = Path(__file__).parent.parent / "dusty.conf"

DEFAULT_CONF = """[library]
music_scan_dir = "{music_scan_dir}"
db_path = "{db_path}"

[player]
default_volume = 50
"""

def fetch_default_user_music_path():
    home = Path.home()
    return str(home / "Music")

def fetch_default_db_path():
    home = Path.home()
    return str(home / ".config" / "dusty" / "dusty.db")

def gen_default_conf(path=CONF_PATH):
    contents = DEFAULT_CONF.format(
        music_scan_dir=fetch_default_user_music_path(),
        db_path=fetch_default_db_path()
    )
    path.write_text(contents)
    print(f"Default configuration file generated at {path}")

def load_config(path=CONF_PATH):
    if not path.exists():
        gen_default_conf(path)
    with open(path, "rb") as f:
        config = tomllib.load(f)
    return config