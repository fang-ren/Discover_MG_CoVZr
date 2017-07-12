import pandas as pd
from sklearn import metrics
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

# Load in the CV data
data = pd.read_csv('cv_data.csv')

# Compute the ROC
fpr, tpr, thr = metrics.roc_curve(data['Measured'], data['P(AM)'], pos_label=0)

# Make a plot
fig, ax = plt.subplots()

ax.plot(fpr, tpr, 'r')
ax.plot([0,1],[0,1], 'k--')

ax.set_xlim([0,1])
ax.set_ylim([0,1])

ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')

fig.set_size_inches(4,4)
fig.tight_layout()
fig.savefig('cv_roc.png', dpi=320)

# Compute the FPR at 95%
f = interp1d(thr, fpr)
print('FPR at 95% liklihood:', f(0.95))
print('FPR at 50% liklihood:', f(0.50))

# Compute the log-loss, and other classification metrics
print('Accuracy:', metrics.accuracy_score(data['Measured'], data['Predicted']))
print('ROC AUC:', metrics.roc_auc_score(data['Measured'], data['P(CR)']))
print('Log-loss:', metrics.log_loss(data['Measured'], data[['P(AM)','P(CR)']].values))