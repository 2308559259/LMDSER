from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import torch
import numpy as np

with open("./data/cluster.json",'r',encoding='utf-8')as fp:
    data = json.load(fp)

# for i in range(len(data)):




print(1)