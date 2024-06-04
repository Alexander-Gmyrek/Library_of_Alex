import gc
import weakref
import inspect

def problem_1():
    print("Problem 1:")
    def testconection():
        connection = get_db_connection()
        if connection.is_connected():
            db_info = connection.get_server_info()
            return jsonify({"message": "Connected to MySQL Server version ", "version": db_info})
        else:
            return jsonify({"message": "Connection to MySQL Server failed"})
    testconection()

def problem_2():
    print("Problem 2: Reference Cycle")
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a 

def problem_3():
    print("Problem 3: Large Object in Global Scope")
    global large_list
    large_list = [i for i in range(1000000)]

def problem_4():
    print("Problem 4: Mutable Default Argument")
    def append_to_list(value, my_list=[]):
        my_list.append(value)
        return my_list

    list1 = append_to_list(1)
    list2 = append_to_list(2)
    print(list1, list2)  

def check_fixes():
    correct_fixes = {
        'problem_1': 'def testconection():\n    with get_db_connection() as connection:\n        if connection.is_connected():\n            db_info = connection.get_server_info()\n            return jsonify({"message": "Connected to MySQL Server version ", "version": db_info})\n        else:\n            return jsonify({"message": "Connection to MySQL Server failed"})\n',
        'problem_2': 'class Node:\n    def __init__(self, value):\n        self.value = value\n        self.next = None\n\na = Node(1)\nb = Node(2)\na.next = b\nb.next = weakref.ref(a)\n',
        'problem_3': 'global large_list\nlarge_list = [i for i in range(1000000)]\ndel large_list\n',
        'problem_4': 'def append_to_list(value, my_list=None):\n    if my_list is None:\n        my_list = []\n    my_list.append(value)\n    return my_list\nlist1 = append_to_list(1)\nlist2 = append_to_list(2)\nprint(list1, list2)\n'
    }
    problems = [problem_1, problem_2, problem_3, problem_4]
    not_fixed = []

    for problem in problems:
        source = inspect.getsource(problem)
        if correct_fixes[problem.__name__].strip() in source:
            print(f"{problem.__name__} is fixed.")
        else:
            print(f"{problem.__name__} is not fixed.")
            not_fixed.append(problem.__name__)
    
    if not not_fixed:
        print("Good job! All problems are fixed.")
    else:
        print(f"Problems not fixed: {', '.join(not_fixed)}")

if __name__ == "__main__":
    # Run the problems
    problem_1()
    problem_2()
    problem_3()
    problem_4()

    # Check the fixes
    check_fixes()

# Placeholder function for get_db_connection()
def get_db_connection():
    class MockConnection:
        def is_connected(self):
            return True
        
        def get_server_info(self):
            return "8.0.23"
        
        def close(self):
            pass
    
    return MockConnection()

# Placeholder function for jsonify()
def jsonify(data):
    return data