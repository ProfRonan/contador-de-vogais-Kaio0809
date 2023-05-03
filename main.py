#This program counts the number of vowels in a string.

def count_vowels(string:str) -> int:
    count = 0
    for i in range(0, len(string)):
        if string[i] == 'a' or string[i]== 'e' or string[i]== 'i' or string[i]== 'o' or string[i]== 'u' or string[i] == 'A' or string[i]== 'E' or string[i]== 'I' or string[i]== 'O' or string[i]== 'U':
            count += 1
    return(count)

if __name__ == "__main__":
    n = str(input('N: '))
    print(count_vowels(n))