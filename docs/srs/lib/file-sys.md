## File Sys

`lib/file_sys.py`

### FileSystemResult

- provide dataclass
- path: Path
- created: bool
- provides data if path was created or already exists when creating files and dirs

### log_file_system_result

- provide `def log_file_system_result(result: FileSystemResult, logger: Logger) -> None:`
- log info path created
- or log debug path already exists

### create_folder

- provide `def create_folder(parent_path: Path, folder_name: str) -> FileSystemResult:`
- try to create dir, create-or-fail
- return if created or already exists
- handle exists but path is not dir, raise error

### create_folder_and_log

- provide `def create_folder_and_log(parent_path: Path, folder_name: str, logger: Logger) -> FileSystemResult:`
- invoke create_folder and log_file_system_result
- return result

### create_file

- provide

```py
def create_file(
    parent_path: Path,
    file_name: str,
    content: str = "",
) -> FileSystemResult:
```

- try to create file, create-or-fail
- return if created or already exists
- handle exists but path is not file, raise error

### create_file_and_log

- provide

```py
def create_file_and_log(
    parent_path: Path,
    file_name: str,
    content: str,
    logger: Logger,
) -> FileSystemResult:
```

- invoke create_file and log_file_system_result
- return result

### copy_file_and_log

- provide

```py
def copy_file_and_log(
    source: Path,
    destination: Path,
    logger: Logger,
) -> bool:
```

- create dirs for destination if not there
- try copy file from source to destination
- log warning source not exist
- or log debug already exists
- or log warning failed
- return bool
