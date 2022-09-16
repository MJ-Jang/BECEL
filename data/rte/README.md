# RTE

This directory includes **semantic** and **negational** consistency datasets of RTE data

### Column information of train/validation sets
- index: index number of data instance.
- sentence1: sentence input 1.
- sentence2: sentence input 2. 
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- sentence1: sentence input 1.
- sentence2: sentence input 2. 
- sentence2_paraphrased: paraphrased version of *sentence2*.
- label: class labels.

** inference should be done for *sentence2* and *sentence2_paraphrased*.

### Column information of **negational** sets
- index: index number of data instance.
- sentence1: sentence input 1.
- sentence2: sentence input 2. 
- sentence2_neg: negated version of *sentence2*.
- label: class labels.
- neg_label: class labels of negated sentence2.

** inference should be done for *sentence2* and *sentence2_neg*.

### Column information of **symmetric** sets
- index: index number of data instance.
- sentence1: sentence input 1.
- sentence2: sentence input 2. 
- label: class labels.

** inference should be done for the original and perturbed instances where the order of *sentence1* and *sentence2* is switched.