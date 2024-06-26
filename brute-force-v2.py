import time

# Liste de tous les caractères possibles
liste = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/"
]

def get_password():
    mot = input('Entrez votre mot de passe : ')
    if not mot:
        print("Le mot de passe ne peut pas être vide.")
        exit()
    return mot

mot = get_password()
longueur_mot = len(mot)  # Déterminer automatiquement la longueur du mot de passe

def test(chaine, mot, start_time):
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
            new_string = current_string + char
            print(f"Testing: {new_string}")  # Affichage de la progression
            brute_force(new_string, mot, start_time, longueur_mot)

def main():
    start_time = time.time()
    try:
        brute_force("", mot, start_time, longueur_mot)
    except Exception as e:
        print(f"Erreur lors de l'exécution de la force brute : {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erreur générale : {e}")