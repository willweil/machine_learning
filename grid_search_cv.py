# your turn
from sklearn.model_selection import GridSearchCV
log = LogisticRegression()
parameter = {'C': [0.001, 0.1, 1, 10, 100]}
grid = GridSearchCV(log, parameter, cv=5, scoring="accuracy")
grid.fit(Xlr, ylr)
grid.best_estimator_, grid.best_params_, grid.best_score_

log = LogisticRegression(C=grid.best_params_['C'])
log.fit(Xlr, ylr)
ypred = log.predict(Xtestlr)
accuracy_score(ypred, ytestlr)
