# stegobliterate
Tool for destroying steganographic data from the spatial domain of png images.

When run, the script flips one of the least significant bits of every pixel according to the bits and weights hardcoded into `BIT_CHOICES`, then writes the modified image to the output filename. Although not fullproof, this should destroy any spatial domain steganography in the file, while not perceptibly changing the original image.

## Usage

```
python3 stegobliterate.py <original filename> <output filename>
```
