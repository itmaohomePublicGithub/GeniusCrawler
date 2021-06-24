#coding:utf-8
'''
SpiderUtils  ---> com.taobao.tes.py
date：2021-06-24
Anchor：Levon
'''
import ctypes
import inspect
import threading
import asyncio

class Asyncs(object):
    def __init__(self):
        self.loop = None
        self.Threads = Threads()
        self.GCTasks = []
    def _handler_push_tasks(self,fn,**args):
        args = args or {}
        if len(args)==0:
            self.GCTasks.append(fn())
        else:
            self.GCTasks.append(fn(**args))
    def _handler_async_start(self):
        try:
            self.loop = asyncio.get_event_loop()
        except:
            self.loop = asyncio.new_event_loop()
        result = self.loop.run_until_complete(asyncio.gather(*self.GCTasks))
        self.GCTasks.clear()
        return result or None
    def _handler_start(self,fn,*args):
        try:
            self.loop = asyncio.get_event_loop()
        except:
            self.loop = asyncio.new_event_loop()
        args = args or None
        if len(args) == 1:
            result = self.loop.run_until_complete(asyncio.gather(fn()))
        else:
            result = self.loop.run_until_complete(asyncio.gather(fn(args)))
        return result[0] or None

class EventCallback(Asyncs):

    def handler_start_callback(self,func,callback,*args):
        args = args or None
        return callback(func(args)) if args is not None else callback(func())
    def handler_callback(self,func,**args):
        return func(**args)
    def handler_stop(self):
        self.Threads.handler_stop()

    def handler_async_push_tasks_callback(self,fn,**args):
        args = args or None
        self._handler_push_tasks(fn,**args)

    def handler_async_start_callback(self,callback,handlerData=None):
        if handlerData is not None:
            return handlerData(callback(self._handler_async_start()))
        return callback(self._handler_async_start())

    def handler_async(self,func,callback,*args):
        result = self._handler_start(func,args)
        callback(result)

class GCEvent(EventCallback):
    def start_new_Thread(self,fn,callback,*args):
        self.handler_start_callback(fn,callback,*args)
    def Async_new_start(self,fn,callback,*args):
        self.handler_async(fn,callback,args)
    def handler_received(self,fn):
        pass




class Threads():
    def __init__(self):
        self.thread = None
    def _async_raise(self,tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    def stop_thread(self,thread):
        self._async_raise(thread.ident, SystemExit)
    def handler_start(self,fn,*args):
        args = args or None
        if args is not None:
            self.thread = threading.Thread(target=fn,args=(args))
        else:
            self.thread = threading.Thread(target=fn)
        self.thread.setDaemon(True)
        self.thread.start()
        self.thread.join()
    def handler_stop(self):
        self.stop_thread(self.thread)









