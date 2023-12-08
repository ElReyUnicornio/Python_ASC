#export PATH="$HOME/.local/bin:$PATH"
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.table import Table
import rich.box
import re
import silables as sb
import accents as acns
import os

debug = True
console = Console()

MARKDOWN = """
# Calculadora De Silabas

>separa las palabras por espacios

**Este es un programa para separar palabras por silabas y clasificarlas**

"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    #inicio-----------------------------------------------------
    clear_console()
    
    md = Markdown(MARKDOWN)
    console.print(md)

    #Obtiene datos y realiza los proceso necesarios----------------------------
    console.print()
    words = Prompt.ask("[bold yellow]•[/bold yellow] Introduce un texto")
    words = words.strip()
    words = re.sub(r'\s{2,}', " ", words)
    #words = words.replace
    separated_words = words.split(" ")
    silables = sb.silables(words)
    tonics = acns.Get_tonics_index(silables)
    tonics_slbs = acns.Get_tonics(silables, tonics)
    types = acns.Get_clasification(tonics)
    console.print()
    console.rule()

    #procesa y formatea la salida de datos--------------------------------------

    if debug:
        console.print(f"'{separated_words}'")
        console.print(silables)
        console.print(f"tonics_indx: '{tonics}'")
        console.print(f"tonics: '{tonics_slbs}'")
        console.print(f"types: '{types}'")

    console.print()
    table = Table(show_header=True, header_style="bold cyan", box = rich.box.ROUNDED)
    table.title = "[green]'resultados'"
    table.padding = (0, 5)

    # Agrega columnas a la tabla
    table.add_column("Palabra", style="bold", justify="center")
    table.add_column("Silaba", style="bold", justify="center", overflow="fold")
    table.add_column("Tonica", style="bold", justify="center")
    table.add_column("Tipo", style="bold", justify="center")

    # Agrega filas a la tabla
    for i, x in enumerate(separated_words):
        table.add_row("[bold red]" + x, "[bold yellow]" + silables[i].replace(" ", "-"), "[bold green]" + tonics_slbs[i], "[bold purple]" + types[i])

    table.overflow = "fold"
    # Renderiza la tabla en la consola
    console.print(table, justify="center")
    console.print()
    
    console.rule()
    console.print()

    if Confirm.ask("Desea probar de nuevo?"):
        main()
        
main()