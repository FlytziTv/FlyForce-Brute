import time

liste = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"
]

mot = input('Entrez votre mot de passe : ')
longueur_mot = len(mot)  # Déterminer automatiquement la longueur du mot de passe

# Initialiser le compteur global
global_counter = 0

def test(chaine, mot, start_time):
    global global_counter
    global_counter += 1
    if global_counter % 1000 == 0:
        print(f'{global_counter} essais effectués.')
    if chaine == mot:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Votre mot de passe est', chaine)
        print(f'Trouvé en : {elapsed_time:.2f} secondes')
        exit()

def brute_force(current_string, mot, start_time, longueur_mot):
    if len(current_string) > longueur_mot:
        return
    test(current_string, mot, start_time)
    if len(current_string) < longueur_mot:
        for char in liste:
            brute_force(current_string + char, mot, start_time, longueur_mot)

def main():
    start_time = time.time()
    brute_force("", mot, start_time, longueur_mot)

main()