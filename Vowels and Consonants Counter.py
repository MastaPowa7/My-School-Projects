def main():
    vowels_total = 0
    vowels = ['a','e','i','o','u']
    
    user_input = input('enter text: ')
    for character in user_input:
        if character.isalpha():
            if character in vowels or character.lower() in vowels:
                vowels_total += 1
    
    consonants_total = find_consonants(user_input)
    
    print(f"Vowels = {vowels_total} || Consonants = {consonants_total}")
    
def find_consonants(x):
    consonants_total = 0
    vowels = ['a','e','i','o','u']
    
    for character in x:
        if character.isalpha():
            if character not in vowels and character.lower() not in vowels:
                consonants_total += 1
    
    return consonants_total

main()
