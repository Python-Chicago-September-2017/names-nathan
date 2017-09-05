students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_names(arr):
    for data in arr:
        name = ""
        for value in data:
            name += data[value] + " "
        print name

# print_names(students)

def students_and_instructors(arr):
    for i in arr:
        print i
        count = 1
        for data in arr[i]:
            name = ""
            for value in data:
                name += data[value] + " "
            print str(count) + " - " + name.upper() + "- " + str(len(name) - 2)
            count += 1
            name = ""
        count = 1

students_and_instructors(users)