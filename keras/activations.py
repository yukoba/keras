from __future__ import absolute_import
from . import backend as K
from .utils.generic_utils import get_from_module


def softmax(x, axis=-1):
    return K.softmax(x, axis=axis)


def log_softmax(x, axis=-1):
    return K.log_softmax(x, axis=axis)


def elu(x, alpha=1.0):
    return K.elu(x, alpha)


def softplus(x):
    return K.softplus(x)


def softsign(x):
    return K.softsign(x)


def relu(x, alpha=0., max_value=None):
    return K.relu(x, alpha=alpha, max_value=max_value)


def tanh(x):
    return K.tanh(x)


def sigmoid(x):
    return K.sigmoid(x)


def hard_sigmoid(x):
    return K.hard_sigmoid(x)


def linear(x):
    return x


def get(identifier):
    if identifier is None:
        return linear
    return get_from_module(identifier, globals(), 'activation function')
