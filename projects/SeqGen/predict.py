import numpy as np
from keras.models import model_from_json


chars = ['S', 'L', 'R', 'E']
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))


def load_model(model_name):
    json_file = open(model_name + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(model_name + ".h5")
    print("Loaded model from disk")

    loaded_model.compile(
        optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return loaded_model


path_model = load_model('path_model')


def predict_next_char(x_latent, x_sent=None, time_step=0):

    x_latent = np.array(x_latent).reshape(1, 5)
    if x_sent is None:
        x_sent = np.zeros((1, 7, 4))
        x_sent[0, 0, 0] = 1
    
    pred = path_model.predict([x_latent, x_sent])
    time_step += 1
    return x_sent, pred[0], time_step

#########
# Seq Generation Example 
##########

# example to predict one character at a time

# initialize the end-of-sentence token to False
EOS = False
# intialize char encoding matrix of size (1, max_seq_len, max_vocab_size)
x_sent = np.zeros((1, 7, 4))
x_sent[0, 0, 0] = 1
time_step = 0
x_latent = [1.0, -0.95, -0.91, 0.99, 0.29]
sent = []
max_len  = 5
print(' --- example begin ---')
while not EOS:
    x_sent, prob, time_step = predict_next_char(x_latent, x_sent, time_step)
    # take the char with max prob
    char_index = np.argmax(prob)
    # mark that we predicted the above char at this time_step
    x_sent[0, time_step, char_index] = 1
    # if this char is 'E', end-of-token, stop
    next_char = indices_char[char_index]
    if next_char == 'E':  # or max len -- check path_model summary
        print('Reached a leaf node/ goal state.')
        EOS = True
    sent.append(next_char)
    print('time_step',time_step)
    print('sent',sent)
    print('x_sent',x_sent)
    
    if len(sent) > max_len:
        EOS = True
print(' --- example done ---')


#########
# Next Character Generation Example 
##########

# Example
time_step = 0
x_sent, prob, time_step = predict_next_char([1.0, -0.95, -0.91, 0.99, 0.29])
# simply selecting "R" char as the predicted char
# update the x_sent encoding matrix
state = np.array([[[1., 0., 0., 0.],
                    [0., 0., 1., 0.],
                    [0., 0., 0., 0.],
                    [0., 0., 0., 0.],
                    [0., 0., 0., 0.],
                    [0., 0., 0., 0.],
                    [0., 0., 0., 0.]]])
# move the pointer to predict next string
x_sent, prob, time_step = predict_next_char([1.0, -0.95, -0.91, 0.99, 0.29], x_sent=state, time_step=2)
print(prob)
print(time_step)
print(x_sent)