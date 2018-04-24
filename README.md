# Speech Commands Example

This is a basic speech recognition example. For more information, see the
tutorial at https://www.tensorflow.org/versions/master/tutorials/audio_recognition.

# generate frozen model file
python freeze.py \
--start_checkpoint=/model/02_speech_command_sp/speech_commands_train/conv/conv.ckpt-100 \
--output_file=/model/02_speech_command_sp/my_frozen_graph_conv.pb



# use mobilenet v2 model
python freeze.py \
--start_checkpoint=/model/02_speech_command_sp/speech_commands_train/mobilenetv2/mobilenetv2.ckpt-800 \
--output_file=/model/02_speech_command_sp/my_frozen_graph_mobilenetv2.pb

# validation

python label_wav.py \
--graph=/model/02_speech_command_sp/my_frozen_graph_conv.pb \
--labels=/model/02_speech_command_sp/speech_commands_train/mobilenetv2/mobilenetv2_labels.txt \
--wav=/data/speech_command/speech_dataset/stop/1a6eca98_nohash_0.wav

