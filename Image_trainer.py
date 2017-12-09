import tensorflow as tf, sys
# This is our variable to store the user input path
image_path = sys.argv[0]


# read the image data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()


label_lines = [line.rstrips() for line
               in tf.gfile.GFile("")]

#Unpersists graph from file

with tf.gfile.FastGFile("", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')










