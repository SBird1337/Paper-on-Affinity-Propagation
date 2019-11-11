# Clustering with Affinity Propagation and its applications

## Questions to answer

1. What is the idea behind Affinity Propagation (AP) and how does AP work?
   Explain the steps and objects (matrices) that are involved.

   Affinity propagation can find a set of clusters and their exemplars (Datapoints that are responsible for the formation of a cluster)

   It works by taking measures of similarity as input, and exchanges real-valued messages until clusters emerge. It uses matrices to describe the current state of the algorithm:

   Similarity Matrix, s(i,k) is initially given, describes how suited data point k is an exemplar of i. Depending on the metric it can e.g. be set to the negative euclidian distance (squared error) - It may also be set by hand.

   Responsability Matrix, r(i,k) - Messages sent from data point i to a candidate exemplar reflects how suited candidate exemplar k is to be an exemplar of i.

   Availability Matrix, a(i,k) - Messages sent from candidate exemplar k to data point i reflects how suited k is to be chosen as an exemplar for i.

   The message matricies are computed in each step according to rules specified in the paper. The similarity matrix is set once at the beginning. Special values s(k,k) are called preferences and may be set to a common value, depending on the outcome one would expect from the algorithm. The message-matrices are initialized to zero, and can be viewed as log-probability tables.

   Each step computes the message matricies, and the algorithm can be terminated after n steps, or when the matricies converge. The exemplars are extracted from the message-matricies using the rule r(i,i) + k(i,i) > 0

2. How can we influence the number of clusters that are found and
   how can we increase/decrease the chance that a certain data point is selected as exemplar?

   We can set the preference values s(k,k). If we want to increse the chance for a point to be a cluster, we choose a smaller preference, and vice-versa.

3. What are the differences to classical clustering techniques like
   K-center clustering or K-means?

   Affinity propagation does not need a fixed number of exemplars, they emerge from the algorithm directly. It can be applied to problems where similarities are not symmetrical, too. It only uses local computations per step, making it faster than k-means clustering and the results show less errors, according to the paper.

4. What typical applications do exist?

   The paper mentions clustering of faces, genes, sentences, and cities to be easily accessed via airline travel. But generally any application that requires clustering of data points could opt for affinity propagation.
