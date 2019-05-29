import random
import time
                                #Sortowanie bąbelkowe
                                #Sortowanie polegające na porównywaniu każdego elementu z jego sąsiadem
def sortowanie(d):

    start_time = time.time()    #Przypisanie czasu rozpoczęcia procesu sortowania
    n = len(d)                  #ilość elementów listy



    for j in range(n-1):
        for i in range(n-1):
            if d[i]> d[i+1]:    #Porównanie elementu z jego 'następnym' sąsiadem
                temp = d[i]     #Przypisanie elementu i do zmiennej 'tymczasowej'
                d[i] = d[i+1]   #Przypiasnie do elementu i wartości jego sąsiada (i+1)
                d[i+1] = temp   #Przypisanie do elementu sąsiadującego (i+1) wartości ze zmiennej tymczasowej
    czas = (time.time() - start_time)#Odjęcie czasu aktualnego od czasu rozpoczęcia wynikiem jest długość działania kodu
    print('Po sortowaniu')
    print()
    e=1                         #Zmienna pomocnicza do numerowania elementów wyświetlanych
    for xy in d:                #Wyjście posortowanej listy
        print(e,end='# ')
        print(xy)
        e+=1

    print("Długość sortowania --- %s sekund ---" % czas )

    return d
def sortowaniePliku(nazwaPliku,nazwaPlikuWyjsciowego):
    with open(nazwaPliku, 'r') as plik1:
        d = plik1.readlines()
    start_time = time.time()        # Przypisanie czasu rozpoczęcia procesu sortowania
    n = len(d)                      # ilość elementów listy

    for j in range(n - 1):
        for i in range(n - 1):
            if d[i] > d[i + 1]:     # Porównanie elementu z jego 'następnym' sąsiadem
                temp = d[i]         # Przypisanie elementu i do zmiennej 'tymczasowej'
                d[i] = d[i + 1]     # Przypiasnie do elementu i wartości jego sąsiada (i+1)
                d[i + 1] = temp     # Przypisanie do elementu sąsiadującego (i+1) wartości ze zmiennej tymczasowej
    czas = (time.time() - start_time)# Odjęcie czasu aktualnego od czasu rozpoczęcia wynikiem jest długość działania kodu

    print('Po sortowaniu')
    print()
    e = 1                           # Zmienna pomocnicza do numerowania elementów wyświetlanych
    for xy in d:                    # Wyjście posortowanej listy
        print(e, end='# ')
        print(xy)
        e += 1
    print("Długość sortowania --- %s sekund ---" % czas)
    with open(nazwaPlikuWyjsciowego, 'w') as plikWyj:   #Zapisanie pliku z danymi wyjściowymi
        plikWyj.writelines("%s" % liczba for liczba in d)

    return d

def losowanieListy(elementy):   #Dodaje określoną liczbe liczb pseudolosowych do listy
    d = []                      #Stworzenie pustej listy d
    x = 1                       #Zmienna pomocnicza do numerowania elementów wyświetlanych
    for i in range(elementy):   #Dodanie  pseudolosowej liczby z zakresu od 1 do 100 do listy o indeksie i
        d.insert(i,random.randint(1,1000))
    print('Przed sortowaniem')
    print()
    for j in d:                 #Wyjście nieposortowanej listy z liczbami pseudolosowymi
        print(x, end='# ')
        print(j)
        x+=1
                                #Stworzenie pliku niesportowane i wstawienie do każdej lini jednego elementu

    return d
def losowanieListyPlik(elementy):
    pass
def usuwanie(lista):            #Usuwanie z listy elementów powtarzających się
    lista = list(dict.fromkeys(lista))
    x = 1
    for j in lista:
        print(x, end='# ')
        print(j)
        x+=1
    return lista

sortowaniePliku('nieposortowane.txt','xyz.txt')