def counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    words = text.split()
    amount_per_letter = {}
    for word in words:
        word = word.lower()
        n = 0
        while n < len(word):
            
            if word[n] in amount_per_letter:
                amount_per_letter[word[n]] += 1
            else: 
                amount_per_letter[word[n]] = 1
            n += 1
    return amount_per_letter
def sort_inp(dict):
    return dict["num"]
def splitter(unsorted_di):
    sorted_l = []
    temp_di = {}
    for key in unsorted_di:
        temp_di = {}
        temp_di["char"] = key
        temp_di["num"] = unsorted_di[key]
        sorted_l.append(temp_di)
        
    sorted_l.sort(reverse=True, key=sort_inp)
    return sorted_l
