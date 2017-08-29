import os, numpy, PIL
from PIL import Image

def ex1():
    # Access all h*.JPG
    allfiles=os.listdir(os.getcwd())
    imlist=[filename for filename in allfiles if filename in ['h1.JPG', 'h2.JPG', 'h3.JPG', 'h4.JPG'] ]

    # Assuming all images are the same size, get dimensions of first image
    w,h=Image.open(imlist[0]).size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr=numpy.zeros((h,w,3),numpy.float)

    # Build up average pixel intensities, casting each image as an array of floats
    for im in imlist:
        imarr=numpy.array(Image.open(im),dtype=numpy.float)
        arr=arr+imarr/N

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode='RGB')
    out.save('exercise1.PNG')
    out.show()

def ex2():
    # Access all dog*.jpg files
    allfiles = os.listdir(os.getcwd())
    imlist = [filename for filename in allfiles if  filename in ['dog1.jpg','dog2.jpg']]

    # Assuming all images are the same size, get dimensions of first image
    w,h=Image.open(imlist[0]).size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    # arr=numpy.zeros((h,w,3),numpy.float)
    imarr = []
    # Build up average pixel intensities, casting each image as an array of floats
    for im in imlist:
        imarr.append(numpy.array(Image.open(im),dtype=numpy.float))

    arr = (imarr[1] - imarr[0] + 255)/2

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode='RGB')
    out.save('exercise2.PNG')
    out.show()

if __name__ == '__main__':
    print('All images must be in this file folder')
    # Generates HDR image
    o = int(input('1- Run 1st exercise\n2- Run 2nd exercise\nOption: '))
    if o == 1:
        ex1()
    elif o == 2:
        ex2()