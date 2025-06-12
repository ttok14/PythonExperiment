
import time

def generator_func():
    for i in range(0,10):
        # 3. 'yield i' 문을 만나는 순간 i 값을 밖으로 리턴함과
        #       동시에 실행이 중단됨. 
        # 5. yield i 는 외부에서 보낸 1000 이란 값을 반환하고
        #       received_from_outside 에는 1000 이 들어간다.
        #       이후에는 다시 yield 를 만날때까지 실행을 쭉 한다.
        #       그 뒤로는 3. ~ 을 반복한다. 
        received_from_outside = yield i
        print(received_from_outside)
        
        time.sleep(1)

# 1. 제너레이터 객체 생성
gen = generator_func()
# 2. next(gen) 로 generator_func() 실행을 
#       시작, 및 yield 를 만날때까지 진행해서 값을 리턴받음
received_from_inside = next(gen)

# 4. 현재 generator_func() 은 'yield i' 문에서 멈춘 상태이며,
#       이때 send(1000) 함수를 통해서 현재 멈춘 'yield i' 이
#       1000 을 반환하게끔 보낸다. 
received_from_inside = gen.send(1000)
received_from_inside = gen.send(2000)
received_from_inside = gen.send(3000)
received_from_inside = gen.send(4000)