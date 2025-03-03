
!pip install -qU gensim

import numpy as np
np.random.seed(0)

CONTEXT_SIZE = 2

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu sem
scelerisque, dictum eros aliquam, accumsan quam. Pellentesque tempus, lorem ut
semper fermentum, ante turpis accumsan ex, sit amet ultricies tortor erat quis
nulla. Nunc consectetur ligula sit amet purus porttitor, vel tempus tortor
scelerisque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
posuere cubilia curae; Quisque suscipit ligula nec faucibus accumsan. Duis
vulputate massa sit amet viverra hendrerit. Integer maximus quis sapien id
convallis. Donec elementum placerat ex laoreet gravida. Praesent quis enim
facilisis, bibendum est nec, pharetra ex. Etiam pharetra congue justo, eget
imperdiet diam varius non. Mauris dolor lectus, interdum in laoreet quis,
faucibus vitae velit. Donec lacinia dui eget maximus cursus. Class aptent taciti
sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus
tincidunt velit eget nisi ornare convallis. Pellentesque habitant morbi
tristique senectus et netus et malesuada fames ac turpis egestas. Donec
tristique ultrices tortor at accumsan.
""".split()

text

len(text)

# create skipgrams
skipgrams = []
for i in range(CONTEXT_SIZE, len(text) - CONTEXT_SIZE):
  array = [text[j] for  j in np.arange(i - CONTEXT_SIZE, i + CONTEXT_SIZE + 1) if j != i]
  skipgrams.append((text[i], array))

print(skipgrams[0:2])

from gensim.models.word2vec import Word2Vec

# create word2vec

model = Word2Vec([text],
                 sg=1,   # we're using skipgram
                 vector_size=10,
                 min_count=0,
                 window=2, # the context size
                 workers=1,
                 seed=0)
print(f"Shape of W_embed: {model.wv.vectors.shape}")

# train model
model.train([text], total_examples=model.corpus_count, epochs=10)

print('\nWord embedding = ')
print(model.wv[0])





