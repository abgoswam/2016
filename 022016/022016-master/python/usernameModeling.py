# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:37:52 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'E:\hackerreborn\022016\csharp\ConsoleAppsFeb\okcFeaturizerFull\bin\Debug\data\Results2.csv')

df['TrainingError'] = 1.0 - df['TrainingAccuracy']
df['CrossValidationError'] = 1.0 - df['CrossValidationAccuracy']

plt.plot(df['TrainingSampleSize'], df['TrainingError'], 'bo-', label='training error')
plt.plot(df['TrainingSampleSize'], df['CrossValidationError'], 'ro-', label='cross-validation error (10 fold)')

plt.title("Learning Curve for Username, Gender Prediction API.")
plt.ylabel('Error' )
plt.xlabel('Training Size' )
plt.grid(True)
plt.axis([0, 80000, 0, .4])
plt.legend(loc=0)
plt.show()

samplesplot = df[df['TrainingSampleSize'] < 40000]
plt.plot(samplesplot['TrainingSampleSize'], samplesplot['CrossValidationAccuracy'], 'bo-', label='Cross Validation accuracy (10-fold)')
plt.plot(samplesplot['TrainingSampleSize'], samplesplot['TestAccuracy'], 'ro-', label='Test set accuracy (35K samples)')
plt.title("Linear Plot.")
plt.ylabel('Accuracy' )
plt.xlabel('Training Set Size.' )
plt.grid(True)
plt.axis([5000, 40000, 0.6, 0.8])
plt.legend(loc=0)
plt.show()

samplesplot = df[df['TrainingSampleSize'] < 40000]
plt.plot(np.log2(samplesplot['TrainingSampleSize']), samplesplot['CrossValidationAccuracy'], 'bo-', label='Cross Validation accuracy (10-fold)')
plt.plot(np.log2(samplesplot['TrainingSampleSize']), samplesplot['TestAccuracy'], 'ro-', label='Test set accuracy (35K samples)')
plt.title("Log Plot.")
plt.ylabel('Accuracy' )
plt.xlabel('Log2 of Training Set Size' )
plt.grid(True)
plt.axis([12.5, 15.5, 0.6, 0.8])
plt.legend(loc=0)
plt.show()

df = pd.read_csv(r'E:\hackerreborn\022016\csharp\ConsoleAppsFeb\okcFeaturizerFull\bin\Debug\data\Results3.csv')

plt.plot(np.log2(df['TrainingSampleSize']), df['CrossValidationAccuracy'], 'bo-', label='Cross Validation accuracy (10-fold)')
plt.plot(np.log2(df['TrainingSampleSize']), df['TestAccuracy'], 'ro-', label='Test set accuracy (35K samples)')
plt.title("Log Plot.")
plt.ylabel('Accuracy' )
plt.xlabel('Log2 of Training Set Size' )
plt.grid(True)
plt.axis([12, 15.5, 0.6, 0.8])
plt.legend(loc=0)
plt.show()