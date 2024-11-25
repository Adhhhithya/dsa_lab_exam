import pandas as pd
from math import log2

def entropy(data):  # Calculate entropy
    probs = data.value_counts(normalize=True)
    return -sum(p * log2(p) for p in probs)

def info_gain(data, target, attr):  # Calculate information gain
    total_entropy = entropy(data[target])
    values = data[attr].unique()
    weighted_entropy = sum(
        (data[data[attr] == v].shape[0] / data.shape[0]) * entropy(data[data[attr] == v][target])
        for v in values
    )
    return total_entropy - weighted_entropy

def id3(data, target, attributes):  # Build tree
    if len(data[target].unique()) == 1: return data[target].iloc[0]
    if not attributes: return data[target].mode()[0]
    best_attr = max(attributes, key=lambda attr: info_gain(data, target, attr))
    return {best_attr: {v: id3(data[data[best_attr] == v], target, [a for a in attributes if a != best_attr]) for v in data[best_attr].unique()}}

data = pd.DataFrame({"Weather": ["Sunny", "Sunny", "Rainy", "Sunny", "Rainy"], "Play": ["No", "No", "Yes", "Yes", "Yes"]})
tree = id3(data, "Play", ["Weather"])
print(tree)
