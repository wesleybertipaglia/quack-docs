import os
import argparse
from datetime import datetime
from pyfiglet import Figlet
from rich.console import Console
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
        usage="python main.py --file <path> [--output <dir>] [--inplace]"
    )
    parser.add_argument('--file', required=True, help='Path to the code file to be documented')
    parser.add_argument('--output', help='Directory to save the generated documentation or modified code')
    parser.add_argument('--inplace', action='store_true', help='If set, injects docstrings directly into the code')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        console.print(f"❌ [bold red]Error:[/bold red] The file {args.file} does not exist.")
        return

    if args.output is None:
        if args.inplace:
            args.output = os.path.dirname(args.file)
        else:
            args.output = os.path.join('./docs')

    if not os.path.isdir(args.output):
        if os.path.isfile(args.output):
            console.print(f"❌ [bold red]Error:[/bold red] The output path {args.output} is a file, not a directory.")
            return
        else:
            console.print(f"📂 [yellow]Creating output directory:[/yellow] {args.output}")
            os.makedirs(args.output, exist_ok=True)

    filename = os.path.basename(args.file)

    if not args.inplace:        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(args.output, f"quack_{filename}_{timestamp}.md")
    else:
        output_path = os.path.join(args.output, filename)

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

    if args.inplace:
        save_doc_inplace(output_path, doc)
        console.print(f"\n✅ [bold green]Docstrings successfully added to:[/bold green] {output_path}")
    else:
        save_doc_markdown(output_path, doc, filename)
        console.print(f"\n📄 [bold green]Documentation successfully generated at:[/bold green] {output_path}")

    console.print("\n[bold green]✅ Process completed successfully! 🦆[/bold green]")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"\n❌ [bold red]Unexpected error:[/bold red] {e}")
        exit(1)
