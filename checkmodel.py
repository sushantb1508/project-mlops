#!/usr/bin/env python
# coding: utf-8

# In[ ]:


programfile = open('/home/jyotirmaya/ws/mlops1/program.py','r')	#connecting to the code file
code = programfile.read() #reading the code file

if 'keras' or 'tensorflow' in code: #CNN code should have keras and tensorflow
    if 'Conv2D' in code:#If the code is in CNN then conv2D should always be there 
        print('CNN')
    else:
        print('not CNN')
else:
    print('not deep learning')

