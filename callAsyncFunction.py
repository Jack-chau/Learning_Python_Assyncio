import asyncio
import time

# Use async will return a coroutine object

async def main ( text ) :
    start_time = time.time()
    print ( text )
    # use await to call coroute object
    await secondFun( "This is second function" )
    print ( "Finish" )
    end_time = time.time()
    total_time = end_time - start_time
    print ( f'total time consumed: {total_time}.' )

async def secondFun ( text ) :
    # use await to call coroutine object
    start_time = time.time()
    await asyncio.sleep ( 3 )
    mid_time = time.time()
    time_consumed_1 = mid_time - start_time
    print ( time_consumed_1 )
    print ( text )
    await asyncio.sleep ( 5 )
    end_time = time.time()
    time_consumed_2 = ( end_time - mid_time )
    print ( time_consumed_2 )

asyncio.run ( main( "This is main function" ) )