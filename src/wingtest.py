#encoding:UTF-8

import wingdbstub
import thread
wingdbstub.Ensure(require_connection=1, require_debugger=1)
wingdbstub.kEmbedded = 1
thread_id = thread.get_ident()
wingdbstub.debugger.SetDebugThreads({thread_id:1})

print 'haha'

def f():
    return 'hello world'

print f()