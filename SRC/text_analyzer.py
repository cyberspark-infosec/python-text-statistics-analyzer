import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter 
import json

def load_text(filepath):


    with open (filepath, 'r', encoding='utf-8') as file:
        text=file.read()

    return text


def clean_text(text):

    start_marker="*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker="*** END OF THE PROJECT GUTENBERG EBOOK"

    if start_marker in text:
        text = text.split(start_marker, 1)[1]

    if end_marker in text:
        text=text.split(end_marker,1)[0]

    text = text.replace("\r\n", "\n")
    text=re.sub(r"\n{2,}","\n",text)
    text=re.sub(r"\n{3,}","\n\n",text)

    return text.strip()


def calculate_basic_stats(text):

    words = text.split()

    character_count=len(text)
    word_count=len(words)

    sentences=re.split(r'[.!?]+',text)
    sentences=[
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    
    ]

    sentence_count=len(sentences)

    if word_count>0:
        average_word_lenght=np.mean(
            [len(word) for word in words]
        )
    else:
        average_word_lenght=0

    if sentence_count>0:
        average_sentence_length=np.mean(
            [len(sentence.split()) for sentence in sentences]
        )
    else:
        average_sentence_length=0

    return{
        "characters":character_count,
        "words":word_count,
        "sentences":sentence_count,
        "average_word_length": average_word_lenght,
        "average_sentence_length":average_sentence_length,
    }


def calculate_word_frequency(text):
    words=re.findall(r"[A-Za-z]+", text.lower())
    word_frequency = Counter(words)

    return word_frequency


