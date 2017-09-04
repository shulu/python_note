# -*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello Again! (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()