import mmcv
import numpy as np
import random


img = mmcv.imread('demo.jpg') # read the image
img_gray = mmcv.imread('demo.jpg', flag='grayscale') # read the image in grayscale
# mmcv.imshow(img_gray) # display the image
mmcv.imwrite(img_gray, 'demo_output_gray.jpg') # save the image

# read image from bytes
with open('demo.jpg', 'rb') as f:
    data = f.read()

img_bytes = mmcv.imfrombytes(data)
# mmcv.imshow(img_bytes)


# generate random image
for i in range(10):
    img_range = np.random.randint(256, size=(500, 500, 1), dtype=np.uint8)
    # mmcv.imshow(img_range, win_name='test_img', wait_time=500)

# Resizing the image
# mmcv.imshow(mmcv.imresize(img, (800, 1000))) # resize by dimensions
# mmcv.imshow(mmcv.imrescale(img, 0.25)) # resize by ratio
# mmcv.imshow(mmcv.imresize_like(img, mmcv.imread('sky.jpeg'))) # resize by image

# rotate image
# mmcv.imshow(mmcv.imrotate(img, 90)) # rotate by angle
# mmcv.imshow(mmcv.imrotate(img, 50, scale=0.5)) # rotate by angle and scale it

# flip image
# mmcv.imshow(mmcv.imflip(img)) # flip horizontally
# mmcv.imshow(mmcv.imflip(img, direction='vertical')) # flip vertically

# crop image x1,y1,z2,y2 are upper left and lower right coordinates
bboxes = np.array([[100, 10, 500, 120], [0, 0, 50, 50]])
patches = mmcv.imcrop(img, bboxes)
for patch in patches:
    # mmcv.imshow(patch)
    pass

# Video
vid = mmcv.VideoReader('city.mp4')

print("length of video: ",len(vid))
print("fps of video: ",vid.fps)
print("resolution of video: ",vid.resolution)
print("width of video: ",vid.width,"height of video: ",vid.height)

# for frame in vid:
#     print("shape of frame: ",frame.shape)

img = vid.read() # read the next frame
# mmcv.imshow(img) 

img = vid[400] # read the frame at index 100
# mmcv.imshow(img)

img = vid[10:100] # read the frame at index 10 to 100
# for i in range(len(img)):
#     mmcv.imshow(img[i])

# vid.cvt2frames('out_dir') # convert video to frames and save it in out_dir
# mmcv.frames2video('out_dir', 'test.mp4') # convert frames to video

# mmcv.concat_video(['test.mp4', 'test.mp4'], 'joined.mp4', log_level='quiet')
    
# Optical flow

#flow = np.random.rand(800,600,2).astype(np.float32) # generate random optical flow
flow = mmcv.imread('demo.jpg')
mmcv.flowwrite(flow, 'demo_flow.flo') # save optical flow in .flo format
mmcv.flowwrite(flow, 'compressed.jpg', quantize=True, concat_axis=1) # save optical flow in .jpg format    
flow = mmcv.flowread('demo_flow.flo') # read optical flow in .flo format
flow = mmcv.flowread('compressed.jpg', quantize=True, concat_axis=1) # read optical flow in .jpg format

mmcv.flowshow(flow)
