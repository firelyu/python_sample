#!/usr/bin/python

class Bird:
    '''
    This is class bird.
    '''
    level = 0
    def __init__(self):
        Bird.leve = 0

    def hello(self):
        print "I am a bird."

class Swarm(Bird):
    '''
    This is class swarm.
    '''
    def __init__(self):
        Swarm.level = 1

    def hello(self):
        print "I am a swarm."

b = Bird()
b.hello()
print b.level

s = Swarm()
s.hello()
print s.level
print "Swarm.__bases__ %r" % (Swarm.__bases__)
print "Swarm.__dict__ %r" % (Swarm.__dict__)
print "Swarm.__module__ %r" % (Swarm.__module__)
print "Swarm.__doc__ %r" % (Swarm.__doc__)

print "s.__class__ %r" % (s.__class__)