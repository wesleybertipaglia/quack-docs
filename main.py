import argparse
import os
from datetime import datetime
from src.docs.service import build_documentation, save_documentation, save_inplace
from src.q.service import build_prompt, call_q_cli, clean_q_output
from src.utils.file import read_file

def main():
    print("🚀 Quack Docs — Automatic Documentation Generator started!")

    parser = argparse.ArgumentParser(description="Quack Docs — Automatic Documentation Generator")
    parser.add_argument('--file', required=True, help='Path to the code file')
    parser.add_argument('--inplace', action='store_true', help='Insert docstrings directly into the source file')
    args = parser.parse_args()

    code_text = read_file(args.file)

    doc = build_documentation(
        code_text,
        call_q_cli=call_q_cli,
        build_prompt=build_prompt,
        clean_q_output=clean_q_output,
        inplace=args.inplace
    )

    if "Error" in doc:
        print("❌ Documentation generation failed. Please check the error messages above.")
        return

    filename = os.path.basename(args.file)

    if args.inplace:
        save_inplace(args.file, doc)
        print(f"\n✅ Docstrings successfully added to: {args.file}")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"docs/quack_{filename}_{timestamp}.md"
        save_documentation(output_path, doc, filename)
        print(f"\n✅ Documentation successfully generated in: {output_path}")

if __name__ == "__main__":
    main()
