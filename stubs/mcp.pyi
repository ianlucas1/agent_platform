from typing import Any

def write_file(path: str, content: str) -> None: ...
def read_file(path: str) -> str: ...
def delete_file(path: str) -> None: ...
def list_files(directory: str) -> list[str]: ...
def run_task(name: str, *args: Any, **kwargs: Any) -> Any: ...
