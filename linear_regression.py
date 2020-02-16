import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 일한 시간 
xData= [1,2,3,4,5,6,7]

# 일한시간에 따른 수당
yData= [25000,55000,75000,110000,128000,155000,180000]

#기울기
W=tf.Variable(tf.random_uniform([1],-100,100))

#y절편
b=tf.Variable(tf.random_uniform([1],-100,100))

#틀만들기
X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)
#가설
H=W*X+b

cost=tf.reduce_mean(tf.square(H-Y)) #reduce_mean = 평균값 구함

a=tf.Variable(0.01) #경사하강 알고리즘에서 얼마만큼 점프할지를 정한것 0.01만큼 점
optimizer = tf.train.GradientDescentOptimizer(a)
train=optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess =tf.Session()
sess.run(init)
for i in range(5001):
    sess.run(train,feed_dict={X: xData, Y: yData})
    if i % 500 ==0 :
        print(i, sess.run(cost,feed_dict={X : xData, Y:yData}),sess.run(W),sess.run(b))
print(sess.run(H,feed_dict={X:[8]}))
