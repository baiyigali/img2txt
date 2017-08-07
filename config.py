#img2txt_using_lstm = {
#    'minibatch_size': 32,
##    'embedding_size': 256,
#    'embedding_size': 512,
#    'max_sequence_length': 20,
#    'rnn_cell': {
##        'type': 'lstm',
#        'type': 'lstm_block',
##        'num_units': 256,
#        'num_units': 512,
#        'forget_bias': 1.0,
#        'use_peepholes': False,
#        'dropout_keep_probability': 0.7,
#    },
#    'variable_initializer': {
#        'mean': 0,
#        'stddev': 0.02,
#    },
#    'optimizer': {
#        'initial_learning_rate': 2.0,
#        'learning_rate_decay_rate': 0.5,
#        'num_epochs_per_decay': 8.0,
#        'gradient_clip_norm': 5.0,
#    },
#    'convnet': {
#        'name': 'inception_v3',
#        'train_dataset': 'imagenet',
#        'pretrained_model_file_path': 'pretrained/inception_v3.ckpt',
#        'input_image_shape': [299, 299, 3],
#    },
##    'convnet': {
##        'name': 'inception_v4',
##        'train_dataset': 'imagenet',
##        'pretrained_model_file_path': 'pretrained/inception_v4.ckpt',
##    },
##    'convnet': {
##        'name': 'vgg16',
##        'train_dataset': 'imagenet',
##        'pretrained_model_file_path': 'pretrained/vgg16_weights.h5',
##        'input_image_shape': [224, 224, 3],
##    },
#    'num_examples_per_epoch': None,
#    'num_training_epochs': 15,
#    'beam_size': 3,
#}
