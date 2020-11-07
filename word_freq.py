"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
"""
import nltk
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Top 100 words in a file")
    parser.add_argument("filename",
                        help="Path to file to get top 100 words from")
    # input_file = Path(parser.parse_args().file)
    # file_path = "C:\\Program Files (x86)\\YogaDNS\\public-resolvers.md"
    args = parser.parse_args()
    with open(args.filename, "r", encoding="utf-8") as file:
        stopwords = set(nltk.corpus.stopwords.words('english'))
        # tokens = nltk.word_tokenize(file_contents.read())
        tokens = nltk.word_tokenize(file.read())
        # Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo
        tokens = [token for token in tokens
                  # removing one-letter words and single-symbol punctuation
                  # I could've removed all punctuation,
                  # but I actually prefer to see special symbol combinations
                  # and words which include punctuation
                  # for when I tokenize source code files
                  if len(token) > 1
                  and not token.isnumeric()  # removing numbers
                  and token not in stopwords]  # removing stopwords
        top_100_words = nltk.FreqDist(tokens).most_common(100)
    for word, frequency in top_100_words:
        print(u'{} occurs {} times'.format(word, frequency))
