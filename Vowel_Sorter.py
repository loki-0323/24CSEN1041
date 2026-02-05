def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in word:          
        if ch in vowels:     
            count += 1      
    return count

sentence = input("Enter list of words: ")

words = sentence.split()

sorted_words = sorted(words, key=count_vowels, reverse=True)

print("\nWords sorted by vowel count:")
for word in sorted_words:
    print(f"{word} ({count_vowels(word)} vowels)")

Output:
Enter list of words: lokesh akash saran karunaya pranay

Words sorted by vowel count:
karunaya (4 vowels)
lokesh (2 vowels)
akash (2 vowels)
saran (2 vowels)
pranay (2 vowels)
