inputfile=open("demo.txt",'r')
list=[]

a=inputfile.readline()
b=inputfile.readline()
c=inputfile.readline()
d=inputfile.readline()

print(a)
print(b)
print(c)
print(d)

a=a.split('_')
b=b.split('_')
c=c.split('_')
d=d.split('_')

print(a)
print(b)
print(c)
print(d)

dict={}
dict[0]=a
dict[1]=b
dict[2]=c
dict[3]=d
print("\n")
print(dict)

inputfile.close()

f= open("config.c","w+")
f.write("/*This is a port configuration file generated by python script*/")
f.write("\n/* To use this file, first update a PORT_CONFIG.txt and run the script*/")
f.write("\nPort_init()\n{")


f.write("\n\tPort_mode ({0},{1},{2});".format(dict[1][0],dict[1][1],dict[1][2]))
f.write("\n\tPort_mode ({0},{1},{2});".format(dict[2][0],dict[2][1],dict[2][2]))
f.write("\n\tPort_mode ({0},{1},{2});".format(dict[3][0],dict[3][1],dict[3][2]))
        
f.write("\n}")
f.close()

