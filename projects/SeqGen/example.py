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
        time_step += 1
    
    pred = path_model.predict([x_latent, x_sent])
    return x_sent, time_step

def predict_next_char(x_latent, x_sent=None, time_step=0):

    x_latent = np.array(x_latent).reshape(1, 5)
    if x_sent is None:
        x_sent = np.zeros((1, 7, 4))
        x_sent[0, 0, 0] = 1
        time_step += 1

    char_index = np.argmax(pred[0])
    x_sent[0, time_step, char_index] = 1
    next_char = indices_char[char_index]
    if next_char == 'E':  # or max len -- check path_model summary
        print('Reached a leaf node.')
        return x_sent, pred[0], next_char
    return x_sent, pred[0], next_char


# Example
# response = get_outputs([1.0, -0.95, -0.91, 0.99, 0.29])
# state = np.array([[[1., 0., 0., 0.],
#                    [0., 0., 1., 0.],
#                    [0., 0., 0., 0.],
#                    [0., 0., 0., 0.],
#                    [0., 0., 0., 0.],
#                    [0., 0., 0., 0.],
#                    [0., 0., 0., 0.]]])
# response_2 = get_outputs([1.0, -0.95, -0.91, 0.99, 0.29], state, index=2)

# print(response_2)