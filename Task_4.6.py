# Prefix, AD/Metric, Next-Hop, Last update, Outbound Interface
names_par = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
a = ospf_route.replace('via','').replace("[","").replace("]","").replace(",","").split()
for n, o in zip(names_par, a):
    print(f'{n}'.ljust(20, ' '), f'{o}')
