import re

while (True):
    # sees what the username is
    print('To determine vowels, evens or odds.\nMust enter a username.\nEnter username:', end=' ')
    username = ""
    while (username == "" or username == " "):
        username = str(input())
        if (username == ""):
            print('Must enter a username.')
        if (username == " "):
            print('Must enter a username.')

    # removes any character that is NOT in the alphabet like underscores or numbers
    vowelUsername = ''
    vowelUsername = re.sub("[^A-Za-z]", "", username)
    firstCharacter = vowelUsername[0]

    # checks if clean username is vowels
    isVowel = False
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in vowels:
        if (firstCharacter == i):
            isVowel = True

    # removes spaces from username for counting odds/evens
    usernameNoSpaces = ''
    usernameNoSpaces = re.sub(" ", "", username)

    # finds how many characters username has and if even or odd
    isOdds = False
    isEvens = False
    usernameLength = len(usernameNoSpaces)

    if (usernameLength % 2 == 0):
        isEvens = True
    else:
        isOdds = True

    # print the answers
    if (isVowel == True):
        print(f'{username} is vowels. ({usernameLength})\n')
    elif (isEvens == True):
        print(f'{username} is evens. ({usernameLength})\n')
    elif (isOdds == True):
        print(f'{username} is odds. ({usernameLength})\n')