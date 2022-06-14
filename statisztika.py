# 1. A karakterek_szama(text)       függvény visszatér a karakterek számával. ('\n karakterekkel eggyütt')
# 2. A szavak_szama(text)           függvény visszatér a szavak számával.
# 3. A sorok_szama(text)            függvény visszatér a sorok számával.
# 4. Az e_betuk_szama(text)         függvény visszatér a 'e' betük számával.
# 5. A lorem_szavak_szama(text)     függvény visszatér a "lorem" szavak számával.
# 6. A legritkabb_karakter(text)    függvény visszatér a legritkábban előforduló karakterrel.
# 7. A leghosszabb_sor_hossza(text) függvény visszatér a leghosszabb sor hosszával.

# 1
def karakterek_szama(txt):
    return len(txt)
# 2
def szavak_szama(txt):
    return len(txt.split())
# 3        
def sorok_szama(txt):
   return len(txt.split('\n'))
# 4
def e_betuk_szama(txt):
    return txt.count('e')
# 5
def lorem_szavak_szama(txt):
    return txt.count('lorem')

# 6
def legritkabb_karakter(txt):
    stat = dict()
    for betu in txt:
        stat[betu] = stat.get(betu, 0) + 1
    return min(stat, key=stat.get)
# 7
def leghosszabb_sor_hossza(txt):
    sorok =  txt.split('\n')
    return len( max( sorok, key=len ) )