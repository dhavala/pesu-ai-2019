========
DESCRIPTION
========

We are trying to understand how to develop Black-Box solutions that provide explanations. But what is an explanation? If there is one, how to represent it? And it exists, how to reason about them? The three problems posed in this project try to address them.

========
Premise
========

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

Refer to individual project problems for specifics.

========
SUBMITTING A SOLUTION
========


0. fork the repository

1. create a new directory in the following format
projects/<project_name>/solutions/<team_name>/

If you are working in SeqGen problem, and there is a 
there is three member team (Om, Jai, Jagadish) working on it, then create a directory
./SeqGen/solutions/om_jai_jagadish/

2. put all your code in this subdirectory

3. raise a pull request


========
TERMS and CONDITIONS
========
You agreee that your solutions will made public under MIT License.
Absolutely no plagiarism. If you are using some code, please provide attribution. Be generous.