#!/usr/bin/python

def faulty():
    raise Exception('Raise exception.')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except Exception as e:
        print "Catch exception."
        print e
    finally:
        print "Clean after exception."

# handle_exception()
x = None


x = 1/1
except Exception as e:
    print e
finally:
    print "del x"
    del x