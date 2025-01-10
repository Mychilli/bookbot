def main():
    with open("books/frankenstein.txt") as f:
        case_dictonary = {}
        num_words = 0
        file_contents = f.read()
        word = file_contents.split()
        for i in word:
            num_words += 1
            lower_case_word = "".join(i)
            for j in lower_case_word.lower():
                if j in case_dictonary:
                    case_dictonary[j] += 1
                else:
                    case_dictonary[j] = 1
        print(f"Number of words: {num_words}")
        for k in case_dictonary:
            letter = case_dictonary[k]
            print(f"{k} was found {case_dictonary[k]} times!")

main()