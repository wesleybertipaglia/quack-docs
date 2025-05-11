def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"❌ Permission denied while trying to read '{file_path}'.")
    except Exception as e:
        raise Exception(f"❌ An unexpected error occurred while reading '{file_path}': {e}")

def save_file(file_path, content):
    """Save content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except PermissionError:
        raise PermissionError(f"❌ Permission denied while trying to write to '{file_path}'.")
    except Exception as e:
        raise Exception(f"❌ An unexpected error occurred while writing to '{file_path}': {e}")
