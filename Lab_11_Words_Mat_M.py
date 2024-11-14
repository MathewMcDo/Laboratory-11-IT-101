words = []
for i in range(10):
    word = input(f"Enter a word{i + i}")
    words.append(word)
    
while True:
    airplane = input("Enter a length:")
    if airplane.isdigit():
        airplane = int(airplane)
        break
    else:
        print("Invalid input, please enter a number.")
        
pairing_words = [word for word in words if len(word) >- longetivity]
print("pairing words")
if pairing_words:
    print("that is very cool my neighbors")
else:
    print("No words found with the given length")