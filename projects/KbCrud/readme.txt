========
KB-CRUD
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




Problem
=======
Represent these explanations in a KB.  Then, given a new compound explanation (a list of tuples, with an implicit conjunction), test its entailment in the KB. Implement the reasoner. For example

Petal length is 0.4, Sepal Width is -0.5. Does the flower belong to the class Virginica?
When Sepal Length is less 0.5, what should be Petal Length so that, the flower belongs to the class Setosa?


Results
=======
Provide an interface such that, given an explanation, it tests the entailment of the explanation. Discuss the technique being used, whether it is decidable or not. Discuss the soundness, completeness, and complexity (space and time), and accuracy of your solution.

Data
=====
/../data/data.csv
You do not need to use "FeatureEmbedding" coulmn
