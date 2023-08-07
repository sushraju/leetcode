
def find_ngrams(reviews, ngram):
    ngram_dict = {}
    for r in reviews:
        rev_arr = r.split()
        for i in range(len(rev_arr)):
            j = i + 1
            ngram_word = rev_arr[i]
            while ((j < i+ngram) and (j < len(rev_arr))):
                ngram_word = ngram_word + ' ' + rev_arr[j]
                j += 1
            
            if len(ngram_word.split()) == ngram:
                if ngram_word in ngram_dict.keys():
                    ngram_dict[ngram_word] += 1
                else:
                     ngram_dict[ngram_word] = 1
    
    for k,v in ngram_dict.items():
        print(k, v)

def main():
    reviews = ["The cow jumped of the moon", "The moon is far from The cow", "The cow lives nearby"]
    ngram = 5
    find_ngrams(reviews, ngram)

if __name__ == "__main__":
    main()