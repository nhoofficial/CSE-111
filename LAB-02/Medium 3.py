s=input('Enter word: ')
def vowelcount(s):
    vowel=['a','e','i','o','u']
    new=""
    s=s.lower()
    c=0
    new1=""
    for i in s:
        if i in vowel:
           c+=1
           new+=i
    for i in range(len(new)):
        if i==len(new)-1:
            new1+=new[i]+"."
        else:
            new1+=new[i]+","
    if c==0:
        print('No vowels in the name')
    else:
        print("Vowels:",new1,"Total number of vowels:",c)
vowelcount(s)               
    



