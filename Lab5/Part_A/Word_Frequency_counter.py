
text = input("Enter a paragraph: ")

# Convert into lowercase
text = text.lower()

# Remove punctuation
punctuation = ".,!?;:'\"()-"

for ch in punctuation:
    text = text.replace(ch, "")

words = text.split()

if len(words) == 0:
    print("No words entered!")

else:
    # Count word frequency
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print("Word Counts:", freq)

    # Top N words
    n = int(input("Enter N: "))

    sorted_words = sorted(
        freq.items(),
        key=lambda x: (-x[1], x[0])
    )

    print("Top N Words:", sorted_words[:n])

    # Words appearing once
    once = []

    for word in freq:
        if freq[word] == 1:
            once.append(word)

    print("Words appearing once:", sorted(once))

    # Invert dictionary
    inverted = {}

    for word, count in freq.items():
        if count not in inverted:
            inverted[count] = []

        inverted[count].append(word)

    for count in inverted:
        inverted[count].sort()

    print("Inverted Dictionary:", inverted)

    # Group words by length
    length_group = {}

    for word in freq:
        length = len(word)

        if length not in length_group:
            length_group[length] = []

        length_group[length].append(word)

    print("Words by Length:", length_group)

    # Search word
    search = input("Enter word to search: ").lower()

    if search in freq:
        print("Frequency:", freq[search])
    else:
        print("Word not found!")
