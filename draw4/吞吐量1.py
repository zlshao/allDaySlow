import  matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# sample_x=['1/8','1/16','1/32','1/64']
# pckrate_y=[2.7,4.8,7.2,10.0]

sample_x=['1/256','1/512','1/1024','1/2048','1/4096','1/8192']
pckrate_y=[7.54 ,
8.82 ,
9.42 ,
9.79 ,
10.00 ,
10.11 ,

]
# throughput_y=[26.1,45.8,69.5,96.3]

plt.figure(figsize=(5,5))
plt.subplot(1,1,1)
plt.bar(sample_x,pckrate_y,width=0.4,edgecolor='black')
plt.xlabel('Sampling Rate')
plt.ylabel('Packet rate of DCSS (Mpps)')
plt.ylim(0,14)
for a, b in zip(sample_x, pckrate_y):
 plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=10)

# plt.subplot(1,2,2)
# plt.bar(sample_x,throughput_y,width=0.4,color='#6495ED',edgecolor='black',hatch='/')
# plt.xlabel('Sampling Rate')
# plt.ylabel('Throughput(Gbps)')
# plt.ylim(0,105)
# for a, b in zip(sample_x, throughput_y):
#  plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=10)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2)

plt.show()
# plt.savefig('DCSS Perfor0319 1.pdf')
