from structural.facade.logic import TextComparer


data_to_compare = (
    ("I was old", "I was young"),
    ("123", "123"),
    ("Long time no see, hello my dear friend", "Long time no see, hello my dear enemy"),
    ("Operation completed at 18:23:12", "Operation completed at 15:58:03"),
)


def main() -> None:
    for text1, text2 in data_to_compare:
        print(f"Text similarity between '{text1}' and '{text2}'")
        text_comparer = TextComparer(text1, text2)
        similarity = text_comparer.compare_text()
        similarity_after_filter = text_comparer.compare_text_with_filter()
        print(f"'{similarity:.2f}' Without filter and '{similarity_after_filter:.2f}' With filter", end="\n\n")


if __name__ == "__main__":
    main()
