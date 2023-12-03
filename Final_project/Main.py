#export PATH="$HOME/.local/bin:$PATH"
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.prompt import Confirm
import re
import silables as sb
import accents as acns

#inicio-----------------------------------------------------
console = Console()
MARKDOWN = """
# Calculadora De Silabas

**Este es un programa para separar palabras por silabas y clasificarlas**

"""
md = Markdown(MARKDOWN)
console.print(md)

#Obtiene datos y realiza los proceso necesarios----------------------------
words = Prompt.ask("• Introduce un texto")
#words = words.replace
separated_words = sb.silables(words)
tonics = acns.tonics(separated_words)
types = acns.clasification(tonics)

#procesa y formatea la salida de datos--------------------------------------
console.print(f"'{words}'")
console.print(separated_words)
console.print(f"tonics: '{tonics}'")
console.print(f"types: '{types}'")