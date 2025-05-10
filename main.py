import argparse
import os
from datetime import datetime
import subprocess
import re
from dotenv import load_dotenv

load_dotenv()
DEFAULT_CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 50))

def read_file(file_path):
    print("📄 Reading the file:", file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def build_prompt(code_text):
    print("📝 Building the prompt for documentation generation...")
    prompt = f"""
You are a technical writer.

Generate a concise and clear documentation summary for the following code. Include a class explanation, constructor details, a section for properties (if applicable), and method descriptions. 
For each method, provide an example usage. Do not write code comments or docstrings. Just explain the structure and logic in plain English.

Code:
{code_text}

Documentation:
"""
    return prompt.strip()

def clean_q_output(output):
    print("🔧 Cleaning up the Q CLI output...")
    output = re.sub(r'```.*?```', lambda m: f'{{{{CODE_BLOCK_{hash(m.group(0))}}}}}', output, flags=re.DOTALL)
    output = re.sub(r'\x1b\[[0-9;]*m', '', output)
    output = re.sub(r'(To learn more about MCP safety.*|/help.*|ctrl.*|━━━━━━━━━━━━━━━━.*)', '', output)
    output = re.sub(r'\{\{CODE_BLOCK_(.*?)\}\}', lambda m: m.group(1), output)
    
    return output.strip()

def call_q_cli(prompt):
    print("🚀 Quack is thinking... Calling the Q CLI to generate documentation...")
    try:
        result = subprocess.run(
            ["q"],
            input=prompt,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Error: Q CLI returned an error.")
            print(result.stderr)
            return "Error generating documentation."

        return clean_q_output(result.stdout)

    except FileNotFoundError:
        print("❌ Error: Q CLI is not installed. Please install Q CLI first.")
        return "Error: Q CLI is not installed."

    except Exception as e:
        print(f"❌ Exception: Something went wrong while calling Q CLI: {e}")
        return "Error generating documentation."

def save_documentation(file_path, output, code_filename):
    print("💾 Saving documentation to:", file_path)
    now = datetime.now().strftime("%Y-%m-%d")
    header = f"# Quack Docs — {code_filename}\n\n"
    header += f"file: {code_filename}\n"
    header += f"created at: {now}\n"
    header += "---\n\n"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(header + output)

def main():
    print("🚀 Quack Docs — Automatic Documentation Generator started!")
    parser = argparse.ArgumentParser(description="Quack Docs — Automatic Documentation Generator")
    parser.add_argument('--file', required=True, help='Path to the code file')
    args = parser.parse_args()

    code_text = read_file(args.file)

    prompt = build_prompt(code_text)

    doc = call_q_cli(prompt)

    if "Error" in doc:
        print("❌ Documentation generation failed. Please check the error messages above.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(args.file)
    output_path = f"docs/quack_{filename}_{timestamp}.md"

    save_documentation(output_path, doc, filename)
    print(f"\n✅ Documentation successfully generated in: {output_path}")

if __name__ == "__main__":
    main()
