d="hello mummy"
g=d.replace('mummy','john')
print(g)

bag="i Love bags,i love hats"
bag1=bag.replace('love','hate',1)
print(bag1)


import re
man="replace digits like 1234 with x"
new_text=re.sub(r'\d+','X',man)
print(new_text)



