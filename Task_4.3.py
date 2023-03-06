config = "switchport trunk allowed vlan 1,3,10,20,30,100"
s = config.split()
result = s[4].split(',')
print(result)