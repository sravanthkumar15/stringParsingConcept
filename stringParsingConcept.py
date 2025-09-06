inputString = """{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}"""

print("\n String Parsing \n")

print("Requirement: Convert String -> Dictionary -> JSON")
print("After the above step, convert the JSON -> Dictionary -> String \n")

first_list = inputString.split(',')
print(first_list)

second_list = []
for i in first_list:
     second_list.extend(i.split(':'))

print(second_list)

my_dictionary = {}

for i in range(0,len(second_list),2):
     my_dictionary[second_list[i]] = second_list[i+1]

print()
print(my_dictionary)

print("\n Dictionary can contain wide varities of data types including functions...object based, where as JSON is string based\n")
print("\n Iterate over the dictionary and check for the type of both key and value and if they aren't equal to string, ignore them\n")

final_dictionary_for_json= {}

for i in my_dictionary:
    if type(i)==str and type(my_dictionary[i])==str:
         final_dictionary_for_json[i] = my_dictionary[i]

print()
print(final_dictionary_for_json)


for key in final_dictionary_for_json:
    final_dictionary_for_json[key] = final_dictionary_for_json[key].replace('\n', '')

print(final_dictionary_for_json)

