''''lines_read = set()
main=open('main.txt',"r")
stby=open('stby.txt',"w")
print('The main content with duiplicacy is')
for lines in main:
    print(lines)
    if lines not in lines_read:
        stby.write(lines)
        lines_read.add(lines)
stby.close()

print('The fresh content with duplicacy is')
for lines in open('stby.txt',"r"):
        print(lines)'''


x=set(open('main.txt').readlines())
y=open('new.txt',"w").writelines(x)
print('before------------------------------------')

for lines in open('main.txt','r'):
    print(lines)

print('after--------------------------------------')

for i in open('new.txt',"r"):
    print(i)