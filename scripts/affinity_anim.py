#!/usr/bin/env python3

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs

import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.animation as animation
import numpy as np
import imageio

# #############################################################################
# Generate sample data
centers = [[1,1], [-1,-1]]
X, labels_true = make_blobs(n_samples=100, centers=centers, cluster_std=0.1,
                            random_state=0)

# #############################################################################
# Compute Affinity Propagation
colors = 'bgrcmykbgrcmykbgrcmykbgrcmyk'

def plot_for_iterations(i):
    print("Iteration %d", i)
    af = AffinityPropagation(max_iter=i, damping=0.5).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(-1.5, 1.5)
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        ax.plot(X[class_members, 0], X[class_members, 1], col + '.')
        ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
        for x in X[class_members]:
            ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
    plt.title('Colorized clusters after %d iterations' % i)
    
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image
    
kwargs_write = {'fps':5.0, 'quantizer':'nq'}
imageio.mimsave('./ap_iterations.mp4', [plot_for_iterations(i) for i in range(15,201)], fps=10)