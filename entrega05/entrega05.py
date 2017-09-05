import os, numpy, PIL
from PIL import Image

def ex1():
    # Access all png and jpg images
    allfiles = os.listdir(os.getcwd())
    imlist = [filename for filename in allfiles if filename[-4:] in ['.JPG', '.jpg', '.png', '.PNG'] ]
    
    # Choose to use first image
    image = imlist[0]
    
    # Assuming all images are the same size, get dimensions of first image
    c, r = Image.open(image).size

    # Create a numpy array of floats to store the average (assume RGB images)
    arr = numpy.zeros((r,c,3),numpy.float)

    o = int(input('1. Mirror x-axis\n2. Mirror y-axis\n3. Mirror both axis\nOption:'))

    imarr = numpy.array(Image.open(image),dtype=numpy.float)
    for i in range(r):
        for j in range(c):
            new_x = i
            new_y = j
            if o == 1:
                new_x = r-i-1
                new_y = j
            elif o == 2:
                new_x = i
                new_y = c-j-1
            elif o == 3:
                new_x = r-i-1
                new_y = c-j-1
            for k in range(3):
                arr[new_x][new_y][k] = imarr[i][j][k]

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode='RGB')
    out.save('exercise1.png')
    out.show()

def ex2():
    
    scale = int(input('Scale increasement value:\nOnly 2 working ok'))

    # Access all png and jpg images
    allfiles = os.listdir(os.getcwd())
    imlist = [filename for filename in allfiles if filename[-4:] in ['.JPG', '.jpg', '.png', '.PNG'] ]
    
    # Choose to use first image
    image = imlist[0]
    
    # Assuming all images are the same size, get dimensions of first image
    c, r = Image.open(image).size

    # Create a numpy array of floats to store the average (assume RGB images)
    arr = numpy.zeros((r*scale,c*scale,3),numpy.float)

    imarr = numpy.array(Image.open(image),dtype=numpy.float)
    o = input('Use replication (takes a little more time)? y/n:')
    for i in range(r):
        for j in range(c):
            new_x = i*scale
            new_y = j*scale
            for k in range(3):
                if o == 'n':
                    arr[new_x][new_y][k] = imarr[i][j][k]
                elif o == 'y':
                    for s in range(scale):
                        for t in range(scale):
                            arr[new_x+s][new_y+t][k] = imarr[i][j][k]
                else:
                    print('Invalid response.')

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode='RGB')
    out.save('exercise2.png')
    out.show()

if __name__ == '__main__':
    print('The program will choose one of the images from this file folder')
    
    o = int(input('1- Mirror image\n2- Increase image scale\nOption: '))
    if o == 1:
        ex1()
    elif o == 2:
        ex2()