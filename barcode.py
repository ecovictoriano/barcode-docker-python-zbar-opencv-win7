import zbar
import cv2
import sys
import glob

class Barcode():
    @classmethod
    def Decode(self, img):
        image = cv2.imread(img)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        scanner = zbar.Scanner()
        results = scanner.scan(image)
        return results

if __name__ == '__main__':
    img = sys.argv[1]
    results = Barcode.Decode(img)
    for result in results:
        print(img + ' : ' + result.type, result.data)
