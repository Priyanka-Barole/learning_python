# write a python program script to convat user difine any given string to camel case.
# solution-

s=input("enter string:")
frist=s[0].lower()
mid=s[1:len(s)-1].upper()
end=s[-1].lower()
result=frist+mid+end
print(result)
