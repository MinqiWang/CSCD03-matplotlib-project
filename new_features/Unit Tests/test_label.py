import collections
import platform
from unittest import mock

import numpy as np
import pytest

from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.transforms as mtransforms
import matplotlib.collections as mcollections
from matplotlib.legend_handler import HandlerTuple
import matplotlib.legend as mlegend
from matplotlib.cbook.deprecation import MatplotlibDeprecationWarning
from matplotlib import rc_context

@image_comparison(baseline_images=['label_auto1'])
def test_label_auto1():
    'Test automatic label placement'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot([1,2,3], label="label1", color="#1f77b4")
    # The label_line() method will automatically place the label
    ax.label_line()

@image_comparison(baseline_images=['label_auto2'])
def test_label_auto2():
    'Test automatic complete label placement'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot([1,2,3], color="#1f77b4")
    line2, = ax.plot([2,3,4], color="#d62728")
    line3, = ax.plot([3,2,9], color="#dbdb89")
    # The label_line() method will automatically place the labels
    ax.label_line((line1, line2, line3), ("labelA", "labelB", "labelC"))

@image_comparison(baseline_images=['label_auto3'])
def test_label_auto3():
    'Test automatic collision label placement'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot([1,2,3], color="#1f77b4")
    line2, = ax.plot([2,3,9], color="#d62728")
    line3, = ax.plot([3,2,9], color="#dbdb89")
    # The label_line() method will automatically place the labels
    ax.label_line(("labelA", "labelB", "labelC"))

class TestLegendFigureFunction(object):
    # Tests the label function for figure
    def test_label_three_args_pluskw(self):
        # test that third argument and loc=  called together give
        # Exception
        fig, ax = plt.subplots()
        lines = ax.plot(range(10))
        with pytest.raises(Exception):
            fig.label(lines, ['foobar'], 'right', loc='left')

    def test_iterable_handles_error(self):
        line1, = plt.plot([1,2,3], color="#1f77b4")
        line2, = plt.plot([2,3,4], color="#d62728")
        line3, = plt.plot([3,2,9], color="#dbdb8d")
        # The label_line() method place the labels in the order 
        # and will not be easily mismatch with lines.
        with pytest.raises(Exception):
            fig.label(line1, ("labelA", "labelB", "labelC"))

