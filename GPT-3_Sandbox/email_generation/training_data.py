# Format of training prompt
defaultPrompt = """Analyse tweets in terms of their sentiment. Depending on their sentiment, classify them as positive, neutral, or negative.


Input: "I'm seriously worried that super intelligent AI will be disappointed in humans."
Output: Sentiment analysis(positive, neutral, negative): negative
###
Input: "I cannot wait for super intelligent AI to emerge and deepen our understanding of the Universe."
Output: Sentiment analysis(positive, neutral, negative): positive
###
Input: "I think it is neither super likely nor super unlikely that the super intelligent AI will emerge one day."
Output: Sentiment analysis(positive, neutral, negative): neutral
###
Input: "Super intelligent AI is going to be the most exciting discovery in human history."
Output: Sentiment analysis(positive, neutral, negative): positive


Input: {}

Output: """