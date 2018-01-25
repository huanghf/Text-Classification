from keras.models import Sequential
from keras.layers.core import Masking, Dense, initializers
from keras.layers import Conv1D
from keras.layers import Conv1D
from parameter.optimizers import optimizers


def neural_Conv1D(input_shape,
                  net_conv_num=[64, 64],
                  kernel_size=[5, 5],
                  net_dense_shape=[128, 64, 2],
                  optimizer_name='Adagrad',
                  lr=0.001):
    '''
    
    :param input_shape: 样本数据格式
    :param net_shape: 神经网络格式
    :param optimizer_name: 优化器
    :param lr: 学习率
    '''
    model = Sequential()
    # 增加Conv1D层

    for n in range(len(net_conv_num)):
        model.add(Conv1D(input_shape=input_shape,
                         filters=net_conv_num[n],  # 卷积核数量
                         kernel_size=kernel_size[n],  # 卷积核尺寸，或者[3]
                         strides=1,
                         padding='same',
                         activation='relu',
                         kernel_initializer=initializers.normal(stddev=0.1),
                         bias_initializer=initializers.normal(stddev=0.1),
                         name='Conv1D_'+str(n)))
    # 增加全连接隐藏层
    for n, units in enumerate(net_dense_shape[0:-1]):
        model.add(Dense(units=units,
                        activation='relu',
                        kernel_initializer=initializers.normal(stddev=0.1),
                        name='Dense_' + str(n)))
    # 增加最后的softmax层
    model.add(Dense(units=net_dense_shape[-1],
                    activation='softmax',
                    kernel_initializer=initializers.normal(stddev=0.1),
                    name='softmax'))

    optimizer = optimizers(name=optimizer_name, lr=lr)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    return model


if __name__ == '__main__':
    model = neural_Conv1D(input_shape=[10, 5],
                          net_conv_num=[64, 64],
                          kernel_size=[5, 5],
                          net_dense_shape=[128, 64, 2],
                          optimizer_name='Adagrad',
                          lr=0.001)
    model.summary()
