def main():
    with open('./transcript.txt', 'r') as file:
        transcript_content = file.read()
    word_count = {}
    words = transcript_content.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Word frequency count:")
    min_count_threshold = 3
    for word, count in word_count.items():
        if count > min_count_threshold:
        print(f"{word} ({count}): {'#' * count}")

if __name__ == "__main__":
    main()
