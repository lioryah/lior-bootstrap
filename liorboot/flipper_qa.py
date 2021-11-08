import fire
import numpy as np
from flipper import flip_img
import cv2 
import tensorflow as tf



def mse_img(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err


# make image illuimation darker or lighter 
def adjust_gamma(image, gamma=1.0):
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)


def validate_flipper(source, dest): #source is the reference
    flipped_img = flip_img(source, " ")
    
    try:
        mse = mse_img(flipped_img, dest)
    except:
        print("the source image dimensions are: " + source.shape())
        print("the dest image dimensions are: " + dest.shape())
        print("error. check if both images has same dimensions")
    
    print(f"mse is {mse}")

    ssim1 = tf.image.ssim(flipped_img, dest, max_val=255, filter_size=11,
                          filter_sigma=1.5, k1=0.01, k2=0.03)
    print(f"ssim is: {ssim1}")    

    if(ssim1 > 0.8):  
        return True
    else:
        return False


def validate_with_text(source, dest):
     # search for more images comparing methods
    
    return 1

def main_(): 
    src_path = "/mnt/c/Users/liory/_wd/repos/lior-bootstrap/Backchannel-Lena-Soderberg-FA.jpg"
    source = cv2.imread(src_path)

    cv2.imshow("source img", source)
    cv2.waitKey(1)   
    
    # test 1 change lumintion to image
    dest = flip_img(source, " ")
    dest = adjust_gamma(source, gamma=1.0)
    
    cv2.imshow("dest img", dest)
    cv2.waitKey(1)

    '''
    cv2.imshow("source img", source)
    cv2.waitKey(0)
    cv2.imshow("flipped img", dest)
    cv2.waitKey(0)
    '''
    print(validate_flipper(source, dest))
   # fire.Fire(validate_flipper)
    
    print(1)


if __name__ == '__main__':
    main_()