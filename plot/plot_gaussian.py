import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


def skew_norm_pdf(x, e=0, w=1, a=0):
    # adapated from:
    # http://stackoverflow.com/questions/5884768/skew-normal-distribution-in-scipy
    t = (x-e) / w
    return 2.0 * w * stats.norm.pdf(t) * stats.norm.cdf(a*t)


mu = -1
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
location = 0.0
scale = 1.0
plt.figure(figsize=(6, 6))
plt.plot(x, skew_norm_pdf(x, location, scale, -3),
         linewidth=3, color='orange')
plt.xticks([])
plt.yticks([])
# plt.xlim(-4, 4)
# plt.axis('off')
plt.show()
plt.savefig('gaussian1.png')

mu = 1
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.figure(figsize=(6, 6))
plt.plot(x, skew_norm_pdf(x, location, scale, 0), linewidth=3, color='green')
plt.xticks([])
plt.yticks([])
# plt.xlim(-4, 4)
# plt.axis('off')
plt.show()
plt.savefig('gaussian2.png')
