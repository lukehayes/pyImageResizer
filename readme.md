## PyImageResizer
A simple Python script that will resize images to a given width and height

### Dependencies
[Python Pillow Library](https://pillow.readthedocs.io/en/latest/)

### Options
There are options for setting the location directory of the images to be resized, the output directory the resized images
will be placed and the desired width to resize the image with:
``` 
--outputdir / -o
-o 'myTestOutputDir'
``` 

``` 
--imageDir / -i
-i 'myImageDir'
``` 

``` 
--width / -w
-w 1000
``` 

### Example
````
./py-resizer -i myImagesDir -o myOutputDir -w 1000
````

