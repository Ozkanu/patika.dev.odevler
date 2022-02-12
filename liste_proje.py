#birinci kısım 
duz=[]

def duz_liste(liste):
  for x in liste:
    if type(x)==list:
      duz_liste(x)
    else:
      duz.append(x)

liste_1= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
duz_liste(liste_1)

print(duz)

# ikinci kısım
y=[[1, 2], [3, 4], [5, 6, 7]]
new=list()
for i in sorted(y,reverse=True):
    new.append(sorted(i, reverse=True))
print(new)
