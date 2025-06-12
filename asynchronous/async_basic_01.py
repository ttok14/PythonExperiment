
# asyncio 로 비동기 처리 관련 모듈 임포트 
import asyncio

# def 앞에 async 키워드를 붙이면 
# 해당 함수는 코루틴 함수가됨 
async def main():
    print("바로 출력!")

# main() 은 코루틴 객체를 리턴함
coroutine = main()

# 'coroutine' 출력
print(type(coroutine))

# 코루틴 함수를 실행할때는 코루틴 객체를 
# asyncio.run 에 넘김 
asyncio.run(coroutine)