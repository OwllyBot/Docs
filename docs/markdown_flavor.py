import sys
import os
from pathlib import Path
folder = os.path.abspath(os.path.dirname(__file__))


if len(sys.argv) > 0:
    md = Path(f"{folder}/{sys.argv[1]}.md")
    if os.path.exists(md):
        data = open(md, "r", encoding="utf-8")
        lines = data.readlines()
        data.close()
        final=open(md, "w", encoding="utf-8")
        for ln in lines:
            final_text = ''.join([line.rstrip()+'\n' for line in ln.splitlines()])
            final_text=final_text.replace("\n", "  \n")
            final.write(final_text)
        final.close()
    else:
        print("Error, this file doesn't exists.")
