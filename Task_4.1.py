nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
natOverride = nat.replace('FastEthernet', 'GigabitEthernet')

print(natOverride)
