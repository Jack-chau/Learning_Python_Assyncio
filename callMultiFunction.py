import asyncio

async def getData ( ) :
    await asyncio.sleep ( 5 )
    print ( "After 5 second" )
    await asyncio.sleep ( 5 )
    print ( "After 10 second" )
    return { "data_1" : [ "120", "123" ] }

async def printFunction ( ) :
    for number in range ( 30 ) :
        print ( number )
        await asyncio.sleep ( 0.5 )

# set task
async def main () :
    task1 = asyncio.create_task ( getData() )
    task2 = asyncio.create_task ( printFunction() )

    # retrieve task1 data
    # use await means wait until finish task1.
    value = await task1
    print ( "finish task 1" )
    # wait for task 2 finish
    await task2
    print ( "finish task 2")
    print ( value )

asyncio.run ( main() )
