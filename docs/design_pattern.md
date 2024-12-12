Sure! Design patterns provide solutions to common problems in software design. Below are a few Python implementations of popular design patterns, categorized as  **Creational** ,  **Structural** , and  **Behavioral** .

---

### **1. Singleton Pattern (Creational)**

Ensures a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example usage
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
```

---

### **2. Factory Pattern (Creational)**

Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Example usage
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Woof!
```

---

### **3. Observer Pattern (Behavioral)**

Defines a dependency between objects so that when one object changes state, all its dependents are notified.

```python
class Observer:
    def update(self, message):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Example usage
subject = Subject()
observer1 = ConcreteObserver("Observer1")
observer2 = ConcreteObserver("Observer2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Hello Observers!")
```

---

### **4. Decorator Pattern (Structural)**

Adds behavior to an object dynamically.

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

# Example usage
print(greet("Alice"))  # <b><i>Hello, Alice</i></b>
```

---

### **5. Strategy Pattern (Behavioral)**

Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

```python
class Strategy:
    def execute(self, data):
        raise NotImplementedError

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy.execute(data)

# Example usage
data = [5, 3, 2, 8]
context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # [2, 3, 5, 8]

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # [8, 5, 3, 2]
```

---

### **6. Command Pattern (Behavioral)**

Encapsulates a request as an object, allowing you to parameterize clients with different requests.

```python
class Command:
    def execute(self):
        raise NotImplementedError

class LightOnCommand(Command):
    def execute(self):
        print("The light is ON")

class LightOffCommand(Command):
    def execute(self):
        print("The light is OFF")

class RemoteControl:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

# Example usage
remote = RemoteControl()
remote.add_command(LightOnCommand())
remote.add_command(LightOffCommand())
remote.execute_commands()
```

---

### **7. Adapter Pattern (Structural)**

Allows incompatible interfaces to work together.

```python
class EuropeanSocket:
    def plug_in(self):
        return "220V power"

class USASocketAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def plug_in(self):
        return f"Converting {self.european_socket.plug_in()} to 110V"

# Example usage
euro_socket = EuropeanSocket()
adapter = USASocketAdapter(euro_socket)
print(adapter.plug_in())  # Converting 220V power to 110V
```

---

These examples show how Python can implement commonly used design patterns in a clean and efficient way. Would you like to dive deeper into any of these patterns?
