from typing import Any, Callable
import pickle

import numpy as np


def test_function(function: Callable[..., Any], arg_keys: Any):
    """Execute functions and check results of local tests.

    - Assumes data has keys: "inputs", "outputs"
      - each is an array of 100 examples
      - inputs further are dicts with arg_keys as keys
      - check shape, within tolerance

    """
    with open("local_tests/local_tests.pickle", "rb") as f:
        try:
            test_data = pickle.load(f, encoding="latin1")
        except TypeError:
            test_data = pickle.load(f)

    data = test_data[function.__name__]
    inputs = data["inputs"]
    outputs = data["outputs"]

    for input, expected in zip(inputs, outputs):
        args_ = {k: input[k] for k in arg_keys}
        answer = function(**args_)
        if answer.shape != expected.shape or not np.allclose(answer, expected, rtol=1e-5, atol=1e-5):
            print(f"{function.__name__} failed some local tests")
            print(f"\ninput: \n{input}")
            print(f"\nanswer: \n{answer}")
            print(f"\nexpected: \n{expected}")
            return
    print(f"{function.__name__} successfully passed local tests")
    return


def debug_function(function: Callable[..., Any], arg_keys: Any) -> tuple[Any, Any, Any]:
    """Execute functions and check results of local tests, and returns failed test.

    - Assumes data has keys: "inputs", "outputs"
      - each is an array of 100 examples
      - inputs further are dicts with arg_keys as keys
      - check shape, within tolerance

    Return:
        input: Input to the function
        answer: Answer using student's implementation
        expected: Expected correct answer
    """
    with open("local_tests/local_tests.pickle", "rb") as f:
        try:
            test_data = pickle.load(f, encoding="latin1")
        except TypeError:
            test_data = pickle.load(f)

    data = test_data[function.__name__]
    inputs = data["inputs"]
    outputs = data["outputs"]

    answers = []
    for input, expected in zip(inputs, outputs):
        args_ = {k: input[k] for k in arg_keys}
        answer = function(**args_)
        answers.append(answer)
        if answer.shape != expected.shape or not np.allclose(answer, expected, rtol=1e-5, atol=1e-5):
            return input, answer, expected
    return inputs, answers, outputs
