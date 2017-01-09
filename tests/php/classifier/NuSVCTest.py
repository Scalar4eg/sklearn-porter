# -*- coding: utf-8 -*-

import unittest
import numpy as np
import random

from sklearn.svm.classes import NuSVC
from sklearn_porter import Porter

from ..PhpTest import PhpTest


class SVCTest(PhpTest, unittest.TestCase):

    def setUp(self):
        super(SVCTest, self).setUp()
        self.porter = Porter(language='php')
        clf = NuSVC(kernel='rbf', gamma=0.001, random_state=0)
        self._port_model(clf)

    def tearDown(self):
        super(SVCTest, self).tearDown()

    def test_kernel_linear(self):
        clf = NuSVC(kernel='linear', gamma=0.001, random_state=0)
        self._port_model(clf)
        php_preds, py_preds = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.n_random_tests):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            php_preds.append(self.make_pred_in_php(x))
            py_preds.append(self.make_pred_in_py(x))
        self.assertListEqual(py_preds, php_preds)

    def test_kernel_poly(self):
        clf = NuSVC(kernel='poly', gamma=0.001, random_state=0)
        self._port_model(clf)
        php_preds, py_preds = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.n_random_tests):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            php_preds.append(self.make_pred_in_php(x))
            py_preds.append(self.make_pred_in_py(x))
        self.assertListEqual(py_preds, php_preds)

    def test_kernel_sigmoid(self):
        clf = NuSVC(kernel='sigmoid', gamma=0.001, random_state=0)
        self._port_model(clf)
        php_preds, py_preds = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.n_random_tests):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            php_preds.append(self.make_pred_in_php(x))
            py_preds.append(self.make_pred_in_py(x))
        self.assertListEqual(py_preds, php_preds)
