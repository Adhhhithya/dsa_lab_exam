import pandas as pd 
import math 
import numpy as np 

# Load dataset
data = pd.read_csv("C:\\Users\\Adhithya J\\OneDrive\\Documents\\Lab\\AI\\3-dataset.csv")
features = [feat for feat in data.columns if feat != "answer"] 

# Define a Node class to represent the nodes of the decision tree
class Node: 
    def __init__(self): 
        self.children = [] 
        self.value = "" 
        self.isLeaf = False 
        self.pred = "" 

# Function to calculate entropy
def entropy(examples): 
    pos = sum(examples["answer"] == "yes")
    neg = sum(examples["answer"] == "no")
    
    if pos == 0.0 or neg == 0.0: 
        return 0.0 

    total = pos + neg
    p = pos / total 
    n = neg / total 
    return -(p * math.log(p, 2) + n * math.log(n, 2)) 

# Function to calculate information gain
def info_gain(examples, attr): 
    uniq = np.unique(examples[attr]) 
    gain = entropy(examples) 

    for u in uniq: 
        subdata = examples[examples[attr] == u] 
        sub_e = entropy(subdata) 
        gain -= (float(len(subdata)) / float(len(examples))) * sub_e 

    return gain 

# Function to implement the ID3 algorithm
def ID3(examples, attrs): 
    root = Node() 
    max_gain = -1
    max_feat = None

    for feature in attrs: 
        gain = info_gain(examples, feature) 
        if gain > max_gain: 
            max_gain = gain 
            max_feat = feature 

    root.value = max_feat 
    uniq = np.unique(examples[max_feat]) 

    for u in uniq: 
        subdata = examples[examples[max_feat] == u] 
        
        if entropy(subdata) == 0.0: 
            newNode = Node() 
            newNode.isLeaf = True 
            newNode.value = u 
            newNode.pred = subdata["answer"].iloc[0]  # Get the first element
            root.children.append(newNode) 
        else: 
            dummyNode = Node() 
            dummyNode.value = u 
            new_attrs = [attr for attr in attrs if attr != max_feat]
            child = ID3(subdata, new_attrs) 
            dummyNode.children.append(child) 
            root.children.append(dummyNode) 

    return root 

# Function to print the decision tree
def printTree(root: Node, depth=0): 
    print("\t" * depth + root.value, end="") 
    if root.isLeaf: 
        print(" -> ", root.pred) 
    else:
        print()
    for child in root.children: 
        printTree(child, depth + 1) 

# Build and print the decision tree
root = ID3(data, features) 
printTree(root)
