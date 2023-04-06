import time
import struct

import Quartz.CoreGraphics as CG
from color_check import match_color
from color_check import isEmptyColor
from board_generator import generate_board

class ScreenPixel(object):
    """Captures the screen using CoreGraphics, and provides access to
    the pixel values.
    """

    def capture(self, region = None):
        """region should be a CGRect, something like:

        >>> import Quartz.CoreGraphics as CG
        >>> region = CG.CGRectMake(0, 0, 100, 100)
        >>> sp = ScreenPixel()
        >>> sp.capture(region=region)

        The default region is CG.CGRectInfinite (captures the full screen)
        """

        if region is None:
            region = CG.CGRectInfinite
            print('Region is none. Fullscreen')
        else:
            # TODO: Odd widths cause the image to warp. This is likely
            # caused by offset calculation in ScreenPixel.pixel, and
            # could could modified to allow odd-widths
            if region.size.width % 2 > 0:
                emsg = "Capture region width should be even (was %s)" % (
                    region.size.width)
                raise ValueError(emsg)
        
        # Create screenshot as CGImage
        image = CG.CGWindowListCreateImage(
            region,
            CG.kCGWindowListOptionOnScreenOnly,
            CG.kCGNullWindowID,
            CG.kCGWindowImageDefault)

        # Intermediate step, get pixel data as CGDataProvider
        prov = CG.CGImageGetDataProvider(image)

        # Copy data out of CGDataProvider, becomes string of bytes
        self._data = CG.CGDataProviderCopyData(prov)

        # Get width/hei
        # ght of image
        self.width = CG.CGImageGetWidth(image)
        self.height = CG.CGImageGetHeight(image)

    def pixel(self, x, y):
        """Get pixel value at given (x,y) screen coordinates

        Must call capture first.
        """

        # Pixel data is unsigned char (8bit unsigned integer),
        # and there are for (blue,green,red,alpha)
        data_format = "BBBB"

        # Calculate offset, based on
        # http://www.markj.net/iphone-uiimage-pixel-color/
        offset = 4 * ((self.width*int(round(y))) + int(round(x)))

        # Unpack data from string into Python'y integers
        b, g, r, a = struct.unpack_from(data_format, self._data, offset=offset)

        # Return BGRA as RGBA
        return (r, g, b, a)

def return_color(mouse_pos):
    if mouse_pos == None:
        return "Not a Color"
    sp = ScreenPixel()
    x,y = mouse_pos
    x = int(x)
    y = int(y)
    while x%2 != 0:
        x -= 1
    while y%2 != 0:
        y -= 1
    
    rect = CG.CGRectMake(x - 50, y - 50, 200, 200)
    sp.capture(rect)

    for x in range(0,200,20):
        for y in range(0,200,20):
            color = match_color(sp.pixel(x,y))
            if color != "Not a Color":
                return color
    return "Not a Color"

def clean_number(num):
    num = int(num)
    while num%2 != 0:
        num -= 1
    return num

def grab_board_from_screen(top_left, bottom_right):
    if top_left == None:
        return ("no board")
    left_bound, top_bound = top_left #bounds should be defined by the middle of the first/last square
    right_bound, bottom_bound = bottom_right #thus, distance btwn first/last square should be 9 hor, 19 vert
    
    #test lines
    left_bound = clean_number(left_bound)
    right_bound = clean_number(right_bound)
    #top_bound = clean_number(top_bound)
    #bottom_bound = clean_number(bottom_bound)
    #end test lines

    hor_increment = (right_bound-left_bound)/9
    vert_increment = (bottom_bound-top_bound)/19
    board = generate_board()

    if top_left == None:
        return False
    sp = ScreenPixel()
    
    hor_size = right_bound-left_bound
    hor_size = clean_number(hor_size)
    vert_size = bottom_bound-top_bound
    vert_size = clean_number(vert_size)

    rect = CG.CGRectMake(left_bound, top_bound, hor_size*2, vert_size*2)
    sp.capture(rect)

    for x in range(10):
        for y in range(22):
            if y > 19:
                board[x][y] = 0
            else:
                test_x,test_y = [hor_increment*x,vert_size-(vert_increment*y)]
                test_x *= 2
                test_y *= 2
                test_x = clean_number(test_x)
                test_y = clean_number(test_y)

                if isEmptyColor(sp.pixel(test_x,test_y)):
                    board[x][y] = 0
                else:
                    board[x][y] = 1
    return board

    #isEmptyValue = isEmptyColor(sp.pixel(0,0)) useless?
    #return isEmptyValue useless?

if __name__ == '__main__' and False:

    # Timer helper-function
    import contextlib

    @contextlib.contextmanager
    def timer(msg):
        start = time.time()
        yield
        end = time.time()
        print ("%s: %.02fms" % (msg, (end-start)*1000))


    # Example usage
    sp = ScreenPixel()

    with timer("Capture"):
        # Take screenshot (takes about 70ms for me)
        sp.capture(CG.CGRectMake(0, 0, 100, 100))

    with timer("Query"):
        # Get pixel value (takes about 0.01ms)
        print (sp.width, sp.height)
        print (sp.pixel(0, 0))


    # To verify screen-cap code is correct, save all pixels to PNG,
    # using http://the.taoofmac.com/space/projects/PNGCanvas

    from pngcanvas import PNGCanvas
    c = PNGCanvas(sp.width, sp.height)
    for x in range(sp.width):
        for y in range(sp.height):
            c.point(x, y, color = sp.pixel(x, y))

    with open("test.png", "wb") as f:
        f.write(c.dump())

if __name__ == "__main__":
    import pynput
    mouse = pynput.mouse.Controller()
    import time
    print("first spot")
    time.sleep(1)
    loc1 = mouse.position
    print("second spot")
    time.sleep(3)
    loc2 = mouse.position

    for x in range(0,20):
        alt = x / 2

        start = time.time()
        board = grab_board_from_screen([loc1[0]+alt,loc1[1]+alt],[loc2[0]+alt,loc2[1]+alt])
        #color = return_color((0,0))
        #print(time.time()-start)
        from print_board_module import print_board
        time.sleep(0.5)
        print_board(board)
