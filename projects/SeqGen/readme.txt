========
SEQ-GEN
========



Description
============
An atomic Explanation is represented in the form of a tuple (feature, relation, cutpoint). For example, Sepal Length is less than 0.5cm, when the flower belongs to Setosa. This is represented as (L, 1, 0.5).

feature: Sepal Length (indexed as 1)
cutpoint: 0.5
relation: L for left (less than)

A compund explanation can be represented as

(L, 1, 0.5) ^ (R, 2, -0.5)

When a label is known, that observation can be stated with an implication

(L, 1, 0.5) ^ (R, 1, 0.5) ==> 0

If you only look at the "relations", it looks a like a sequence. [L,R]. We have a built an RNN that, produces such sequences. 

You can use the following function to produce a sequence (one character at a time)

# initialite the curr_char state
curr_char=[1,0,0,0]
feature_embedding = # for a given record, load the feature_embedding
# EOS is end-of-sequence. When True, reached end-of-sentence.
EOS = False
while !EOS:
	next_char, prob, EOS  = predict_next(feature_embedding, curr_char=[1,0,0,0])
	curr_char = next_char
	#  flag is False


Problem
=======

Write a program to generate a sequence using k-step ahead search technique. Treat k=1 is the baseline (pseudo code given above).


Results
=======
Define the heuristics/ cost function to perform the search. Discuss various options.Compare the performance of various sequence generation search techniques using BLEU, bi-grams, Levenshtein Distance.

Optional
========
While comparing the generated sequences, account the predicted label also. That is, two different paths can lead to the same conclusion. In which case, syntactically those two sequences are different, but they convey the same meaning. Those two sentences permutation invariant w.r.t the meaning.



Data
=====
/../data/data.csv
You may need to all columns in the dataset.
Initialize curr_chat with [1,0,0,0]

code
=====
/code/predict.py
you can import the predict_next function or use run FLASK server on localhost and make API an call if you are programming in some other language (other than python)