import os

language_map = {
    '.c': 'c',
    '.cpp': 'cpp',
    '.h': 'cpp',
    '.java': 'java',
    '.go': 'go',
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.cs': 'csharp',
    '.rs': 'rust',
    '.php': 'php',
    '.rb': 'ruby',
    '.html': 'html',
    '.css': 'css',
    '.swift': 'swift',
    '.kt': 'kotlin',
    '.r': 'r',
    '.pl': 'perl',
    '.m': 'matlab'
}

def detect_language(file_path):
    """Detect the programming language based on file extension."""    
    ext = os.path.splitext(file_path)[1].lower()
    return language_map.get(ext, 'plaintext')
