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
