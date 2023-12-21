from pydub import AudioSegment
import math

def slice_audio(file_path, chunk_length_ms=4950):
    audio = AudioSegment.from_file(file_path)

    number_of_chunks = math.ceil(len(audio) / chunk_length_ms)

    for i in range(number_of_chunks):
        start_time = i * chunk_length_ms
        end_time = min((i + 1) * chunk_length_ms, len(audio))
        chunk = audio[start_time:end_time]

        if len(chunk) > chunk_length_ms:
            chunk = chunk[:chunk_length_ms - .1]

        chunk_name = f"chunk{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        print(f"DROPPED {chunk_name}")

slice_audio("C:\\Users\\cache\\Music\\Everything Boz -(Without Coi Leray).mp3")
