data.csv: 
==========
The dataset has four columns and 150 records. Each row corresponds one record or one observation. For each row:

FeatureVec
-----------
It is list of numerical values. Length of the list is constant across rows and is equal to the number of features. Each value in the list corresponds to one feature. 

FeatureEmbedding
-------------
It is list of numerical values. Length of the list is constant across rows. The length of the list is the dimension of a (latent) state of the features.


Explanation
-----------
It is a list of tuples. Each tuple is in the following format.
Examples. SUppose the list is [(L,1,0.5), (R,2,-0.5)]. It can be read as follows: 

Pick Feature 1 (feature index starts at 1, not 0). It is less than 0.5, so to go to the left branch of tree.

Pick Feature 2 (feature index starts at 1, not 0). It is NOT less than -0.5, so to go to the right branch of tree.

Label
-----
The class the record belongs to. The class label can be [0,1,2] for a three class classification problem