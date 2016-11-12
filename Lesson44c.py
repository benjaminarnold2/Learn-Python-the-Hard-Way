class Parent(object):

    def altered(self):

        print "Parent altered()"


class Child(Parent):

    def altered(self):

        print "Child, before Parent altered()"
        super(Child, self).altered()
        print "Child, after Parent altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

print getattr(dad)
