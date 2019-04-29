# machine_learning

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sklearn as sk
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, precision_recall_curve, log_loss
from sklearn.metrics import average_precision_score, mean_squared_error
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.pipeline import Pipeline
import xgboost as xgb
```
