#Exercise Dictionary

#Dictionary 변수를 생성하는 방법
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#Retrieving itmes from dictionary
programming_dictionary["Bug"]


#Adding new item to dictionary
programming_dictionary["Feedback"] = "Thinking about the consequences together. "

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Feedback"] = "is nothing"


#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print (programming_dictionary[key])
