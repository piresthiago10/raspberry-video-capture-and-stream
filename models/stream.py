# For more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# rtsp://admin:sde12345@192.168.10.102:554/cam/realmonitor?channel=2&subtype=0
import subprocess
import threading


class Stream(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="record_thread", daemon=True)
        self._codec = 'h264'
        self._width = '720'
        self._height = '480'
        self._framerate = '15'
        self._device = '/dev/video0'
        self._stream_ip = '18.9.98.125'
        self._stream_port = '80'

    def ffmpeg_stream(self):
        codec = self._codec
        video_size = f'{self._width}x{self._height}'
        framerate = self._framerate
        device = self._device
        rtsp = f'rtsp://admin:Dvr12345@192.168.10.101:554/cam/realmonitor?channel=4&subtype=0'

        ffmpeg_command = ["ffmpeg", "-input_format", codec,
                          "-f", "video4linux2", "-video_size", video_size, "-framerate", framerate,
                          "-i", device, "-c:v", "copy", "-an", "-f", "rtsp", rtsp]

        subprocess.call(ffmpeg_command)

    def run(self):

        try:
            self.ffmpeg_stream()
        except Exception as e:
            return e
