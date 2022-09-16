# WiC

This directory includes **semantic**, **negational**, **symmetric**, and **transitive** consistency datasets of WiC data

### Column information of train/validation sets
- index: index number of data instance.
- word: target word.
- sentence1: input sentence 1 that includes the target word. 
- sentence2: input sentence 2 that includes the target word.
- start1: starting position of the target word in the sentence 1.
- start2: starting position of the target word in the sentence 2.
- end1: ending position of the target word in the sentence 1.
- end2: ending position of the target word in the sentence 2.
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- word: target word.
- sentence1: input sentence 1 that includes the target word. 
- sentence2: input sentence 2 that includes the target word.
- start1: starting position of the target word in the sentence 1.
- start2: starting position of the target word in the sentence 2.
- end1: ending position of the target word in the sentence 1.
- end2: ending position of the target word in the sentence 2.
- label: class labels.
- sentence2_paraphrase: paraphrased version of the *sentence2*.
- start_para: starting position of the target word in the *sentence2_paraphrase*.
- end_para: ending position of the target word in the *sentence2_paraphrase*.

** inference should be done for *sentence2* and *sentence2_paraphrase*.

### Column information of **negational** sets
- index: index number of data instance.
- sentence1: input sentence 1 that includes the target word. 
- sentence2: input sentence 2 that includes the target word.
- start1: starting position of the target word in the sentence 1.
- start2: starting position of the target word in the sentence 2.
- end1: ending position of the target word in the sentence 1.
- end2: ending position of the target word in the sentence 2.
- label: class labels.
- sentence2_neg: negated version of the *sentence2*.
- neg_label: class labels of negated *hypothesis*.
- start_neg: starting position of the target word in the *sentence2_neg*.
- end_neg: ending position of the target word in the *sentence2_neg*.

** inference should be done for *sentence2* and *sentence2_neg*.

### Column information of **symmetric** sets
- index: index number of data instance.
- word: target word.
- sentence1: input sentence 1 that includes the target word. 
- sentence2: input sentence 2 that includes the target word.
- start1: starting position of the target word in the sentence 1.
- start2: starting position of the target word in the sentence 2.
- end1: ending position of the target word in the sentence 1.
- end2: ending position of the target word in the sentence 2.
- label: class labels.

** inference should be done for the original and perturbed instances where the order of *premise* and *hypothesis* is switched.

### Column information of **transitive** sets
- index: index number of data instance.
- word: target word.
- sentence1: input sentence 1 that includes the target word. 
- sentence2: input sentence 2 that includes the target word.
- start1: starting position of the target word in the sentence 1.
- start2: starting position of the target word in the sentence 2.
- end1: ending position of the target word in the sentence 1.
- end2: ending position of the target word in the sentence 2.
- label: class labels.
- originated_idx: the index of two data points where the instance is originated from the *train* set.

** inference should be done for the *transitive* and *train* sets to calculate the transitive inconsistency.

