import re


def prepare(string):
    gesplit = re.split(r'[!|?|"|,|.|(|)|<|>]', string)
    newline = " ".join(gesplit)
    newline1 = newline.split()
    return newline1


def ngrams(seq, n=3):
    ngrams_list = []
    i = 0
    while i <= len(seq) - n:
        ngram = ""
        ngram = seq[i: i + n]
        ngrams_list.append(ngram)
        i += 1
    return ngrams_list


# print(prepare("Lorum ipsum dolor sit amet"))
# print(ngrams("<Lorum>"))


def ngram_table(text, n=3, limit=0):
    word_list = prepare(text)
    # output: ['Lorum', 'ipsum', 'dolor', 'sit', 'amet']
    ngram_dict = {}

    for index, item in enumerate(word_list):
        tokenized_word = "<" + item + ">"
        word_list[index] = tokenized_word
        # Logic om van woord naar ngram te gaan (hopelijk zonder een nieuwe for-loop)
        ngram_list = ngrams(word_list[index], n)

        for index_2, ngram in enumerate(ngram_list):
            # Ngram in dict zetten of frequentie aanpassen als duplicate
            if ngram in ngram_dict:
                # duplicate: +1 bij freq
                ngram_dict[ngram] += 1
            else:
                ngram_dict[ngram] = 1

            index_2 += 1

        index += 1
    #TODO: Dict orderen en limit implementeren
    return ngram_dict


print(ngram_table("hiep, hiep, hoera!"))
# Output:
# {'<hi': 2, 'hie': 2, 'iep': 2, 'ep>': 2, '<ho': 1, 'hoe': 1, 'oer': 1, 'era': 1, 'ra>': 1}
