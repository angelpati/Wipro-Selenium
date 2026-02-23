* Settings *
Library    Collections    # Collections library is required for dictionary and list operations

* Variables *
${NAME}        Angel          # Scalar variable
${NUM1}        100              # First number
${NUM2}        200              # Second number
${CITY}        Delhi           # City variable
@{FRUITS}      Apple    Banana    Mango    # List variable
&{USER}        name=Angel    age=22    role=Tester    # Dictionary variable

* Test Cases *

Scalar Variable Example
    # Print scalar variable
    Log    ${NAME}

Sum Of Two Numbers
    # Add two numbers using Evaluate keyword
    ${sum}=    Evaluate    ${NUM1} + ${NUM2}
    Log    ${sum}

Use Variable Inside Sentence
    # Using variable inside a sentence
    Log    My city name is ${CITY}

Reassign Variable Inside Testcase
    # Reassigning scalar variable inside test case
    ${NAME}=    Set Variable    Rahul
    Log    Updated name is ${NAME}

Print First Item Of List
    # Access first element of list (index starts from 0)
    Log    ${FRUITS}[0]

Loop Through List
    # Loop through each item in list
    FOR    ${item}    IN    @{FRUITS}
        Log    ${item}
    END

Find Length Of List
    # Get length of list using Get Length keyword
    ${length}=    Get Length    ${FRUITS}
    Log    ${length}

Dictionary Example
    # Access dictionary value using key
    Log    ${USER}[name]

Add New Key Value To Dictionary
    # Add new key-value pair to dictionary
    Set To Dictionary    ${USER}    city=Delhi
    Log    ${USER}[city]

Loop Dictionary And Print Key Value
    # Loop through dictionary and print key and value
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} = ${value}
    END