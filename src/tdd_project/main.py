import argparse

def main(transcript_content=None, transcript_file=None):
    if transcript_file:
        with open(transcript_file, 'r') as file:
            transcript_content = file.read()
    word_count = {}
    words = transcript_content.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    min_count_threshold = 3
    print("Word frequency count:")
    for word, count in word_count.items():
        if count > min_count_threshold:
            print(f"{word} ({count}): {'#' * count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process transcript data.")
    parser.add_argument('--transcript_file', type=str, help='Path to the transcript file')
    parser.add_argument('--transcript_content', type=str, help='Transcript content as a string')
    args = parser.parse_args()

    main(transcript_content=args.transcript_content, transcript_file=args.transcript_file)
