import re

text = input()
pattern = "\\b(([a-z]+\\.([a-z]{2,})\\.(\\d{4})@(alumnos)\\.urjc\\.es)|(([a-z]+)\\.([a-z]+)@urjc\\.es))\\b"
results = re.findall(pattern, text)
for match in results:
    if "alumnos" in match:
        print("alumno " + match[2] + " matriculado en " + match[3])
    else:
        print("profesor " + match[6] + " apellido " + match[7])
