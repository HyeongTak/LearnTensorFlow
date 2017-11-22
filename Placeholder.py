import tensorflow as tf

input_data = [1,2,3,4,5]
x = tf.placeholder(dtype=tf.float32) # 플레이스홀더 선언
y = x*2 # 그래프 정의

sess = tf.Session()
result = sess.run(y,feed_dict={x:input_data}) # 플레이스홀더 x 를 통해 input_data 전달

print(result)
