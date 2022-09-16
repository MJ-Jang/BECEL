# SST2

This directory includes **semantic** and **additive** consistency datasets of SST2 data

### Column information of train/validation sets
- index: index number of data instance.
- sentence: input text.
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- sentence: input text.
- sentence_paraphrased: paraphrased version of *sentence*.
- label: class labels.

** inference should be done for *sentence_1* and *sentence_paraphrased*.

### Column information of **additive** sets
- index: index number of data instance.
- sentence_1: first input text.
- sentence_2: second input text.
- merged_sentence: merged version of *sentence_1* and *sentence_2*.
- label: class labels.

** inference should be done for *sentence_1*, *sentence_2* and *merged_sentence* to calculate the additive inconsistency.
