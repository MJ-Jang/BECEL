# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from typing import Text, List, Union, Dict
from datasets import load_dataset


def semantic_inconsistency(
        prediction_original: List,
        prediction_paraphrase: List,
) -> Dict:
    """A function that calculates semantic inconsistency

    Args:
        prediction_original: the list of predictions on the original data instances
        prediction_paraphrase: the list of predictions on the paraphrased data instances

    Returns:
        A dictionary containing inconsistency
    """
    assert len(prediction_original) == len(prediction_paraphrase)

    inconsistency = 1 - accuracy_score(prediction_original, prediction_paraphrase)

    outp = {
        "inconsistency": inconsistency,
    }
    return outp


def negational_inconsistency(
        prediction_original: List,
        prediction_negated: List,
        condition_correct_prediction: Union[int, Text] = None
) -> Dict:
    """A function that calculates negational inconsistency

    Args:
        prediction_original: the list of predictions on the original data instances
        prediction_negated: the list of predictions on the negated data instances
        condition_correct_prediction: correct answer when applying the conditioned inconsistency (e.g., 0 (entailment) for SNLI)

    Returns:
        A dictionary containing inconsistency and conditioned inconsistency
    """
    assert len(prediction_original) == len(prediction_negated)

    inconsistency = accuracy_score(prediction_original, prediction_negated)

    if condition_correct_prediction:
        index_ = [i for i, p in enumerate(prediction_original) if p == condition_correct_prediction]

        condition_pred_original_ = [prediction_original[i] for i in index_]
        condition_pred_neg_ = [prediction_negated[i] for i in index_]

        conditioned_inconsistency = accuracy_score(condition_pred_original_, condition_pred_neg_)
    else:
        conditioned_inconsistency = inconsistency

    outp = {
        "inconsistency": inconsistency,
        "conditioned_inconsistency": conditioned_inconsistency,
    }
    return outp


def symmetric_inconsistency(
        prediction_original: List,
        prediction_symmetric: List,
        condition_correct_prediction: Union[int, Text] = None
) -> Dict:
    """A function that calculates symmetric inconsistency

    Args:
        prediction_original: the list of predictions on the original data instances
        prediction_symmetric: the list of predictions on the negated data instances
        condition_correct_prediction: correct answer when applying the conditioned inconsistency (e.g., 0 (entailment) for SNLI)

    Returns:
        A dictionary containing inconsistency and conditioned inconsistency
    """

    assert len(prediction_original) == len(prediction_symmetric)
    inconsistency = 1 - accuracy_score(prediction_original, prediction_symmetric)

    if condition_correct_prediction:
        index_ = [i for i, p in enumerate(prediction_original) if p == condition_correct_prediction]

        condition_pred_original_ = [prediction_original[i] for i in index_]
        condition_pred_sym_ = [prediction_symmetric[i] for i in index_]

        conditioned_inconsistency = 1 - accuracy_score(condition_pred_original_, condition_pred_sym_)
    else:
        conditioned_inconsistency = inconsistency

    outp = {
        "inconsistency": inconsistency,
        "conditioned_inconsistency": conditioned_inconsistency,
    }
    return outp


def transitive_inconsistency(
        transitive_predictions: List,
        originated_predictions: List,
        data_path: Text,
        task_name: Text,
):
    if task_name == 'wic':
        # consistency: model generate correct answer for the originated data points -> correct on transitive data point
        # inconsistency: 1 - consistency
        train_df = load_dataset('super_glue', 'wic', split='train').to_pandas()
        assert len(train_df) == len(originated_predictions)

        transitive_df = pd.read_csv(os.path.join(data_path, 'transitive.tsv'), sep='\t')

        originated_idx = transitive_df['originated_idx'].tolist()
        originated_idx = [[int(i) for i in s.split('|')] for s in originated_idx]

        hits_ = [1 if p == l else 0 for p, l in zip(transitive_predictions, transitive_df['label'])]
        consistency = []
        for idx_, (o_idx_, h_) in enumerate(zip(originated_idx, hits_)):
            pred1_ = originated_predictions[o_idx_[0]]
            pred2_ = originated_predictions[o_idx_[1]]

            gs1_ = train_df['label'][o_idx_[0]]
            gs2_ = train_df['label'][o_idx_[1]]

            if pred1_ == gs1_ and pred2_ == gs2_:
                if h_ == 0:
                    consistency.append(0)
                else:
                    consistency.append(1)

        consistency = np.sum(consistency) / len(consistency)
        inconsistency = 1 - consistency

    elif task_name == 'snli':
        test_df = load_dataset('snli', split='test').to_pandas()
        test_df = test_df[test_df['label'] != -1].dropna()
        test_df = test_df.reset_index()

        assert len(test_df) == len(originated_predictions)

        transitive_df = pd.read_csv(os.path.join(data_path, 'transitive.tsv'), sep='\t').dropna()
        transitive_label = transitive_df['label'].tolist()

        hits_ = []
        for l, p in zip(transitive_label, transitive_predictions):
            if l == 2:
                if p == 2:
                    hits_.append(1)
                else:
                    hits_.append(0)
            if l == 3:
                if p in [1, 2]:
                    hits_.append(1)
                else:
                    hits_.append(0)
            if l == 4:
                if p in [0, 1]:
                    hits_.append(1)
                else:
                    hits_.append(0)

        # inconsistency
        originated_idx = transitive_df['originated_idx'].tolist()
        originated_idx = [[int(i) for i in s.split('|')] for s in originated_idx]

        consistency = []
        for idx_, (o_idx_, h_) in enumerate(zip(originated_idx, hits_)):
            pred1_ = originated_predictions[o_idx_[0]]
            pred2_ = originated_predictions[o_idx_[1]]

            gs1_ = test_df['label'][o_idx_[0]]
            gs2_ = test_df['label'][o_idx_[1]]

            if pred1_ == gs1_ and pred2_ == gs2_:
                if h_ == 0:
                    consistency.append(0)
                else:
                    consistency.append(1)

        consistency = np.sum(consistency) / len(consistency)
        inconsistency = 1 - consistency
    else:
        raise NotImplementedError

    outp = {
        "inconsistency": inconsistency,
    }
    return outp


