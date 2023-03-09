ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
ip = "10.1.1.1"
sp = ip.split('.')
print(ip_template.format(int(sp[0]), int(sp[1]), int(sp[2]), int(sp[3])))
