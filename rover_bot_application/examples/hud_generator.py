"""
gst-launch-1.0 udpsrc port=5000 \
! application/x-rtp, encoding-name=JPEG,payload=26 \
! rtpjpegdepay \
! jpegdec \
! fpsdisplaysink

"""
from threading import Timer
import cv2
import numpy as np


WIDTH = 320
HEIGHT = 240
FPS = 20
INTERVAL = 1 / FPS

font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (150, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 255, 255)
# Line thickness of 2 px
thickness = 2

PIPE = f"""appsrc 
! video/x-raw, width={WIDTH}, height={HEIGHT}, framerate={FPS}/1,format=BGR 
! videoconvert 
! video/x-raw,format=I420 
! jpegenc 
! rtpjpegpay 
! udpsink host=127.0.0.1 port=5000"""


class HUDGen:
    def __init__(self) -> None:
        self.out = cv2.VideoWriter(
            PIPE, cv2.CAP_GSTREAMER, 0, FPS, (WIDTH, HEIGHT), True
        )

    def send(self):
        try:
            frame = self.gen()
            self.out.write(frame)
        finally:
            Timer(interval=INTERVAL, function=self.send).start()

    def gen(self):
        image = np.zeros([HEIGHT, WIDTH, 3], dtype=np.uint8)
        image = cv2.putText(
            image, "OpenCV", org, font, fontScale, color, thickness, cv2.LINE_AA
        )
        return image

    def run(self):
        t = Timer(interval=INTERVAL, function=self.send)
        t.start()


if __name__ == "__main__":
    hud_gen = HUDGen()
    hud_gen.run()
