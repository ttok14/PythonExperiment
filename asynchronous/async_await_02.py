
# await 키워드로 wait 하기는 하지만 
# 동시 처리는 되지 않는 케이스 

import asyncio
import time

# async 로 코루틴 함수 만들기 
async def say_after(msg, delay):
    # await 키워드뒤에 오는 작업이 끝날때까지 대기함 
    # asyncio.sleep 은 해당 시간만큼 대기하되
    # 전체 프로그램을 멈추진 않음 
    await asyncio.sleep(delay)
    print(msg)
    
async def main():
    start_time = time.time()
    # 1초 후에 메시지 출력 
    await say_after("Hello01", 1)
    # 2초 후에 메시지 출력
    await say_after("Hello02", 2)
    end_time = time.time()
    
    print(f"FINISHED in {end_time-start_time:.2f} seconds ")
    
asyncio.run(main())

print("Closing!")