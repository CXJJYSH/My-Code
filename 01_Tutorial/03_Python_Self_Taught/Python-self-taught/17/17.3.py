import re

a="The ghost that says boo huants the loo."

m=re.findall("[qwertyuiopasdfghjklzxcvbnm]oo",a,re.IGNORECASE)

print(m)

#下面是更取巧的方法

n=re.findall(".oo",a,re.IGNORECASE)

print(n)
