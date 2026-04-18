bindings = input()

l = bindings.split(" ")
output = []
for i in l:
    if i.isspace() or i == "  " or i == " " or i == "" or i is None:
        continue

    if i.startswith("&"):
        output.append(i)
        continue

    output.append("DE_" + i + " ")

print(" ".join(output))
