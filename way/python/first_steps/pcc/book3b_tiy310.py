#!try-it-yourself 3.10
musicians = []
print(musicians)
musicians.extend(['vivaldi', 'queen', '2pac', 'system of a down'])
print(musicians)#без [] extend не добавляет много :)
musicians.append('sex')
print(musicians)
musicians.insert(3, 'lol')
print(musicians)
del musicians[3]
print(musicians)
popped_musicians=musicians.pop()
print(musicians)
musicians.remove('2pac')
print(musicians)
print(sorted(musicians))
print(sorted(musicians, reverse=True))
print(musicians)
musicians.sort()
print(musicians)
musicians.sort(reverse=True)
print(musicians)
musicians.reverse()
print(musicians)