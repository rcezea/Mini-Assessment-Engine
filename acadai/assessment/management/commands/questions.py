PYTHON_TEXT_QUESTIONS = [
    (
        "Explain polymorphism in object-oriented programming using Python.",
        "Polymorphism allows objects of different classes to be treated through a common interface. "
        "In Python this is commonly achieved through method overriding, where multiple classes "
        "implement the same method name with different behavior."
    ),
    (
        "What is the difference between a list and a tuple in Python?",
        "Lists are mutable data structures whose contents can be modified after creation, while "
        "tuples are immutable. Tuples are generally faster and are often used for fixed collections "
        "of values."
    ),
    (
        "Explain how exception handling works in Python.",
        "Exception handling in Python uses try, except, else, and finally blocks to catch and handle "
        "runtime errors, preventing programs from crashing unexpectedly."
    ),
]

DS_TEXT_QUESTIONS = [
    (
        "Explain the difference between a stack and a queue.",
        "A stack follows the Last In First Out principle, while a queue follows the First In First "
        "Out principle. Stacks are used in recursion and function calls, while queues are used in "
        "scheduling and buffering."
    ),
    (
        "What is a binary tree and how is it used?",
        "A binary tree is a hierarchical data structure in which each node has at most two children. "
        "It is used in searching, sorting, and representing hierarchical relationships."
    ),
    (
        "Why do hash tables provide fast data access?",
        "Hash tables use hash functions to map keys directly to memory locations, allowing constant "
        "time average complexity for insertion, lookup, and deletion operations."
    ),
]

DB_TEXT_QUESTIONS = [
    (
        "Explain the purpose of database normalization.",
        "Database normalization organizes data to reduce redundancy and improve data integrity by "
        "dividing tables into related structures and enforcing relationships."
    ),
    (
        "What is a primary key and why is it important?",
        "A primary key uniquely identifies each record in a database table, ensuring data integrity "
        "and enabling efficient indexing and relationships."
    ),
    (
        "Explain the ACID properties in database systems.",
        "ACID stands for Atomicity, Consistency, Isolation, and Durability, which ensure reliable and "
        "safe database transactions even in the presence of failures."
    ),
]
