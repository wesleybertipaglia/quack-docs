import os
from datetime import datetime
from src.utils.file import save_file

def build_documentation(code_text, call_q_cli, build_prompt, clean_q_output):
    prompt = build_prompt(code_text)
    doc = call_q_cli(prompt)
    return doc

def save_documentation(file_path, output, code_filename):
    print("💾 Saving documentation to:", file_path)
    now = datetime.now().strftime("%Y-%m-%d")
    header = f"# Quack Docs — {code_filename}\n\n"
    header += f"file: {code_filename}\n"
    header += f"created at: {now}\n"
    header += "---\n\n"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    save_file(file_path, header + output)