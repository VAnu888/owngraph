
import matplotlib.pyplot as plt #Import matplotlib to the code

title=input("Enter your graph title here: ")#Get input for title
xlabel=input("Enter label for X axes: ")#Get input for X axis label
ylabel=input("Enter label for Y axes: ")#Get input for Y axis label

#Get input for X axis
x1=input("Enter X axis: ")
x2=input("Enter X axis: ")
x3=input("Enter X axis: ")
x4=input("Enter X axis: ")
x5=input("Enter X axis: ")

#Get input for Y axis
y1=int(input("Enter Y axis: "))
y2=int(input("Enter Y axis: "))
y3=int(input("Enter Y axis: "))
y4=int(input("Enter Y axis: "))
y5=int(input("Enter Y axis: "))

#Build the graph
x = [x1, x2, x3, x4,  x5]
y = [y1,y2,y3,y4, y5]
plt.plot(x, y)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.title(title)
plt.show()
