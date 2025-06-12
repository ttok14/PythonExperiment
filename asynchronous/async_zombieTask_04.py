import asyncio
import time

# 1. 영원히 끝나지 않는 '좀비 작업'
async def infinite_waiter():
    """
    이 함수는 영원히 끝나지 않는 Future를 await하며 무한 대기 상태에 빠집니다.
    '좀비'가 되어 시스템에 계속 남아있게 됩니다.
    """
    print("🔴 [좀비 작업] 시작. 저는 영원한 대기에 들어갑니다...")
    
    # 해결(resolve)되지 않는 Future 객체를 생성합니다.
    # 이 Future를 await하면 영원히 기다리게 됩니다.
    #future = asyncio.Future()
    #await future 
    await asyncio.sleep(10)
    
    # 이 아래 코드는 절대 실행되지 않습니다.
    print("🔴 [좀비 작업] 이 메시지는 절대 출력되지 않습니다.")


# 2. 자기 할 일을 정상적으로 하는 '정상 작업'
async def normal_worker(worker_id):
    """
    이 함수는 정해진 시간 동안 일을 하고 정상적으로 끝나는 작업입니다.
    """
    print(f"🟢 [정상 작업 {worker_id}] 시작. 2초간 일하고 완료됩니다.")
    
    # asyncio.sleep은 CPU를 점유하지 않고 협조적으로 대기합니다.
    # 이 동안 이벤트 루프는 다른 일을 할 수 있습니다.
    await asyncio.sleep(2)
    
    print(f"🟢 [정상 작업 {worker_id}] 완료!")


# 3. 모든 작업을 조율하는 메인 함수
async def main():
    """
    메인 함수는 '좀비 작업'을 백그라운드에서 시작시키고,
    그 동안 '정상 작업'들을 순차적으로 실행하며 모든 것이 잘 돌아가는지 보여줍니다.
    """
    print("--- 시뮬레이션 시작 ---")
    
    # '좀비 작업'을 백그라운드에서 실행하도록 예약합니다.
    # create_task는 즉시 Task 객체를 반환하고, main 함수는 멈추지 않고 다음으로 진행합니다.
    zombie_task = asyncio.create_task(infinite_waiter())
    print(type(zombie_task))
    zombie_task.cancel
    
    # 좀비 작업이 시작될 시간을 주기 위해 아주 잠시 기다립니다.
    await asyncio.sleep(0.1)

    print("\n이제 좀비 작업이 백그라운드에서 무한 대기하는 동안,")
    print("메인 루프는 다른 정상 작업들을 계속 처리합니다.\n")

    # 3개의 정상 작업을 순차적으로 실행해 봅니다.
    for i in range(1, 4):
        print(f"▶️ [메인 루프] '정상 작업 {i}'를 호출합니다.")
        await normal_worker(i)
        print(f"◀️ [메인 루프] '정상 작업 {i}'가 끝났으므로 다음으로 진행합니다.\n")

    print("--- 시뮬레이션 완료 ---")
    print("모든 정상 작업이 성공적으로 끝났습니다.")
    print("하지만 좀비 작업은 여전히 백그라운드에서 대기 중입니다.")
    print("프로그램을 종료하려면 Ctrl+C를 누르세요.")

# --- 실행 ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")