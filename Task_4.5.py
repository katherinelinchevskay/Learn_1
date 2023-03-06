command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

a = command1.split()
b = command2.split()
a1 = a[4].split(',')
b1 = b[4].split(',')
result = sorted(list(set(a1) & set(b1)))
print(result)

