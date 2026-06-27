class Stack:
    def __init__(self, length):
        self.stack_list = []
        self.length = length
    def display(self):
        print(f"Stack of Length: {self.length}, and elements: {self.stack_list}.")
    def push(self, element):
        if len(self.stack_list) < self.length:
            self.stack_list.append(element)
        else:
            print("The element cannot be added in stack.")
    def pop(self):
        if len(self.stack_list) > 0:
            element = self.stack_list[-1]
            self.stack_list.pop()
            return element
        else:
            print("The element cannot be erased.")
    def peak(self):
        return self.stack_list[-1]
stack_object = Stack(10)        
stack_object.push(3)
stack_object.display()
stack_object.push(6)
stack_object.display()
stack_object.push(10)
stack_object.display()
print(stack_object.pop())
stack_object.display()
print(stack_object.peak())