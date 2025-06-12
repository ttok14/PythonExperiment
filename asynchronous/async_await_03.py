
# await 키워드로 wait 하기는 하지만 
# 동시 처리는 되지 않는 케이스 

import asyncio
import time

# async 로 코루틴 함수 만들기 
async def say_after(msg, delay):
    print(f"Before : {msg}")
    while True:
        pass
    await asyncio.sleep(delay)
    print(msg)
    
async def main():
    start_time = time.time()
    await asyncio.gather(
        say_after("Hello01", 1),
        say_after("Hello02", 2),
        say_after("Hello03", 3),
        say_after("Hello04", 4)
    )
    end_time = time.time()
    
    print(f"FINISHED in {end_time-start_time:.2f} seconds ")
    
asyncio.run(main())

print("Closing!")