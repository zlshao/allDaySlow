import  matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

sample_x=['1/256','1/512','1/1024','1/2048','1/4096','1/8192']
# pckrate_y=[2.7,4.8,7.2,10.0]
throughput_y=[66.24,
77.43 ,
82.72 ,
85.95 ,
87.82 ,
88.79 ,

]

plt.figure(figsize=(5,5))
# plt.subplot(1,1,1)
# plt.bar(sample_x,pckrate_y,width=0.4,color='#008B8B',edgecolor='black',hatch='x')
# plt.xlabel('Sampling Rate')
# plt.ylabel('Packet Rate(Mpps)')
# plt.ylim(0,12)
# for a, b in zip(sample_x, pckrate_y):
#  plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=10)

plt.subplot(1,1,1)
plt.bar(sample_x,throughput_y,width=0.4,color='#008B00',edgecolor='black')
plt.xlabel('Sampling rate')
plt.ylabel('Throughput of DCSS (Gbps)')
plt.ylim(0,130)
for a, b in zip(sample_x, throughput_y):
 plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=10)

# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2)

plt.show()
# plt.savefig('DCSS Perfor0319 2.pdf')
