import time

liste = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"
]

mot = input('Entrez votre mot de passe : ')
chaine = str()

def test(chaine, mot, start_time):
    if chaine == mot:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Votre mot de passe est', chaine)
        print(f'Trouver en : {elapsed_time:.2f} secondes')
        exit()

def brute_force():
    start_time = time.time()
    for l in liste:
        chaine = l
        test(chaine, mot, start_time)
        print(chaine)

        for l2 in liste:
            chaine = l + l2
            test(chaine, mot, start_time)
            print(chaine)

            for l3 in liste:
                chaine = l + l2 + l3
                test(chaine, mot, start_time)
                print(chaine)

                for l4 in liste:
                    chaine = l + l2 + l3 + l4
                    test(chaine, mot, start_time)
                    print(chaine)

                    for l5 in liste:
                        chaine = l + l2 + l3 + l4 + l5
                        test(chaine, mot, start_time)
                        print(chaine)

                        for l6 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6
                            test(chaine, mot, start_time)
                            print(chaine)

brute_force()
