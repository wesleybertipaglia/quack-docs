import argparse
import os
from datetime import datetime
from pyfiglet import Figlet
from rich.console import Console
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from src.docs.service import build_documentation, save_doc_markdown, save_doc_inplace
from src.utils.file import read_file

console = Console()

def print_header():
    f = Figlet(font='slant')
    console.print(f.renderText('Quack Docs 🦆'), style="bold green")
    console.print(":sparkles: [bold yellow]Automatic Documentation Generator[/bold yellow]\n")

def main():
    print_header()

    parser = argparse.ArgumentParser(
        description="📄 Quack Docs — Automatically generate clean documentation using Amazon Q CLI.",
        usage="python main.py --file <path> [--inplace]"
    )
    parser.add_argument('--file', required=True, help='Path to the code file to be documented')
    parser.add_argument('--inplace', action='store_true', help='If set, injects docstrings directly into the code')
    args = parser.parse_args()

    console.print(f"📄 [cyan]Reading file:[/cyan] {args.file}\n")
    code_text = read_file(args.file)

    console.print("📝 [green]Building prompt for documentation generation...[/green]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
    ) as progress:
        task = progress.add_task("🚀 Quack is thinking...", total=None)
        doc = build_documentation(code_text, inplace=args.inplace)
        progress.stop()

    if "Error" in doc:
        console.print("\n❌ [bold red]Documentation generation failed. Please check the messages above.[/bold red]")
        return

    filename = os.path.basename(args.file)

    if args.inplace:
        save_doc_inplace(args.file, doc)
        console.print(f"\n✅ [bold green]Docstrings successfully added to:[/bold green] {args.file}")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"docs/quack_{filename}_{timestamp}.md"
        save_doc_markdown(output_path, doc, filename)
        console.print(f"\n📄 [bold green]Documentation successfully generated at:[/bold green] {output_path}")

    console.print("\n[bold green]✅ Process completed successfully! 🦆[/bold green]")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"\n❌ [bold red]Unexpected error:[/bold red] {e}")
        exit(1)
