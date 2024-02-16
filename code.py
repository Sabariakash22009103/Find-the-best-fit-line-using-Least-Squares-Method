import numpy as np
import matplotlib.pyplot as plt

# Preprocesseing Input data

X=np.array(eval(input('Enter X values:')))
Y=np.array(eval(input('Enter Y values:')))

# MEAN
X_mean=np.mean(X)
Y_mean=np.mean(Y)
num=0
denom=0

# to find sum of (xi-x')&(yi-y')&(xi-x')^2
for i in range(len(X)):
    num+=(X[i]-X_mean)*(Y[i]-Y_mean)
    denom+=(X[i]-X_mean)**2

# calculate slope
m=num/denom

# calculate intercept
b=Y_mean-m*X_mean
print(m,b)

# line equation
Y_pred=m*X+b
print(Y_pred)

# to plot graph
plt.scatter(X,Y)
plt.plot(X,Y_pred,color='green')
plt.show()
