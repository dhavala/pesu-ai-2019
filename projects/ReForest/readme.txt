========
RE-FOREST
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

(L, 1, 0.5) ^ (R, 2, -0.5) ==> 0

which translates to

"When Sepal Length is less 0.5 and Petal Width is greater -0.5, the flower belongs to the class Setosa?"

Whn a collection of such explanations is given, can we summarize them into a single decision tree or as a collection of trees (random forests).



Problem
=======

Given a p-dimensional feature vector, and a collection of partial explanations (feature, relation, NULL), impute the missing cutpoint. Use dataset mentioned below, except that, treat the “cutpoint” as missing. Approximate the KB as a decision tree or as a random forest. Discuss under which conditions the approximation error is zero. In other words, determine a data structure which is optimal.


Results
=======
Provide an estimate of the missing cutpoint or provide an interval (lower bound, and upper bound). Discuss the efficiency of your algorithm, in terms of time, space and accuracy. Are the predicted cut points consistent in both datasets?

Summarize all the explnations either as a tree or as a forest (collection of trees). Of course, each compound is also tree. Such trivial trees are not considered as solution.

Optional
========
Prove that, when a decision tree is used to produce those explanations, cut points can be recovered with arbitrary precision.

Prove or Disprove that its space and time complexity is better than a polynomial time algorithm, used in typical first-order reasoning systems that assume KB is in Horn Clauses.


Data
=====
/../data/data.csv
You do not need to use "FeatureEmbedding" coulmn