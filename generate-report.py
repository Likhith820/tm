import os

os.system("mkdir -p tm")
os.system("./tm.py --report docs/template.md | pandoc -f markdown -t html > tm/report.html")
os.system("./tm.py --dfd | dot -Tpng -o tm/dfd.png")
os.system("./tm.py --seq | java -Djava.awt.headless=true -jar $PLANTUML_PATH -tpng -pipe > tm/seq.png")
