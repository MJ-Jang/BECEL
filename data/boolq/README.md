# BoolQ

This directory includes **semantic** and **negational** consistency datasets of BoolQ data

### Column information of train/validation sets
- index: index number of data instance.
- passage: given paragraph.
- question: questions regarding the passage. 
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- passage: given paragraph.
- question: questions regarding the passage. 
- question_paraphrased: paraphrased version of *text*.
- label: class labels.

** inference should be done for *question* and *question_paraphrased*.

### Column information of **negational** sets
- index: index number of data instance.
- passage: given paragraph.
- question: questions regarding the passage. 
- question_neg: negated version of *text*.
- label: class labels.
- neg_label: class labels of negated questions.

** inference should be done for *question* and *question_neg*.