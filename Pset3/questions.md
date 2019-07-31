# Questions

## What's `stdint.h`?

A header file that specifies width integer types, with min and max allowed values. Contains the definition of new int types to specify width of them. for example int32_t will gaurentee the system environment will have 32 bits for this int type.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

These structs are used to tell the environment what byte/bit size to use for the corrosponding int type. For example uint16_t will have 2 bytes or 16 bits which is a unsigned short (0 to 65535). An unsigned char = uint8_t and uses 1 byte / 8 bits. ( ((2^8) - 1 = 256 - 1 = 255) 0 to 255, 256 = 0, 257 = 1, etc.) 

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1 byte = 8 bits, 1 word = 2 bytes = 16 bits, 1 dword (double word) = 4 bytes = 32 bits, 1 long = 8 bytes = 64 bits

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

In a BMP file the first two bytes identify the file is 0x42 0x4D in hexadecimal / BM in ASCII.
Possible entries in ASCII are BM (windows 3.1x,95,NT, etc), BA (bitmap arrar), CI (color icon), CP (color pointer), IC (icon), PT (pointer)

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the entire bmp file including headers, while biSize is the size of the bitmapinfoheader only, so its constant and = 40 bytes.

## What does it mean if `biHeight` is negative?

Negative biHeight means the bitmap is top down DIB and its origin is the upper left corner. BiCompression is either BI_RGB or BI_BITFIELDS, they cannot be compressed. 

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies bits per pixel.

## Why might `fopen` return `NULL` in `copy.c`?

fopen will return false if the 2nd argument, the file mode, is not ("r") readable. If read access is not granted.

## Why is the third argument to `fread` always `1` in our code?

The third argument is always 1 because it tells fread to read the file one time from the pointer. 

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

int padding = (4 - (3 * 3) % 4) % 4;
padding = 3;

## What does `fseek` do?

fseek is used to move the file position that the file ptr specifies, to a new location within the file. fssek(file_ptr, offset, position)

## What is `SEEK_CUR`?

seek_cu moves the file pointer position to given location.