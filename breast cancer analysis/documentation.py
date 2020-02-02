the documentation used for linear SVM is below. I will add further sources if necessary to further develop the algorithm.

"""
Code for structuring linear SVM classifier:
https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html#sphx-glr-auto-examples-svm-plot-iris-svc-py

Interesting explanation of C parameter in linear SVM:
https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel

Documentation:
sklearn.svm.LinearSVC - https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
arange - https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
ravel - https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html
contourf - https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.contourf.html
pyplot.subplots_adjust - https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
ndarray (n-dim array).flatten() - https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html

StackOverflow links:
add legend names to plot_decision_regions - https://stackoverflow.com/questions/46194971/add-legend-names-to-a-svm-plot-in-matplotlib
mlxtend + DataFrame - https://stackoverflow.com/questions/49167961/mlextend-plot-decision-regions-with-model-fit-on-pandas-dataframe
expected 2D array, got 1D: https://stackoverflow.com/questions/45554008/error-in-python-script-expected-2d-array-got-1d-array-instead

clf meaning - https://stackoverflow.com/questions/34540017/what-does-clf-mean-in-machine-learning
np.ravel() - https://stackoverflow.com/questions/45108464/can-someone-explain-this-line-z-clf-predict-probanp-c-xx-ravel-yy-ravel
TypeError: zip argument #1 must support iteration -
https://stackoverflow.com/questions/14049860/typeerror-zip-argument-1-must-support-iteration
slice concatenation - https://stackoverflow.com/questions/33491703/meaning-of-x-x-1-in-python/33491724

mlxtend GitHub examples:
http://rasbt.github.io/mlxtend/user_guide/plotting/plot_decision_regions/
http://rasbt.github.io/mlxtend/api_subpackages/mlxtend.plotting/#plot_decision_regions
http://rasbt.github.io/mlxtend/user_guide/plotting/plot_decision_regions/#example-10-providing-your-own-legend-labels
"""

# Documentation for neural network:

Model from: 
https://dev.to/shamdasani/build-a-flexible-neural-network-with-backpropagation-in-python

# d-types: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
# np.amax: https://docs.scipy.org/doc/numpy/reference/generated/numpy.amax.html
# np.random.randn: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
# array[:-n or None]: https://stackoverflow.com/questions/15715912/remove-the-last-n-elements-of-a-list
# itertools and product: https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
# array[:n or None]: https://stackoverflow.com/questions/33626623/the-most-efficient-way-to-remove-first-n-elements-in-a-list
