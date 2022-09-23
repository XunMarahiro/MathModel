from Solover import angel
import matplotlib.pyplot as plt



plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

a=[4,4]

b=[5,10]
c=[0,10]

b1=[4,7]
c1=[5,5]

plt.figure()
g=angel(a,c1,b1)

m=0.1
for q in range(0,100):
    n=0.1
    print(q)
    for w in range(0,100):
        if abs(g=angel(a,c1,[m,n])):

            plt.scatter(m,n,s=1)
        n=n+0.1

    m=m+0.1
plt.show()