if __name__=="__main__":

    input_file="Data/Raw/alice_in_wonderland.txt"

    text=load_text(input_file)

    cleaned_text=clean_text(text)
    with open("Data/Processed/cleaned_text.txt", "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    stats=calculate_basic_stats(cleaned_text)
    stats_df = pd.DataFrame([stats])

    stats_df.to_csv( 
    "Data/Processed/document_stats.csv",
    index=False
               )
    word_frequency = calculate_word_frequency(cleaned_text)

    print("===================================")
    print("     TEXT STATISTICS ANALYZER")
    print("===================================")

    print("\nFile loaded successfully!")

    print("\nBasic Statistics:")
    print("-----------------------------")
    print("Characters:", stats["characters"])
    print("Words:", stats["words"])
    print("Sentences:", stats["sentences"])
    print(
        "Average word length:",
        round(stats["average_word_length"], 2)
    )
    print(
        "Average sentence length:",
        round(stats["average_sentence_length"], 2)
    )

    print("\nTop 20 Most Frequent Words:")
    print("-----------------------------")

    for word, frequency in word_frequency.most_common(20):
        print(word, ":", frequency)

          # Regex Pattern Extraction

def extract_patterns(text):

    
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    phone_numbers = re.findall(
        r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b',
        text
    )

    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    dates = re.findall(
        r'\b(?:'
        r'\d{2}/\d{2}/\d{4}'
        r'|\d{2}-\d{2}-\d{4}'
        r'|(?:January|February|March|April|May|June|July|August|September|October|November|December)'
        r' \d{1,2} \d{4}'
        r')\b',
        text
    )

    currencies = re.findall(
        r'[$£€]\s?\d+(?:\.\d+)?',
        text
    )

    hashtags = re.findall(
        r'#[A-Za-z0-9_]+',
        text
    )

    mentions = re.findall(
        r'@[A-Za-z0-9_]+',
        text
    )

    return {
        "emails": emails,
        "phone_numbers": phone_numbers,
        "urls": urls,
        "dates": dates,
        "currencies": currencies,
        "hashtags": hashtags,
        "mentions": mentions
    }
   
patterns = extract_patterns(cleaned_text)
with open("Data/Processed/patterns.json", "w", encoding="utf-8") as file:
    json.dump(patterns, file, indent=4)

print("REGEX PATTERN EXTRACTION")
print("========================")

for pattern_type, results in patterns.items():
    print(f"\n{pattern_type}: {len(results)} found")

    if results:
        print(results[:10])
        #numpy///
words = re.findall(r"[A-Za-z]+", cleaned_text.lower())

word_lengths = np.array([len(word) for word in words])

print("WORD LENGTH STATISTICS")
print("***********************")

print("Mean:",np.mean(word_lengths))
print("Median:",np.median(word_lengths))
print("Standard deviation:",np.std(word_lengths))
print("25th percentile:",np.percentile(word_lengths, 25))
print("50th Percentile:",np.percentile(word_lengths, 50))
print("75th percentile:",np.percentile(word_lengths, 75))



#character frequency
characters = Counter(cleaned_text.lower())

print("CHARACTER FREQUENCY")
print("###################")

for character, count in characters.most_common(15):
    print(repr(character), ":", count)

#pandas 
word_counts = Counter(words)

word_data = []

for word, frequency in word_counts.items():
    word_data.append({
        "word": word,
        "frequency": frequency,
        "length": len(word),
        "first_char": word[0],
        "vowel_count": sum(1 for letter in word if letter in "aeiou")
    })

word_df = pd.DataFrame(word_data)
word_df = word_df.set_index("word")

word_df.head()

print("TOP 50 MOST FREQUENT WORDS")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
print(word_df.sort_values("frequency", ascending=False).head(50))

print("\nWORDS LONGER THAN 10 CHARACTERS")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(word_df[word_df["length"] > 10])

print("\nAVERAGE FREQUENCY BY WORD LENGTH")
print("+++++++++++++++++++++++++++++++++++")
print(word_df.groupby("length")["frequency"].mean())

print("\nAVERAGE FREQUENCY BY FIRST CHARACTER")
print("====================================")
print(word_df.groupby("first_char")["frequency"].mean())

print("\nWORD LENGTH AND FIRST CHARACTER CROSSTAB")
print("========================================")

crosstab = pd.crosstab(
    word_df["length"],
    word_df["first_char"]
)

print(crosstab)

#matplotlib
top_20 = word_df.sort_values("frequency", ascending=False).head(20)

plt.figure(figsize=(10, 7))

plt.barh(top_20.index[::-1], top_20["frequency"][::-1])

# Show frequency numbers on the bars
for i, value in enumerate(top_20["frequency"][::-1]):
    plt.text(value + 10, i, str(value), va="center")

plt.xlabel("Frequency")
plt.ylabel("Word")
plt.title("Top 20 Most Frequent Words")

plt.tight_layout()
plt.show()
plt.savefig("PLOTS/top_20_words.png", dpi=300, bbox_inches="tight")


# Word Length Distribution

# Plot 2: Word Length Distribution with Normal Curve

mean_length = np.mean(word_lengths)
std_length = np.std(word_lengths)

plt.figure(figsize=(10, 6))

# Histogram
plt.hist(
    word_lengths,
    bins=range(1, max(word_lengths) + 2),
    density=True,
    edgecolor="black"
)

# Normal curve
x = np.linspace(min(word_lengths), max(word_lengths), 200)

normal_curve = (
    1 / (std_length * np.sqrt(2 * np.pi))
) * np.exp(
    -((x - mean_length) ** 2) / (2 * std_length ** 2)
)

plt.plot(x, normal_curve, linewidth=2)

plt.xlabel("Word Length")
plt.ylabel("Density")
plt.title("Word Length Distribution with Normal Curve")

plt.tight_layout()

plt.savefig(
    "PLOTS/word_length_normal_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Top 15 Characters

character_counts = Counter(cleaned_text.lower())

top_characters = character_counts.most_common(15)

characters = []

for character, frequency in top_characters:
    if character == " ":
        characters.append("[space]")
    else:
        characters.append(character)

frequencies = [item[1] for item in top_characters]

plt.figure(figsize=(10, 6))

plt.bar(characters, frequencies)

plt.xlabel("Character")
plt.ylabel("Frequency")
plt.title("Top 15 Most Frequent Characters")

plt.tight_layout()

plt.savefig("PLOTS/top_15_characters.png", dpi=300, bbox_inches="tight")

plt.show()

# Sentence Length Distribution

sentences = re.split(r'[.!?]+', cleaned_text)

sentence_lengths = []

for sentence in sentences:
    sentence_words = re.findall(r"[A-Za-z]+", sentence)
    
    if sentence_words:
        sentence_lengths.append(len(sentence_words))

print("\nSENTENCE LENGTH ANALYSIS")
print("========================")

print("Shortest sentence:", np.min(sentence_lengths))
print("Longest sentence:", np.max(sentence_lengths))

print("\nVOWEL AND CONSONANT ANALYSIS")
print("============================")

letters = [char.lower() for char in cleaned_text if char.isalpha()]

vowels = sum(1 for char in letters if char in "aeiou")
consonants = sum(1 for char in letters if char not in "aeiou")

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Vowel/Consonant Ratio:", np.divide(vowels, consonants))

plt.figure(figsize=(10, 6))

plt.hist(sentence_lengths, bins=20, edgecolor="black")

plt.xlabel("Number of Words in Sentence")
plt.ylabel("Number of Sentences")
plt.title("Sentence Length Distribution")

plt.tight_layout()

plt.savefig("PLOTS/sentence_length_distribution.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Sentence Length Boxplot

plt.figure(figsize=(8, 6))

plt.boxplot(sentence_lengths)

plt.ylabel("Number of Words")
plt.title("Sentence Length Boxplot")

plt.tight_layout()

plt.savefig("PLOTS/sentence_length_boxplot.png",
            dpi=300, bbox_inches="tight")

plt.show()

# Letters vs Punctuation

letters_count = sum(1 for char in cleaned_text if char.isalpha())
punctuation_count = sum(1 for char in cleaned_text if char in ".,!?;:'\"-()[]")

labels = ["Letters", "Punctuation"]
values = [letters_count, punctuation_count]

plt.figure(figsize=(8, 6))

plt.bar(labels, values)

plt.xlabel("Character Type")
plt.ylabel("Count")
plt.title("Letters vs Punctuation")

for i, value in enumerate(values):
    plt.text(i, value + 100, str(value), ha="center")

plt.tight_layout()

plt.savefig("PLOTS/letters_vs_punctuation.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Plot 7: 2x2 Text Analysis Dashboard

plt.figure(figsize=(12, 9))

# 1. Top 10 words
plt.subplot(2, 2, 1)

top_10 = word_df.sort_values("frequency", ascending=False).head(10)

plt.barh(top_10.index[::-1], top_10["frequency"][::-1])
plt.xlabel("Frequency")
plt.title("Top 10 Words")


# 2. Word length distribution
plt.subplot(2, 2, 2)

plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2),
         edgecolor="black")


plt.xlabel("Word Length")
plt.ylabel("Count")
plt.title("Word Length Distribution")

# Plot Text Statistics Dashboard

plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
top_10 = word_df.sort_values("frequency", ascending=False).head(10)
plt.barh(top_10.index[::-1], top_10["frequency"][::-1])
plt.xlabel("Frequency")
plt.title("Top 10 Words")

plt.subplot(2, 2, 2)
plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2),
         edgecolor="black")
plt.xlabel("Word Length")
plt.ylabel("Count")
plt.title("Word Length Distribution")

plt.subplot(2, 2, 3)
plt.hist(sentence_lengths, bins=20, edgecolor="black")
plt.xlabel("Words per Sentence")
plt.ylabel("Number of Sentences")
plt.title("Sentence Length Distribution")

plt.subplot(2, 2, 4)
plt.bar(labels, values)
plt.xlabel("Character Type")
plt.ylabel("Count")
plt.title("Letters vs Punctuation")

for i, value in enumerate(values):
    plt.text(i, value + 100, str(value), ha="center")

plt.suptitle("Text Statistics Analysis Dashboard", fontsize=16)

plt.tight_layout()

plt.savefig(
    "PLOTS/text_statistics_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

