from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text("""
In computer science, digital image processing is the use of computer algorithms to perform image processing on digital images.
As a subcategory or field of digital signal processing, digital image processing has many advantages over analog image processing. 
It allows a much wider range of algorithms to be applied to the input data and can avoid problems such as the build-up of noise and signal distortion during processing.
Since images are defined over two dimensions (perhaps more) digital image processing may be modeled in the form of multidimensional systems.
""")

# Extraction given the list of strings where each string is a sentence.
#r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases())

# To get keyword phrases ranked highest to lowest with scores.
print(r.get_ranked_phrases_with_scores())

j = Rake()

j.extract_keywords_from_text('''
this is praja. hope you are doing good. i am image processing 
''')

print(j.get_ranked_phrases())

x = r.get_ranked_phrases()
y = j.get_ranked_phrases()

comp = [a for a, b in zip(x, y) if a==b]
print(comp)

