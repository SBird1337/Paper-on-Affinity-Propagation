#!/usr/bin/env python3

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs

# #############################################################################
# Generate sample data
centers = [[0.4,0.4], [-0.4,-0.4], [0.4,-0.4]]
X, labels_true = make_blobs(n_samples=30, centers=centers, cluster_std=0.1,
                            random_state=0)

# #############################################################################
# Plot initial
import matplotlib.pyplot as plt
from itertools import cycle
import tikzplotlib

plt.close('all')
plt.figure(1)
plt.clf()

for p in X:
    plt.plot(p[0], p[1], 'k.')
plt.title('Unclustered dataset')
tikzplotlib.save("figures/ap_unclust.tex")
# #############################################################################
# Compute Affinity Propagation
af = AffinityPropagation(max_iter=1000, damping=0.5).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels,
                                           average_method='arithmetic'))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

# #############################################################################
# Plot result

plt.close('all')
plt.figure(2)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in X[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
tikzplotlib.save("figures/ap_clust.tex")
