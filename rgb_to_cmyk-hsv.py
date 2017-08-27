def rgb_to_cmyk(r,g,b):

    cmyk_scale = 100

    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, cmyk_scale

    c = 1 - r / 255.
    m = 1 - g / 255.
    y = 1 - b / 255.

    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale, k*cmyk_scale

def rgb_to_hsv(r, g, b):

    r, g, b = r/255.0, g/255.0, b/255.0

    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn

    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx

    return h, s, v

if __name__ == "__main__":
    
    print('Entre com os valores de RGB:')
    r = eval(input('R:'))
    g = eval(input('G:'))
    b = eval(input('B:'))

    c, m, y, k = rgb_to_cmyk(r, g, b)
    h, s, v = rgb_to_hsv(r, g , b)

    print("RGB({0},{1},{2}) = CMYK({3:.2f},{4:.2f},{5:.2f},{6:.2f})".format(r,g,b,c,m,y,k))
    print("RGB({0},{1},{2}) = HSV({3:.2f}º,{4:.2f}%,{5:.2f}%)".format(r,g,b,h,s*100,v*100))