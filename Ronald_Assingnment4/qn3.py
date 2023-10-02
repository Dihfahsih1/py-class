"""using a string function split"""
def my_str():
    greet="how are you doing man"
    great=greet.split()
    print(great)
my_str()

man="12345"
nam="67890"
for x in man:
    for y in nam:
        print(x.split(),y)