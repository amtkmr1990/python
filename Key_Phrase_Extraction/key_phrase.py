from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()
a = '''
India (IAST: Bhārat), also known as the Republic of India (IAST: Bhārat Gaṇarājya),[18][e] is a country in South Asia. It is the seventh largest country by area and with more than 1.3 billion people, it is the second most populous country and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the northeast; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives, while its Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia.

The Indian subcontinent was home to the urban Indus Valley Civilisation of the 3rd millennium BCE. In the following millennium, the oldest scriptures associated with Hinduism began to be composed. Social stratification, based on caste, emerged in the first millennium BCE, and Buddhism and Jainism arose. Early political consolidations took place under the Maurya and Gupta empires; later peninsular Middle Kingdoms influenced cultures as far as Southeast Asia. In the medieval era, Judaism, Zoroastrianism, Christianity, and Islam arrived, and Sikhism emerged, all adding to the region's diverse culture. Much of the north fell to the Delhi Sultanate; the south was united under the Vijayanagara Empire. The economy expanded in the 17th century in the Mughal Empire. In the mid-18th century, the subcontinent came under British East India Company rule, and in the mid-19th under British crown rule. A nationalist movement emerged in the late 19th century, which later, under Mahatma Gandhi, was noted for nonviolent resistance and led to India's independence in 1947.

In 2017, the Indian economy was the world's sixth largest by nominal GDP[19] and third largest by purchasing power parity.[15] Following market-based economic reforms in 1991, India became one of the fastest-growing major economies and is considered a newly industrialised country. However, it continues to face the challenges of poverty, corruption, malnutrition, and inadequate public healthcare. A nuclear weapons state and regional power, it has the second largest standing army in the world and ranks fifth in military expenditure among nations. India is a federal republic governed under a parliamentary system and consists of 29 states and 7 union territories. A pluralistic, multilingual and multi-ethnic society, it is also home to a diversity of wildlife in a variety of protected habitats.
'''
# Extraction given the text.
r.extract_keywords_from_text(a)

# Extraction given the list of strings where each string is a sentence.
#r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
r.get_ranked_phrases()

# To get keyword phrases ranked highest to lowest with scores.
r.get_ranked_phrases_with_scores()