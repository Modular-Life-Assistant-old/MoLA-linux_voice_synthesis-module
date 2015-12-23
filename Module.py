from helpers.modules.VoiceSynthesisModule import VoiceSynthesisModule

import os


class Module(VoiceSynthesisModule):
    voice_quality = 5

    def is_available(self):
        return os.system('pico2wave --help > /dev/null') == 0 and \
            os.system('aplay --help > /dev/null') == 0

    def textToSpeak(self, msg):
        msg = msg.replace('"', '\'')  # security
        path = '/tmp/pico2wave.wav'
        os.system(
            'pico2wave -l fr-FR -w %s "%s" && aplay %s' % (path, msg, path)
        )