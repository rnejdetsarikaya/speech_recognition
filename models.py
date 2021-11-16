from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten

from keras.layers import Conv2D, MaxPooling2D, BatchNormalization 

def deep_cnn(features_shape, num_classes, act='relu'):

    x = Input(name='inputs', shape=features_shape, dtype='float32')
    o = x
    
    # Block 1
    #32:filters, konvolüsyon çıkış filtresinin sayısı/(3,3) boyutunda taranır stride=1 erli kaydırır
    #maxpooling2d de 3,3 pool sizedır
    #normalizasyon default parametreleri: axis = -1, momentum = 0.99, epsilon = 0.001,
    o = Conv2D(32, (3, 3), activation=act, padding='same', strides=1, name='block1_conv', input_shape=features_shape)(o)
    o = MaxPooling2D((3, 3), strides=(2,2), padding='same', name='block1_pool')(o)
    o = BatchNormalization(name='block1_norm')(o)
    
    # Block 2
    o = Conv2D(32, (3, 3), activation=act, padding='same', strides=1, name='block2_conv')(o)
    o = MaxPooling2D((3, 3), strides=(2,2), padding='same', name='block2_pool')(o)
    o = BatchNormalization(name='block2_norm')(o)

    # Block 3
    o = Conv2D(32, (3, 3), activation=act, padding='same', strides=1, name='block3_conv')(o)
    o = MaxPooling2D((3, 3), strides=(2,2), padding='same', name='block3_pool')(o)
    o = BatchNormalization(name='block3_norm')(o)

    # Flatten
    #son katmana verileri hazırlar
    o = Flatten(name='flatten')(o)
    
    # Dense layer(Full Connected Layer)
    #dropoutta 0.2 girişlerin azaltma oranıdır.
    o = Dense(64, activation=act, name='dense')(o)
    o = BatchNormalization(name='dense_norm')(o)
    o = Dropout(0.2, name='dropout')(o)
    
    # Predictions
    o = Dense(num_classes, activation='softmax', name='pred')(o)

    # Print network summary
    #print("summary")
    #Model(inputs=x, outputs=o).summary()
    return Model(inputs=x, outputs=o)