# 내 파이썬 프로그램의 이름을 알아보자.
# psutil로 지금 돌아가고 있는 프로세스에 한 번씩 접근한다.
# 내가 지금 돌리고 있는 이 파일과 일치하는 프로세스를 발견하게 되면 그 이름을 출력하는 코드

# 1. 실행 중인 프로세스에 순차적으로 접근한다.
# 2. 만일 프로세스의 pid가 내 파이썬 프로그램의 pid와 같으면
# 3. 해당 프로세스의 이름을 출력한다.

# hint : os 모듈의 getpid() 함수와 psutil의 pid 속성 간 어떤 차이가 있는지 알면 된다.

import psutil
import os

my_pid = os.getpid()

for p in psutil.process_iter():

    p_name = p.name()
    p_id = p.pid

    if my_pid == p_id:
        print(f'프로세스 pid : {p_id}')
        print(f'현재 파이썬 프로그램의 pid : {my_pid}')
        print(f'해당 프로세스 이름 : {p_name}')