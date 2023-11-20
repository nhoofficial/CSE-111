#hard2
s=input("Enter Sring: ")
new=""
for i in range(len(s)):
    if s[i]!=s[len(s)-1]:
        new+=s[i]
    else:
        new+=s[i]
        break
if s.startswith(new)==s.endswith(new) and s.count(new)==3:
    print("Palindrome Substring")
else:
    print("Not palindrome Substring")