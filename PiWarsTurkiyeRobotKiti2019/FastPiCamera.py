
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
import cv2

class FastPiCamera:

    def __init__(self, resolution=(640, 480)):

        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.rawFrame = PiRGBArray(self.camera, size=self.camera.resolution)
        self.broadcast = self.camera.capture_continuous(self.rawFrame, format="bgr", use_video_port=True)
        self.currentFrame = None

        self.toShowOnWindow = dict()
        self.cameraViewingActive = False

    def startReadingData(self):

        Thread(target=self.__updateData__, args=()).start()
        return self

    def __updateData__(self):

        for f in self.broadcast:

            self.currentFrame = f.array
            self.rawFrame.truncate(0)

    def readData(self):

        return self.currentFrame

    def showFrame(self, windowName="frame", shownImage=None):
        if shownImage is None:
            self.toShownOnWindow[windowName] = self.currentFrame
        else:
            self.toShowOnWindow[windowName] = shownImage

        if not self.cameraViewingActive:
            Thread(target=self.__updateShownFrame__, args=()).start()

    def __updateShownFrame__(self):

        self.cameraViewingActive = True

        while True:

            for name in self.toShowOnWindow.copy():
                cv2.imshow(isim, self.toShowOnWindow[name])

            key = cv2.waitKey(1)

            if key == ord("q"):
                cv2.destroyAllWindows()
                break
