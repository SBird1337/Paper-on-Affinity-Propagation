# Literature research results for the topic "Clustering with Affinity Propagation and its Applications"

Based on the original paper on Affinity Propagation (Clustering with Affinity Propagation and its Applications by Frey, Brendan J and Dueck, Delbert) I conducted research on other research in this topic. The results I found are mainly following up on the application of the originally proposed algorithm, but also try to compare it to conventional methods, or try to propose follow-up algorithms that can eliminate some of the downsides of Affinity Propagation. I also did some research on software implementations of the original Affinity Propagation (AP) clustering algorithm in order to further understand how the parameters affect the convergence and sanity of the clustered datasets.

## Papers

A BibTex version of the research results can be found in the file `literature.bib` as requested. Here follows a short description of the papers I found, and why they seem to be interesting in the context of this seminar.

### Clustering by passing messages between data points (Frey, Brendan J and Dueck, Delbert)

This is the paper that was presented to me by my seminar instructor. It describes the initial proposal of AP Clustering and is crucial for anything that wants to do further research on this topic. It also compares its implementation with conventional methods, such as k-means.

### Adaptive affinity propagation clustering (Wang, Kaijun and Zhang, Junying and Li, Dan and Zhang, Xinna and Guo, Tao)

This paper tries to build on AP by tackling 2 crucial challenges/limitations: Finding an optimal `preference` parameter for AP, and eliminating oscilations in the convergence behavior in the originally proposed AP implementation. It proposes a new algorithm called `Adaptive Affinity Propagation` and compares presents the results on some example data sets.

### Fast algorithm for affinity propagation (Fujiwara, Yasuhiro and Irie, Go and Kitahara, Tomoe)

Another try on improving the classic AP clustering method. This paper proposes a fast implementation of the AP clustering algorithm without sacrificing any accuracy or convergence compared to the original algorithm. It does so based on two key ideas: Pruning unnecessary message exchanges, and computing the convergence values of those pruned messages using unpruned ones.

### Markov clustering versus affinity propagation for the partitioning of protein interaction graphs (Vlasblom, James and Wodak, Shoshana J)

Frey et al. already mention how AP could be used in biomedical applications, specifically gene detection. This tackles another biomedical problem: partitioning of protein interaction graphs, and compares it to the conventional method for this problem, which is Markov clustering. Even though the results of the study sound rather deminishing, I decided to include this paper anyways, to show that AP is not the go-to for each and any clustering problem in existance.

### Fingerprint indoor positioning algorithm based on affinity propagation clustering (Tian, Zengshan and Tang, Xiaomou and Zhou, Mu and Tan, Zuohong)

This paper is a direct application of the AP clustering algorithm. It describes and proposes indoor positioning using reference points of WLAN data. The results show an improvement through several metrics in comparison to previous algorithms.

### Optimization of traveling salesman problem using affinity propagation clustering and genetic algorithm

Sounding a bit obscure at first, this tries to solve one of the classic np-complete problems, the TSP problem, using AP clustering. It makes use of genetic algorithms, which where used before to optimize TSP, and shows that AP can improve those results both in the error of the produced solution, as well as the computational time based on different data sets.
