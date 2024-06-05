import json
import os

from libs.system.file_system import ensure_directory_exists, ensure_empty_directory

#
# Local Path
#


def _get_local_path(script_path: str, relpath: str):
    script_dir = os.path.dirname(script_path)
    return os.path.join(script_dir, relpath)


def get_local_dir(script_path: str, relpath: str, make_empty: bool = False):
    local_path = _get_local_path(script_path, relpath)

    if make_empty:
        ensure_empty_directory(local_path)

    return local_path


#
# Absolute IO
#


def load_text(file_path) -> str:
    with open(file_path) as file:
        return file.read()


def load_json(file_path):
    with open(file_path) as file:
        return json.loads(file.read())


def save_text(file_path, value: str):
    ensure_directory_exists(os.path.dirname(file_path))
    with open(file_path, "w") as file:
        file.write(value)


def save_json(file_path, value):
    ensure_directory_exists(os.path.dirname(file_path))
    with open(file_path, "w") as file:
        file.write(json.dumps(value, indent=4))


#
# Local IO
#


def load_local_text(script_path: str, relpath: str) -> str:
    local_path = _get_local_path(script_path, relpath)
    return load_text(local_path)


def load_local_json(script_path: str, relpath: str):
    local_path = _get_local_path(script_path, relpath)
    return load_json(local_path)


def save_local_text(script_path: str, relpath: str, value: str):
    local_path = _get_local_path(script_path, relpath)
    save_text(local_path, value)


def save_local_json(script_path: str, relpath: str, value):
    local_path = _get_local_path(script_path, relpath)
    save_json(local_path, value)
