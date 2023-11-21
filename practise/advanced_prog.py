
import matplotlib.pyplot as plt

class Calculation1:
    def __init__(self, x, y):
        self.x1 = x
        self.x2 = y
        
    def sum(self):
        print(self.x1, self.x2) 
        return self.x1 + self.x2
    
class Calculation2:
    def __init__(self, x, y):
        self.x1 = x
        self.x2 = y
        
    def subtraction(self):
        return self.x1 - self.x2
    
    def multiplication(self):
        return self.x1 * self.x2
    
    def division(self):
        return self.x1 / self.x2
    
class Derived(Calculation1, Calculation2):
    def __init__(self, x, y):
        Calculation1.__init__(self, x, y)
        Calculation2.__init__(self, x, y)

def visualize_input_output(x, y, result):
    plt.figure(figsize=(8, 6))

    # Visualize input data
    plt.subplot(2, 1, 1)
    plt.bar(['x1', 'x2'], [x, y], color=['skyblue', 'salmon'])
    plt.title('Input Data')
    plt.xlabel('Variables')
    plt.ylabel('Values')

    # Visualize output result
    plt.subplot(2, 1, 2)
    plt.bar(['Sum'], [result], color='green')
    plt.title('Output Result')
    plt.xlabel('Operation')
    plt.ylabel('Result')

    plt.tight_layout()
    plt.show()

x = int(input('x1 = '))
y = int(input('x2 = '))

derived1 = Derived(x, y)
yy1 = derived1.sum()  # Calling the sum method on the Derived object

print("Sum:", yy1)

# Visualize input data and output result
visualize_input_output(x, y, yy1)
        