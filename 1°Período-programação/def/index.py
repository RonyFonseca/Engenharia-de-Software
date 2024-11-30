list = ["Rony", "Bruno", "Juh", "Wevertton"]
p_max = max(list, key=len)
i = 0 
print("*"* (len(p_max) + 4))
while(i != len(list)):
    diferenca = len(str(p_max)) - len(list[i])
    print(f"* {list[i]} {diferenca*" "}*")
    i+= 1
print("*"* (len(p_max) + 4))