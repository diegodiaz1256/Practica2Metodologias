import re

text = input()
pattern = "\\b(?:C/|Calle) ([A-ZÑÁÉÍÓÚ][a-zñáéíóú]+),? *(?:Nº|N|n)? *(\\d+), *(\\d{5})\\b"
results = re.findall(pattern, text)
for match in results:
    print(match[2] + "-" + match[0] + "-" + match[1])

