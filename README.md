# Speech Commands Example

This is a basic speech recognition example. For more information, see the
tutorial at https://www.tensorflow.org/versions/master/tutorials/audio_recognition.

# generate frozen model file
python freeze.py \
--start_checkpoint=/model/02_speech_command_sp/speech_commands_train/conv/conv.ckpt-100 \
--output_file=/model/02_speech_command_sp/my_frozen_graph_conv.pb