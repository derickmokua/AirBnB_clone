AirBnB Clone Project
Welcome to the AirBnB clone project! This project is designed to help you build your first full web application, starting with a command interpreter to manage your AirBnB objects.

Description of the Project
This project involves creating a command interpreter that can manage various objects related to an AirBnB-like application. The interpreter will be able to create new objects, retrieve objects from a file or database, perform operations on objects, update attributes of an object, and destroy an object.

The project also involves creating a parent class (BaseModel) to handle the initialization, serialization, and deserialization of future instances. Furthermore, you will create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.

Additionally, you will create classes for User, State, City, Place, and more that inherit from BaseModel. You will also create the first abstracted storage engine of the project: File storage. Lastly, you will create all unittests to validate all your classes and storage engine.

Description of the Command Interpreter
A command interpreter, in this context, is a custom shell that allows you to interact with the program and manage its objects. It's similar to a shell in a Unix-like operating system, but it's limited to a specific use-case: managing the objects of this project.

The command interpreter will be able to:

Create a new object (e.g., a new User or a new Place)
Retrieve an object from a file, a database, etc.
Perform operations on objects (count, compute stats, etc.)
Update attributes of an object
Destroy an object
How to Start It
To start the command interpreter, you would typically run a Python script that initializes the interpreter. This could be done by running a command like python3 interpreter.py in your terminal, assuming that interpreter.py is the script that initializes the interpreter.

How to Use It
Once the command interpreter is running, you can interact with it by typing commands into the terminal. The exact commands you can use will depend on how the interpreter is implemented, but you can generally expect to be able to create, retrieve, update, and destroy objects, as well as perform operations on objects.

Examples
Here's an example of how you might use the command interpreter to create a new User object:
> create_user Derick Mokua derickmokua@outlook.com
> get_user derickmokua@outlook.com
