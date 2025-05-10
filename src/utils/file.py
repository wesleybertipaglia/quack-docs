def read_file(file_path):
    """Read the contents of a file."""
    print("📄 Reading the file:", file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_file(file_path, content):
    """Save content to a file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
