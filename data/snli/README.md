# SNLI

This directory includes **semantic**, **negational**, **symmetric**, and **transitive** consistency datasets of SNLI data

### Column information of train_1/train_2/validation/test sets
- index: index number of data instance.
- premise: input premise.
- hypothesis: input hypothesis. 
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- premise: input premise.
- hypothesis: input hypothesis. 
- hypothesis_paraphrased: paraphrased version of *hypothesis*.
- label: class labels.

** inference should be done for *hypothesis* and *hypothesis_paraphrased*.

### Column information of **negational** sets
- index: index number of data instance.
- premise: input premise.
- hypothesis: input hypothesis. 
- hypothesis_neg: negated version of *hypothesis*.
- label: class labels.
- neg_label: class labels of negated *hypothesis*.

** inference should be done for *hypothesis* and *hypothesis_neg*.

### Column information of **symmetric** sets
- index: index number of data instance.
- premise: input premise.
- hypothesis: input hypothesis. 
- label: class labels.

** inference should be done for the original and perturbed instances where the order of *premise* and *hypothesis* is switched.

### Column information of **transitive** sets
- index: index number of data instance.
- premise: input premise.
- hypothesis: input hypothesis. 
- label: class labels.
- originated_idx: the index of two data points where the instance is originated from the *test* set.

** inference should be done for the *transitive* and *test* sets to calculate the transitive inconsistency.

