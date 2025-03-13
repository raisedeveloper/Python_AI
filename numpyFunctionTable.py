"""<함수(), 설명과 예시>
    np.array() : 리스트를 Numpy 배열로 변환 
                import numpy as np
                arr = np.array([1,2,3])
                print(arr)
                
    np.arange(): 주어진 범위 내에서 일정한 간격의 값을 가지는 배열 생성
                arrange(시작값, 종료값, 건너뛰기)
                arr = np.arange(0, 10, 2) #2씩 증가
                
    np.random.rand() : 0과 1사이의 균일 분포를 따르는 난수 생성
                       np.random : 난수생성, rand: 0~1난수
                       arr = np.random.rand(3,3)
                       
    np.reshape : 배열의 shape 변경
                arr = arr.reshape(1, 9)
                
    np.sum() : 배열 요소의 합
               np.sum([1,2,3]) # 출력값 : 6 
               
    np.mean() : 배열 요소의 평균
                np.mean([1,2,3]) # 출력값 : 2
                
    np.std() : 배열 요소의 표준편차 계산
                np.std([1,2,3]) # 출력값 : 0.816 """