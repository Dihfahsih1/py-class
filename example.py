import matplotlib.pyplot as plt

x=["science","commerce","arts"]
y=[200,300,500]
plt.bar(x,y,color='blue')
plt.xlabel("subjects")
plt.ylabel("Students enrolled")
plt.title("Enrollments per year")

plt.show()