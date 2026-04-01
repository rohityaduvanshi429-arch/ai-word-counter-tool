print("== AI WORD COUNTER TOOL ==")
print("- Word count\n- Character count\n- Sentence detection\n- Average word length")

while True:
    text = input("\nEnter your text (type 'exit' to quit): ")

    if text.lower() == "exit":
        print("bye")
        break

    if text.strip() == "":
        print("enter valid text")
        continue

    else:
        chars = len(text)
        chars_no_space = len(text.replace(" ", ""))
        sentence = text.count(".") + text.count("!") + text.count("?")
        word_list = text.lower().split()

        total_chars = sum(len(word) for word in word_list)

        print("\nresult")
        print("chars:", chars)
        print("chars no space:", chars_no_space)
        print("sentence:", sentence)
        print("Total words:", len(word_list))

        if len(word_list) > 0:
            print("Avg word length:", total_chars / len(word_list))
        else:
            print("avg=0")