import os
from datetime import datetime
from src.q.service import build_prompt, call_q_cli, clean_q_output
from src.utils.file import save_file

def build_documentation(code_text, inplace=False):
    prompt = build_prompt(code_text, inplace)
    doc = call_q_cli(prompt)
    doc = clean_q_output(doc, inplace)
    return doc

def save_doc_markdown(file_path, output, code_filename):
    now = datetime.now().strftime("%Y-%m-%d")
    header = f"# Quack Docs — {code_filename}\n\n"
    header += f"file: {code_filename}\n"
    header += f"created at: {now}\n"
    header += "---\n\n"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    save_file(file_path, header + output)

def save_doc_inplace(file_path, modified_code):
    save_file(file_path, modified_code)
