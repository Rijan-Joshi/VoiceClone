from voice_test import VoiceTest
import time

if __name__ == "__main__":
    voice_test = VoiceTest()
    voice_test.opevoice_v2_test()

    start_time = time.time()
    voice_test.openvoice(
        "Accessing alarm and interface settings, in this window you can set up your customized greeting and alarm preferences. Hello Sir, What can I do for you today?"
    )
    end_time = time.time()
    print(f"⏰ Openvoice Execution Time: {end_time - start_time}")
    print("Openvoice ended")
