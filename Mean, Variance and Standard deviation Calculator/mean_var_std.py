import numpy as np

def calculate(list):
  array = np.array(list)
  try:
    array = array.reshape(3,3)
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  #Create the lists
  list_mean,  list_var, list_std, list_max, list_min, list_sum = ([] for i in range(6))
  #Put the values inside each list looking their axes
  for i in range(2):
    list_mean.append(array.mean(axis = i).tolist())
    list_var.append(array.var(axis = i).tolist())
    list_std.append(array.std(axis = i).tolist())
    list_min.append(array.min(axis = i).tolist())
    list_max.append(array.max(axis = i).tolist())
    list_sum.append(array.sum(axis = i).tolist())
  #Put the value inside each list looking the whole matrix 
  list_mean.append(array.mean())
  list_var.append(array.var())
  list_std.append(array.std())
  list_min.append(array.min())
  list_max.append(array.max())
  list_sum.append(array.sum())
  #Preparing the dictionary
  dic = {'mean':list_mean, 'variance': list_var, 'standard deviation': list_std, 'max':list_max, 'min':list_min, 'sum':list_sum}
  return(dic)