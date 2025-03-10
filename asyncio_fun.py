import asyncio


async def func1():
	print("Function 1 started..")
	await asyncio.sleep(10)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(15)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(5)
	print("Function 3 Ended")


async def main():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")


asyncio.run(main())
