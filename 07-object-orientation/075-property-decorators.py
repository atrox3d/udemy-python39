class A():
    __private = 'private'

    @property
    def public(self):
        return self.__private

    @public.setter
    def public(self, private):
        self.__private = private


a = A()
print(a.public)
a.public = "hello, public here"
print(a.public)
