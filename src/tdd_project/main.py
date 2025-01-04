import argparse

def main(transcript_content=None):
    if transcript_content is None:
        parser = argparse.ArgumentParser(description='Process a transcript file.')
        parser.add_argument('transcript_file', type=str, help='Path to the transcript file')
        args = parser.parse_args()
        with open(args.transcript_file, 'r') as file:
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
    main()  # This will now require a command-line argument or a string input