def additive_inconsistency(
        first_prediction: List,
        second_prediction: List,
        merged_prediction: List,
        labels: List
):
    """A function that calculates additive inconsistency

    Args:
        first_prediction: the list of predictions on the first data instances
        second_prediction: the list of predictions on the second data instances
        merged_prediction: xhe list of predictions on the merged data instances
        labels: the list of labels of the first and second (and merged) sentences
    Returns:
        A dictionary containing inconsistency
    """
    # consistency: model generate correct answer on both the first and second sentence -> correct on additive data point
    # inconsistency: 1 - consistency

    assert len(first_prediction) == len(second_prediction)
    assert len(second_prediction) == len(merged_prediction)
    assert len(merged_prediction) == len(labels)

    consistency = []
    for idx_, (merged_pred_, label_) in enumerate(zip(merged_prediction, labels)):
        first_pred_ = first_prediction[idx_]
        second_pred_ = second_prediction[idx_]

        if first_pred_ == label_ and second_pred_ == label_:
            if merged_pred_ == label_:
                consistency.append(1)
            else:
                consistency.append(0)

    consistency = np.sum(consistency) / len(consistency)
    inconsistency = 1 - consistency

    outp = {
        "inconsistency": inconsistency,
    }
    return outp


if __name__ == '__main__':
    import os
    import json

    example_data_path = os.path.join(os.path.abspath(os.path.dirname(__name__)), "../data", "examples")
    # 1. Semantic example
    with open(os.path.join(example_data_path, "mrpc-semantic.json"), "r") as readFile:
        semantic_ = json.load(readFile)
    semantic_inconsistency_ = semantic_inconsistency(
        semantic_["original_preds"],
        semantic_["paraphrase_preds"]
    )["inconsistency"]

    print(f"MRPC Semantic inconsistency: {semantic_inconsistency_}")

    # 2. Negation example
    with open(os.path.join(example_data_path, "mrpc-negational.json"), "r") as readFile:
        negational_ = json.load(readFile)

    negational_inconsistency_ = negational_inconsistency(
        negational_["original_preds"],
        negational_["negation_preds"]
    )["inconsistency"]

    print(f"MRPC Negation inconsistency: {negational_inconsistency_}")

    # 3. Symmetric example
    with open(os.path.join(example_data_path, "snli-symmetric.json"), "r") as readFile:
        symmetric_ = json.load(readFile)

    symmetric_inconsistency_ = symmetric_inconsistency(
        symmetric_["original_preds"],
        symmetric_["symmetric_preds"]
    )["inconsistency"]

    conditional_symmetric_inconsistency_ = symmetric_inconsistency(
        symmetric_["original_preds"],
        symmetric_["symmetric_preds"],
        condition_correct_prediction=2
    )["inconsistency"]

    print(f"SNLI Symmetric inconsistency: {semantic_inconsistency_} | "
          f"SNLI Conditional Symmetric inconsistency: {conditional_symmetric_inconsistency_}")

    # 4. Additive example
    with open(os.path.join(example_data_path, "ag_news-additive.json"), "r") as readFile:
        additive_ = json.load(readFile)

    additive_inconsistency_ = additive_inconsistency(
        first_prediction=additive_["first_preds"],
        second_prediction=additive_["second_preds"],
        merged_prediction=additive_["merged_preds"],
        labels=additive_["labels"],
    )["inconsistency"]
    print(f"AG-News Additive inconsistency: {additive_inconsistency_}")

    # 5. SNLI Transitive example
    with open(os.path.join(example_data_path, "snli-transitive.json"), "r") as readFile:
        snli_transitive = json.load(readFile)

    transitive_snli_inconsistency_ = transitive_inconsistency(
        transitive_predictions=snli_transitive["transitive_preds"],
        originated_predictions=snli_transitive["originated_preds"],
        data_path="../data/snli",
        task_name="snli"
    )["inconsistency"]
    print(f"SNLI Transitive inconsistency: {transitive_snli_inconsistency_}")

    # 6. WiC Transitive example
    with open(os.path.join(example_data_path, "wic-transitive.json"), "r") as readFile:
        wic_transitive = json.load(readFile)

    transitive_wic_inconsistency_ = transitive_inconsistency(
        transitive_predictions=wic_transitive["transitive_preds"],
        originated_predictions=wic_transitive["originated_preds"],
        data_path="../data/wic",
        task_name="wic"
    )["inconsistency"]
    print(f"WiC Transitive inconsistency: {transitive_wic_inconsistency_}")
