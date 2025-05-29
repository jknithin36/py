message = "You are a dumb person and a total IDIOT!"
banned_words = ["dumb", "idiot"]


def mute_words(text, banned_list):
    words = text.split(" ")
    for word in range(len(words)):
        clean_word = words[word].lower().re
        if (words[word] in list):
            length = len(words[word])
            new_word = "*" * length
            words[word] = new_word
        
    return words








ans = mute_words(message,banned_words)

print(ans)
# print(mute_words.__globals__)

# print(message.split(" "))