#encoding utf-8

import asyncio
import datetime,time
 
now = lambda: time.time()
 
async def do_some_work(x,name):
    print('Waiting: ', name)
    await asyncio.sleep(x)
    print('Waitingss: ', name)

async def do_some_works(x,name):
	print('Waiting_works: ', name)
	with open('1.txt','w') as f:
		f.write('Hello, world!')
	print(datetime.datetime.now())
	await asyncio.sleep(x)
	print(datetime.datetime.now())
    # print('Waiting_works: ', name)
    # 
    # print('Waitingss_works: ', name)
 
start = now()

loop = asyncio.get_event_loop()
task = [
	# asyncio.ensure_future(do_some_work(2,1)),
	asyncio.ensure_future(do_some_works(2,2)),
	# asyncio.ensure_future(do_some_work(2,3))
]
print(123)
print(datetime.datetime.now())
loop.run_until_complete(asyncio.wait(task))
print('TIME: ', now() - start)