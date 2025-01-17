#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import sys
import os

console = Console()


def banner():
    console.print(Panel("""[cyan]
    Subdomain Duplicate Remover
    Author: https://github.com/Poor-Code
    """))

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            subdomains = set(f.read().splitlines())

        with open(output_file, 'w') as f:
            for subdomain in sorted(subdomains):
                f.write(f"{subdomain}\n")

        console.print(f"[green]Successfully removed duplicates!")
        console.print(f"[white]Total unique subdomains: {len(subdomains)}")

    except FileNotFoundError:
        console.print("[red]Error: Input file not found!")
        sys.exit(1)
    except PermissionError:
        console.print("[red]Error: Permission denied when accessing files!")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {str(e)}")
        sys.exit(1)


def main():
    banner()

    if len(sys.argv) != 3:
        console.print("""[yellow]
Usage: python3 subdomain_dedup.py <input_file> <output_file>
Example: python3 subdomain_dedup.py subdomains.txt unique_subdomains.txt
        """)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    remove_duplicates(input_file, output_file)

    console.print("""[cyan]
Thanks for using this tool!
Feel free to contribute at https://github.com/Poor-Code
    """)


if __name__ == "__main__":
    main()
