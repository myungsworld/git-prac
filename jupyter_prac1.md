```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```

    WARNING:tensorflow:From C:\Users\Owner\Anaconda3\lib\site-packages\tensorflow_core\python\compat\v2_compat.py:65: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
    Instructions for updating:
    non-resource variables are not supported in the long term
    


```python
a=tf.placeholder("float")
b=tf.placeholder("float")

y=tf.multiply(a,b)

sess=tf.Session()
print (sess.run(y,feed_dict={a:3,b:3}))
```
