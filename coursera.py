# import numpy as np
#
# X = np.array([[1, 0, 1], [2, 2, 2]])
# out = X[0, 1:3]
# print(out)

# X = np.array([[1, 0], [0,1]])
# y = np.array([[2,1],  [1,2]])
# z = np.dot(X,y)
# print(z)
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

import pandas as pd
import matplotlib.pyplot as plt
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))
print(df.head())
print(df.mean())
