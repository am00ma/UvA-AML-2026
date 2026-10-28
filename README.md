![uva-logo](src/uva-logo.jpg)

# Applied Machine Learning 2026

Lab assignments for the course Applied Machine Learning at the University of Amsterdam.

## Installation

```bash
# If you haven't already
git clone https://github.com/am00ma/UvA-AML-2026.git

# Update to latest version
cd UvA-AML-2026
git pull
```

## Usage

1. Open the folder `week_[x]` from your IDE.
   ( If your working dir is PWD, the notebook should find
   `local_tests/local_tests.pickle` and `automark.py` in the path )

2. Define your functions in the code where indicated:

   ```python
   def w1_linear_forward(x_input, P):
       """Perform the Linear mapping of the input
       # Arguments
           x_input: input of the linear function - np.array of size `(n_objects, n_in)`
           P: np.array of size `(n_in, n_out)`
       # Output
           the output of the linear function
           np.array of size `(n_objects, n_out)`
       """
       #################
       ### YOUR CODE ###
       #################
       return output
   ```

3. Test your answer (tests locally from `local_tests/local_tests.pickle`)

   ```python
   am.test_student_function(w1_linear_forward, ["x_input", "P"])
   ```

4. Check progress as shown above in step 2.

## Index

### week 1

week_1/Intro.ipynb

| function             | args                   |
| -------------------- | ---------------------- |
| w1_linear_forward    | ['x_input', 'P']       |
| w1_cal_pseudoinverse | ['x_input', 'y_input'] |
| w1_L2_regression     | ['x_input', 'y_input'] |

### week 2

week_2/ML.ipynb

| function                    | args                                       |
| --------------------------- | ------------------------------------------ |
| w2_linear_forward           | ['x_input', 'W', 'b']                      |
| w2_linear_grad_W            | ['x_input', 'grad_output', 'W', 'b']       |
| w2_linear_grad_b            | ['x_input', 'grad_output', 'W', 'b']       |
| w2_sigmoid_forward          | ['x_input']                                |
| w2_sigmoid_grad_input       | ['x_input', 'grad_output']                 |
| w2_nll_forward              | ['target_pred', 'target_true']             |
| w2_nll_grad_input           | ['target_pred', 'target_true']             |
| w2_dist_to_training_samples | ['x_input', 'training_set']                |
| w2_nearest_neighbors        | ['distances', 'training_labels']           |
| w2_tree_weighted_entropy    | ['Y_left', 'Y_right', 'classes']           |
| w2_tree_split_data_left     | ['X', 'Y', 'feature_index', 'split_value'] |
| w2_tree_split_data_right    | ['X', 'Y', 'feature_index', 'split_value'] |
| w2_tree_to_terminal         | ['Y']                                      |

### week 3

week_3/Neural_Nets.ipynb

| function           | args                        |
| ------------------ | --------------------------- |
| w3_dense_forward   | ['x_input', 'W', 'b']       |
| w3_relu_forward    | ['x_input']                 |
| w3_l2_regularizer  | ['weight_decay', 'weights'] |
| w3_conv_matrix     | ['matrix', 'kernel']        |
| w3_box_blur        | ['image', 'box_size']       |
| w3_maxpool_forward | ['x_input']                 |
| w3_flatten_forward | ['x_input']                 |
