def main():
    with open('./transcript.txt', 'r') as file:
        transcript_content = file.read()
    print("Transcript content loaded.")
    print("Hello, Cruel World!")

if __name__ == "__main__":
    main()
