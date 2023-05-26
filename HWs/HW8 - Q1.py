#
# Do a search online and find an example of JSON data.
# Cut and paste the example into your program (assign it to a variable, call it data),
# and demonstrate how you can access at least two items inside the data structure.
# In your comments, add a link/reference to where you found the JSON example.
#

# Example of JSON data is from https://www.javatpoint.com/json-object
data = {
     "firstName": "Sonoo",
     "lastName": "Jaiswal",
     "age": 27,
     "address" :
         {
            "streetAddress": "Plot-6, Mohan Nagar",
             "city": "Ghaziabad",
             "state": "UP",
             "postalCode": "201007"
         }
}

print(data['firstName'], data['address']['city'])
