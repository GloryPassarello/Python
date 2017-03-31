class test:
    def name_call(self, name):
        self.name = name
    def display(self):
        return self.name
    def introd(self):
        print "Hello, I am %s" % self.name


##usiing classes
#to  use a class a need to create a object


primo = test()
secondo = test()
terzo = test()

primo.name_call('luca')
secondo.name_call('anakin')
terzo.name_call('buddy')

primo.introd()
secondo.introd()
terzo.introd()
print primo.display()
