# dictionary is a changeble, unordered collection of unique key, values pairs fast
# because they use hashing,allow us to access a value quickly, Simliarly set

capitals = {'USA':'washington', 'india':'delhi', 'china':'bejing', 'seden':'stockholm'}
#print(capitals['india'])
print(capitals.get('germany'))
print(capitals.get('india'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'kerala':'trvndrm'})
for key,value in capitals.items():
    print(key,value)