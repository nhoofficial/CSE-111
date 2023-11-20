#2
a=list(input().split(','))
my_dict={}
maximum=''
minimum=''
first=True
for i in a:
    x=i.split(':')
    if first:
        maximum=x[0]
        minimum=x[0]
        first=False
    my_dict[x[0]] = int(x[1])
    if my_dict[x[0]]>my_dict[maximum]:
        maximum=x[0]
    if my_dict[x[0]]<my_dict[minimum]:
        minimum=x[0]
print('Minimum:',minimum,'Maximum:',maximum)    
    
     
             
        

