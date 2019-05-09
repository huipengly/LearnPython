# bri = set(['brazil', 'russia', 'india'])
bri = {'brazil', 'russia', 'india'}     # 和上面一样生产set，但是更高效
print('india in bri :', 'india' in bri)
print('usa in bri :', 'usa' in bri)
bric = bri.copy()
bric.add('china')
print('bric is superset of bri :', bric.issuperset(bri))
bri.remove('russia')
print('bri intersection of bric :', bri & bric)    # OR bri.intersection(bric)
