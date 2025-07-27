class School:
    def __init__(self,email):
        self._email='vse@gmail.com'

    def email(self):
        return self._email


s1=School('tk@gmail.com')
print(s1.email())

s1._email='xyz@gmail.com'
print(s1.email())