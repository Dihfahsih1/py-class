import matplotlib.pyplot as plt

x=["comm","science","arts"]
y=[200,300,500]
plt.bar(x,y)
plt.xlabel("subjects")
plt.ylabel("Students enrolled")
plt.title("Enrollments per year")

plt.show()