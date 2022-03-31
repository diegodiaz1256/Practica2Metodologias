import re

text = input()
pattern = r"^.+\.\d{3}\s+(\w+) .+\[(\w+)\] (?:[a-z]+\.)+([A-Z]\w+)\s+:\s+(.+)$"
pattern = r"^.+\.\d{3}\s+(\w+) .+\[(\w+)\] (?:[a-z]+\.)*([A-Z]\w+)\s+:\s+(.+)$"
results = re.findall(pattern, text)
for match in results:
    match = list(match)
    for group in match:
        print('"', group, '"', "," if match.index(group) != 3 else "", end="", sep="")
