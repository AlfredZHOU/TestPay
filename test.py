import audio_analysis_wrapper
import numpy as np

def test_analyze_audio_pcm():

    sample_rate = 44100
    pcm_data = np.random.randint(-32768, 32767, size=sample_rate * 1, dtype=np.int16)  # 1 seconds of PCM data
    result = audio_analysis_wrapper.analyze_audio_pcm_wrapper(pcm_data, sample_rate)
    print("Analysis result:")
    print(result)

if __name__ == "__main__":
    test_analyze_audio_pcm()
