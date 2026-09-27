from text_analyzer import (
    load_text,
    clean_text,
    calculate_basic_stats,
    calculate_word_frequency,
    save_cleaned_text,
    save_stats_to_csv
)


def main():
    """Run the text analysis program."""

    input_file = "Data/Raw/alice_in_wonderland.txt"
    cleaned_file = "Data/Processed/cleaned_alice_in_wonderland.txt"
    stats_file = "Data/Processed/document_statistics.csv"

    text = load_text(input_file)

    cleaned_text = clean_text(text)

    save_cleaned_text(cleaned_text, cleaned_file)

    stats = calculate_basic_stats(cleaned_text)

    save_stats_to_csv(stats, stats_file)

    word_frequency = calculate_word_frequency(cleaned_text)

    print("Text analysis completed.")
    print()
    print("Basic Statistics:")
    
    for key, value in stats.items():
        print(f"{key}: {value}")

    print()
    print("Top 10 Words:")
    print(word_frequency.most_common(10))


if __name__ == "__main__":
    main()