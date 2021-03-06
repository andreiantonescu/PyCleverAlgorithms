#!/usr/bin/env python

"""
Perceptron
"""


def iif(condition, true_part, false_part):
    return (condition and [true_part] or [false_part])[0]


def random_vector(minmax):
    import random

    return map(lambda x: x[0] + (x[1] - x[0]) * random.random(), minmax)


def initialize_weights(problem_size):
    minmax = [[-1.0, 1.0]] * (problem_size + 1)
    return random_vector(minmax)


def update_weights(num_inputs, weights, input, out_exp, out_act, l_rate):
    for i in range(0, num_inputs):
        weights[i] = weights[i] + l_rate * (out_exp - out_act) * input[i]
    weights[num_inputs] += l_rate * (out_exp - out_act) * 1.0


def activate(weights, vector):
    sum_wv = weights[- 1] * 1.0
    for i in range(0, len(vector)):
        sum_wv += weights[i] * vector[i]
    return sum_wv


def transfer(activation):
    return iif(activation >= 0, 1.0, 0.0)


def get_output(weights, vector):
    activation = activate(weights, vector)
    return transfer(activation)


def train_weights(weights, domain, num_inputs, iterations, lrate):
    for epoch in range(0, iterations):
        error = 0.0
        for pattern in domain:
            input = pattern[0:num_inputs]
            output = get_output(weights, input)
            expected = pattern[-1]
            error = error + abs(output - expected)
            update_weights(num_inputs, weights, input, expected, output, lrate)
        print("> epoch=%d, error=%f" % (epoch, error))


def do_test_weights(weights, domain, num_inputs):
    correct = 0
    for pattern in domain:
        input_vector = [float(pattern[k]) for k in range(0, num_inputs)]
        output = get_output(weights, input_vector)
        if round(output) == pattern[-1]:
            correct += 1
    print("Finished test with a score of %d/%d" % (correct, len(domain)))
    return correct


def execute(domain, num_inputs, iterations, learning_rate):
    weights = initialize_weights(num_inputs)
    train_weights(weights, domain, num_inputs, iterations, learning_rate)
    do_test_weights(weights, domain, num_inputs)
    return weights


def main():
    # problem configuration
    or_problem = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    inputs = 2
    # algorithm configuration
    iterations = 20
    learning_rate = 0.1
    # execute the algorithm
    w = execute(or_problem, inputs, iterations, learning_rate)
    #
    print("weights : %s" % str(w))
    #
    print("result : %s -> %s" % (str([0, 1, 0]), get_output(w, [0, 1, 0])))
    print("result : %s -> %s" % (str([1, 1, 1]), get_output(w, [1, 1, 1])))
    print("result : %s -> %s" % (str([1, 0, 0]), get_output(w, [1, 0, 0])))
    print("result : %s -> %s" % (str([0, 0, 0]), get_output(w, [0, 0, 0])))


if __name__ == "__main__":
    main()
