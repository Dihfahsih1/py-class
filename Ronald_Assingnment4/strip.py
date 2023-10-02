##creating a function to apply strip
def my_fun():
    url = '   hello world   '
    ban=url.bothstrip()
    print(ban)
my_fun()

"""But we can also use the left and right strips like below"""
url = '   hello world   '
ban=url.lstrip()#we use l for left strip
print(ban)
"""this therefore prints without the left whitespace"""

url = '   hello world   '
ban=url.rstrip()##we can also use r for right strip
print(ban)
"""this therefore prints without the right whitespace"""

