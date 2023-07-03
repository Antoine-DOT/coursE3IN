#choix du mot
mot = "accbb"

#si la premiere lettre est un a, retourner f0(mot -1 lettre), si c'est un b, retourner f1(mot -1 lettre), si c'est un c, retourner f2(mot -1 lettre), sinon print('rejeté')

def f0(mot):
    if mot[0] == 'a':
        return f0(mot[1:])
    elif mot[0] == 'b':
        return f1(mot[1:])
    elif mot[0] == 'c':
        return f2(mot[1:])
    else:
        print('rejeté')

#Si la premiere lettre de f1 est un a ou un c, retourner f3(mot -1lettre), sinon print('rejeté')

def f1(mot):
    if mot[0] == 'a' or mot[0] == 'c':
        return f3(mot[1:])
    else:
        print('rejeté')

# Si la premiere lettre de f2 est un b ou un a, retourner f4(mot -1 lettre), sinon print('rejeté')

def f2(mot):
    if mot[0] == 'b' or mot[0] == 'a':
        return f4(mot[1:])
    else:
        print('rejeté')

# Si la premiere lettre de f3 est un a, retourner f5(mot -1 lettre), sinon print('rejeté')

def f3(mot):
    if mot[0] == 'a':
        return f5(mot[1:])
    else:
        print('rejeté')

# Si la premiere lettre de f4 est un b, retourner f5(mot -1 lettre), sinon print('rejeté')

def f4(mot):
    if mot[0] == 'b':
        return f5(mot[1:])
    else:
        print('rejeté')

# Si f5 est retourné avec un mot vide, print('accepté'), sinon print('rejeté')

def f5(mot):
    if mot == '':
        print('accepté')
    else:
        print('rejeté')

(f0(mot))