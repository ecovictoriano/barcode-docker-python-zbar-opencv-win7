import zbar, cv2, sys, glob
from barcode import Barcode

dirpath = '/py/images/**/'
filetypes = ('*.png', '*.jpg')
images = []
decoded = 0

for files in filetypes:
    images.extend(glob.glob(dirpath + files))

for img in images:
    results = Barcode.Decode(img)
    decoded += 1 if len(results) else 0
    for result in results:
        print(img + ' : ' + result.type, result.data)
        # print(result.type, result.data, result.quality, result.position)

print('')
print('Total image : ' + str(len(images)))
print('Total decoded : ' + str(decoded))
