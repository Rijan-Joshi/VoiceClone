import os
import torch
from melo.api import TTS
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
import pygame as pg
import time


class VoiceTest:
    def __init__(self):
        self.ckpt_converter = "modules/OpenVoice/checkpoints_v2/converter"
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.output_dir = "outputs_v2"
        self.tone_color_converter = ToneColorConverter(
            f"{self.ckpt_converter}/config.json", device=self.device
        )
        self.tone_color_converter.load_ckpt(f"{self.ckpt_converter}/checkpoint.pth")

        os.makedirs(self.output_dir, exist_ok=True)

    def opevoice_v2_test(self):
        reference_speaker = "modules/OpenVoice/resources/example_reference.mp3"  # This is the voice you want to clone
        target_se, audio_name = se_extractor.get_se(
            reference_speaker, self.tone_color_converter, vad=True
        )

        texts = {
            "EN_NEWEST": "Hey, this is Next Wave AI. Do you want to know more about our latest update?",  # The newest English base speaker model
            "EN": "Hey, this is Next Wave AI. Do you want to know more about our latest update?",
            # 'ES': "El resplandor del sol acaricia las olas, pintando el cielo con una paleta deslumbrante.",
            # 'FR': "La lueur dorée du soleil caresse les vagues, peignant le ciel d'une palette éblouissante.",
            # 'ZH': "在这次vacation中，我们计划去Paris欣赏埃菲尔铁塔和卢浮宫的美景。",
            # 'JP': "彼は毎朝ジョギングをして体を健康に保っています。",
            # 'KR': "안녕하세요! 오늘은 날씨가 정말 좋네요.",
        }

        src_path = f"{self.output_dir}/tmp.wav"

        # Speed is adjustable
        speed = 1.0

        for language, text in texts.items():
            model = TTS(language=language, device=self.device)
            speaker_ids = model.hps.data.spk2id

            for speaker_key in speaker_ids.keys():
                speaker_id = speaker_ids[speaker_key]
                speaker_key = speaker_key.lower().replace("_", "-")
                print(f"Speaker ID: {speaker_key}")
                source_se = torch.load(
                    f"modules/OpenVoice/checkpoints_v2/base_speakers/ses/{speaker_key}.pth",
                    map_location=self.device,
                )
                model.tts_to_file(text, speaker_id, src_path, speed=speed)
                save_path = f"{self.output_dir}/output_v2_{speaker_key}_{language}.wav"

                # Run the tone color converter
                encode_message = "@MyShell"
                self.tone_color_converter.convert(
                    audio_src_path=src_path,
                    src_se=source_se,
                    tgt_se=target_se,
                    output_path=save_path,
                    message=encode_message,
                )

                self.play_audio(save_path)

    def openvoice(self, text):
        reference_speaker = "modules/openvoice/resources/demo_speaker2.mp3"  # This is the voice you want to clone
        target_se, audio_name = se_extractor.get_se(
            reference_speaker, self._tone_color_converter, vad=True
        )
        source_se = torch.load(
            f"modules/openvoice/checkpoints_v2/base_speakers/ses/en-newest.pth",
            map_location=self._device,
        )
        save_path = f"{self.output_dir}/output.wav"
        src_path = self.melotts(text, standalone=False)
        # Run the tone color converter
        encode_message = "@MyShell"
        self._tone_color_converter.convert(
            audio_src_path=src_path,
            src_se=source_se,
            tgt_se=target_se,
            output_path=save_path,
            message=encode_message,
        )
        self.play_audio(save_path)

    def melotts(self, text, standalone=False):
        start = time.time()
        model = TTS(
            language="EN_NEWEST",
            device="cpu",
            ckpt_path="modules/melo/checkpoints/checkpoint.pth",
            config_path="modules/melo/checkpoints/config.json",
        )
        src_path = f"{self.output_dir}/tmp.wav"

        # Speed is adjustable
        speed = 1.1
        model.tts_to_file(text, 3, src_path, speed=speed)
        end = time.time()
        print("⏰ Melo TTS Execution Time: ", end - start)
        return self.play(src_path) if standalone else src_path

    def play_audio(self, audio_path):
        pg.mixer.init()
        pg.mixer.music.load(audio_path)
        pg.mixer.music.play()

        while pg.mixer.music.get_busy():
            pg.time.Clock().tick(10)

        pg.mixer.music.stop()
        pg.mixer.quit()
