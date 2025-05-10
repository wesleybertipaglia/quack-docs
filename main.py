import argparse
import os
from datetime import datetime
from dotenv import load_dotenv

from src.docs.service import build_documentation, save_documentation
from src.q.service import build_prompt, call_q_cli, clean_q_output
from src.utils.file import read_file

load_dotenv()
DEFAULT_CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 50))

def main():
    print("🚀 Quack Docs — Automatic Documentation Generator started!")
    parser = argparse.ArgumentParser(description="Quack Docs — Automatic Documentation Generator")
    parser.add_argument('--file', required=True, help='Path to the code file')
    args = parser.parse_args()

    code_text = read_file(args.file)

    doc = build_documentation(code_text, call_q_cli, build_prompt, clean_q_output)

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
