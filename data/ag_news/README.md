# AG-News

This directory includes **semantic** and **additive** consistency datasets of AG-News data

### Column information of train/validation/test sets
- index: index number of data instance.
- text: news article.
- label: class labels.

### Column information of **semantic** sets
- index: index number of data instance.
- text: news article.
- text_paraphrased: paraphrased version of *text*.
- label: class labels.

** inference should be done for *text* and *text_paraphrased*.

### Column information of **additive** sets
- index: index number of data instance.
- text_1: first news article.
- text_2: second news article.
- merged_text: merged version of *text_1* and *text_2*.
- label: class labels.

** inference should be done for *text_1*, *text_2* and *merged_text* to calculate the additive inconsistency.
