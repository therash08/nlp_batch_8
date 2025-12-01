class User:  # 1. Renamed 'X' to 'User' to match the instantiation below
    # name = ''
    # email = ''
    # phone = ''

    def registration(self, x, y):
        self.name = x
        self.email = y
        self.age = 90
        print(self.name, self.email)


# Creating objects
rash_obj = User()
rash_obj.registration('rash', 'thersh@gmail.com')
print(rash_obj.__dict__)


# fahmid_obj = User()

# # 2. Fixed variable names to match what was defined above (rash_obj, not rash_object)
# print(rash_obj)
# rash_obj.name = 'rash'
# print(rash_obj.name)


# print(fahmid_obj)
# fahmid_obj.name = 'fahmid'
# print(fahmid_obj.name)
