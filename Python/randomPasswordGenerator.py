import random
'''
create class Generator
define array to hold all characters
define password
define helper function for generating password by using for loop to pick out random indices from the array and add the to the variable password

'''
class Generator:
        
    def __init__(self):
        self.charArray=['a', 'b','c','d', '1','2','3','4','5','6','7','8','9','0','e','f','g','h','i','j','A','B','C','D','E','F','G','H','I','J','_','-','#']
        self.passwordGenerator=self.GeneratePassword()
    def GeneratePassword(self):
        password=""
        for i in range(random.randrange(9,20)):
            rand=random.randrange(0,len(self.charArray))
            password+=self.charArray[rand]
        return password

def main():
    passwordGenerator1=Generator()
    return passwordGenerator1.GeneratePassword()

if __name__ == '__main__':
    print(main())