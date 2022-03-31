import re

text = input()
pattern = ""
results = re.findall(pattern, text)
for match in results:
    if "alumnos" in match:
        print("alumno " + match[2] + " matriculado en " + match[3])
    else:
        print("profesor " + match[6] + " apellido " + match[7])
