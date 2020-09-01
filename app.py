from models import stream

Stream = stream.Stream()

if __name__ == "__main__":

    try:
        ffmpeg_stream = Stream.ffmpeg_stream()
    except Exception as e:
        print(e)