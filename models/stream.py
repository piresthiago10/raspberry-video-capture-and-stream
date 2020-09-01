# For more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import subprocess

import cv2
import ffmpeg
import numpy as np


class Stream():
    def __init__(self):
        self._codec = 'h264'
        self._width = '1920'
        self._heigth = '1080'
        self._framerate = '30'
        self._device = '/dev/video0'
        self._stream_ip = '18.9.98.125'
        self._stream_port = '80'

    def ffmpeg_stream(self):
        codec = self._codec
        video_size = f'{self._width}x{self._height}'
        framerate = self._framerate
        device = self._device
        rstp = f'rtsp://{self._stream_ip}:{self._stream_port}/live/stream'

        self._rtsp = 'rtsp://18.9.98.125:80/live/stream'
        subprocess.call(
            f'ffmpeg -input_format {codec} -f video4linux2 -video_size {video_size} -framerate {framerate} -i {device} -c:v copy -an -f rtsp {rtsp}')
        # ffmpeg -input_format yuyv422 -f video4linux2 -s 1280x720 -r 10 -i /dev/video0 -c:v h264_omx -r 10 -b:v 2M -an -f rtsp rtsp://localhost:80/live/stream


# # Playing video from file:
# # cap = cv2.VideoCapture('vtest.avi')
# # Capturing video from webcam:
# cap = cv2.VideoCapture(0)

# currentFrame = 0
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Handles the mirroring of the current frame
#     frame = cv2.flip(frame, 1)

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Saves image of the current frame in jpg file
#     # name = 'frame' + str(currentFrame) + '.jpg'
#     # cv2.imwrite(name, frame)

#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     # To stop duplicate images
#     currentFrame += 1

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# # Potential Error:
# # OpenCV: Cannot Use FaceTime HD Kamera
# # OpenCV: camera failed to properly initialize!
# # Segmentation fault: 11
# #
# # Solution:
# # I solved this by restarting my computer.
# # http://stackoverflow.com/questions/40719136/opencv-cannot-use-facetime/42678644#42678644
