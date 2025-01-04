def main():
    with open('./transcript.txt', 'r') as file:
        transcript_content = file.read()
    word_count = {}
    words = transcript_content.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Word Frequency:", word_count)

if __name__ == "__main__":
    main()
