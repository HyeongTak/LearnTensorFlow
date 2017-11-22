# LearnTensorFlow
텐서플로우 공부.


### 1. Constant.py
constant는 상수를 저장하는 데이터 형이다.
#### tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
와 같이 정의한다.

* value = 상수의 값
* dtype = 상수의 데이터형
* shape = 행렬의 크기 ex)shape = [1,2]
* name = 상수의 이름

### 2. Placeholder.py

placeholder는 입력 데이터를 위한 데이터 타입이다.

그래프에서 입력값(X)을 저장하는 일종의 통(버킷)이다.
#### tf.placeholder(dtype, shape, name)
와 같이 정의한다.
