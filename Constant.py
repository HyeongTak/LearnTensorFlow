import tensorflow as tf

a = tf.constant([5],dtype=tf.float32)
b = tf.constant([10],dtype=tf.float32)
c = tf.constant([2],dtype=tf.float32)

d = a*b+c # 계산이 아닌 그래프 정의

# print(d) 할시 
# Tensor("add:0", shape=(1,), dtype=float32)가 출력됨.

sess = tf.Session() # 세션 생성
result = sess.run(d) # 그래프를 인자로 받아서 실행해줌.
print(result) # 계산 결과 출력