
# coding: utf-8

# In[111]:


import os
import numpy as np
import re
import matplotlib.pyplot as plt


# In[112]:


fil = open("nohup-copy.txt", 'r')


# In[113]:


content = fil.read()


# In[114]:


sep = [m.start() for m in re.finditer('#', content)]


# In[115]:


part1 = content[:sep[0]-1]
part2 = content[sep[0]+2:sep[1]-1]
part3 = content[sep[1]+2:]


# In[116]:


#print(part1)
#print(part2)
#print(part3)


# In[121]:


def plot(mat):
    test_auc = []
    test_loss = []
    train_auc = []
    train_loss = []
    x = []
    for i in range(250):
        test_auc.append(float(mat[iters_testauc[i] + 10 : iters_testloss[i] - 1]))
        test_loss.append(float(mat[iters_testloss[i] + 11: iters_traintime[i] - 1]))
        train_auc.append(float(mat[iters_trainauc[i] + 11: iters_trainloss[i] - 1]))
        train_loss.append(float(mat[iters_trainloss[i] + 12: iters_looptime[i] - 1]))
        x.append(i+1)
        
    plt.figure()
    plt.plot(x, test_auc)
    plt.title("Test AUC vs Epochs - Part 1")
    plt.xlabel("Epochs")
    plt.ylabel("AUC")

    plt.figure()
    plt.plot(x, test_loss)
    plt.title("Test loss vs Epochs - Part 1")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    plt.figure()
    plt.plot(x, train_auc)
    plt.title("Train AUC vs Epochs - Part 1")
    plt.xlabel("Epochs")
    plt.ylabel("AUC")

    plt.figure()
    plt.plot(x, train_loss)
    plt.title("Train Loss vs Epochs - Part 1")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")


# In[122]:


#Part 1 plot

iters_testauc = [m.start() for m in re.finditer("Test AUC", part1)]
iters_testloss = [m.start() for m in re.finditer("Test loss", part1)]
iters_traintime = [m.start() for m in re.finditer("Eval train time", part1)]
iters_trainauc = [m.start() for m in re.finditer("Train AUC", part1)]
iters_trainloss = [m.start() for m in re.finditer("Train loss", part1)]
iters_looptime = [m.start() for m in re.finditer("Loop time", part1)]

plot(part1)


# In[123]:


#Part 2 plot

iters_testauc = [m.start() for m in re.finditer("Test AUC", part2)]
print(part2[iters_testauc[22]])

iters_testloss = [m.start() for m in re.finditer("Test loss", part2)]
iters_traintime = [m.start() for m in re.finditer("Eval train time", part2)]
iters_trainauc = [m.start() for m in re.finditer("Train AUC", part2)]
iters_trainloss = [m.start() for m in re.finditer("Train loss", part2)]
iters_looptime = [m.start() for m in re.finditer("Loop time", part2)]

plot(part2)


# In[124]:


#Part 3 plot

iters_testauc = [m.start() for m in re.finditer("Test AUC", part3)]
iters_testloss = [m.start() for m in re.finditer("Test loss", part3)]
iters_traintime = [m.start() for m in re.finditer("Eval train time", part3)]
iters_trainauc = [m.start() for m in re.finditer("Train AUC", part3)]
iters_trainloss = [m.start() for m in re.finditer("Train loss", part3)]
iters_looptime = [m.start() for m in re.finditer("Loop time", part3)]

plot(part3)

