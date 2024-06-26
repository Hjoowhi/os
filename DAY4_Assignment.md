## 일일과제

### 스레싱 (thrashing)

가상 메모리란 실제 메모리 크기보다 더 큰 프로세스들을 관리하기 위해 존재하는 기술이다. 가상 메모리를 구현해 다중 프로그래밍(multi programming)울 하면 CPU 이용률이 높아진다. 일정 수 이상으로 다중 프로그래밍을 하여 프레임이 부족하면(메모리가 부족한 것은 가상 메모리 관점에서 설명하면 '프레임이 부족하다.'라고 표현할 수 있다) 페이지 폴트(page fault)가 자주 발생한다. 페이지 폴트가 발생하면 매끄러운 작업이 진행되지 않고 잦은 스와핑 작업으로 인해 CPU 사용률이 떨어지게 된다. 

CPU 사용률이 떨어지면 운영체제는 더 많은 프로세스를 메모리에 올리려 하고, 이는 더 잦은 페이지 폴트로 이어져 악순환에 빠지게 된다. 프로세스가 실제 실행되는 시간보다 페이징에 더 많은 시간을 소요하느라고 성능이 떨어지는 문제를 **"스레싱(trashing)"**이라 한다.

성능 저하를 막기 위해 운영체제가 페이지와 프레임의 갯수를 잘 관리해 주는 것이 중요하다. 프로세스 실행을 위해 각 프로세스의 프레임을 할당할 때 프레임을 너무 많이 할당하면 다른 프로세스들이 사용할 프레임이 줄어든다. 반면 너무 적은 프레임을 할당하면 페이지 폴트가 빈번하게 발생할 수 있다. 각 프로세스들이 무리없이 실행될 수 있는 선에서 최소한의 프레임 수를 파악하고 프로세스들이 적절한 수만큼 프레임을 할당해 줄 수가 있어야 한다. 

### 워킹 세트 (working set)

지역성을 기반으로 자주 사용하는 페이지를 저장해 주는 것을 의미한다. "워킹 세트"를 바탕으로 자주 사용하는 페이지를 물리 메모리의 프레임에 고정하면 페이지 폴트가 빈번하게 발생하는 현상을 방지할 수 있다.