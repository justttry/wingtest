#encoding:UTF-8

import wingdbstub
import thread
wingdbstub.Ensure(require_connection=1, require_debugger=1)
wingdbstub.kEmbedded = 1
wingdbstub.kExitOnFailure = 1
thread_id = thread.get_ident()
wingdbstub.debugger.SetDebugThreads({thread_id:1})

print 'haha'

def f():
    return 'hello world'

print f()
a = 0
for i in xrange(1000):
    a += 1
print "Entered the debugger"

raw_input("Hit Enter to proceed")

print "\nAnother statement"
