import math
import numpy as np

def rescale(a):
    r = a.shape[0]
    c = a.shape[1]

    mean_list = []
    std_list = []

    for i in range(c):
        mean_list.append(np.mean(a[:,i]))
        std_list.append(np.std(a[:,i]))

    a_s = a

    for col in range(c):
        for row in range(r):
            a_s[row,col] = (a[row,col]-mean_list[col])/std_list[col]
    
    return a_s

def similarity(u,v):
    d = dot(u,v)
    mag_u = mag(u)
    mag_v = mag(v)
    return d/(mag_u*mag_v)

def dot(u,v):
    d = 0
    for i in range(len(u)):
        d = d + u[i]*v[i]
    return d

def mag(x):
    m = 0
    for i in x:
        m = m + i**2
    return math.sqrt(m)

data = np.genfromtxt('state_facts-1.csv', delimiter = ',' ,  skip_header=1)

data = data[:,1:]

z_data = rescale(data)

#Virginia similarity

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

va = 46
m = -1
index = -1

for i in range(z_data.shape[0]):
    if i != 46:
        s = similarity(z_data[46,:], z_data[i,:])
        if s>m:
            m=s
            index = i

print('Similarity:',m)
print('Index:',index)
print('Virginia is most similar to',states[index])

#The state most similar to Virginia is Maryland