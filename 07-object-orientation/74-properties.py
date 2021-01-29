class A():
    __private = 'private'

    def __setprivate(self, private):
        self.__private = private

    def __getprivate(self):
        return self.__private

    public = property(__getprivate, __setprivate)


a = A()
print(a.public)
a.public = "hello, public here"
print(a.public)
