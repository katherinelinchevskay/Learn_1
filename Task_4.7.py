mac = "AAAA:BBBB:CCCC"
a = bin(int(mac.replace(':', ''), 16))
result = str(a.replace('0b', ''))
print(result)

