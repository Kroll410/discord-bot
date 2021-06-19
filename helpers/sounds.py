import random
import pyttsx3
from pydub import AudioSegment
import os


def create_concat_sound(channel_user_name):
    chosen_pidor_setup = random.choice([x for x in os.listdir('mp3') if x.startswith('p')])

    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('voice', 'default')
    engine.save_to_file(channel_user_name, f'tmp_{channel_user_name}.mp3')
    engine.runAndWait()

    sound_1 = AudioSegment.from_mp3(f'mp3/{chosen_pidor_setup}')
    sound_2 = AudioSegment.from_mp3(f'tmp_{channel_user_name}.mp3')

    combined = sound_1 + sound_2
    combined.export(f'f_tmp_{channel_user_name}.mp3')
    return f'f_tmp_{channel_user_name}.mp3'


def delete_concat_sound():
    for file in os.listdir():
        if file.startswith('f_') or file.startswith('tmp_'):
            os.remove(file)