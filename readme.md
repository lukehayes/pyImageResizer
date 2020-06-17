## PyImageResizer
A simple Python script that will resize images to a given width and height

### Dependencies
* Python3
* Pip Package Manager
* [Python Pillow Library](https://pillow.readthedocs.io/en/latest/)

### Options
There are options for setting the location directory of the images to be resized, the output directory the resized images
will be placed and the desired width to resize the image with:

###### Image directory
``` 
--imageDir 'myImageDir'

or

-i 'myImageDir'
``` 

###### Output directory
``` 
--outputdir 'myTestOutputDir'

or

-o 'myTestOutputDir'
``` 

###### Image width
``` 
--width 1000

or

-w 1000
``` 

### Example
Clone the project, cd into the folder and then run:
````
./py-resizer -i myImagesDir -o myOutputDir -w 1000
````
In this example -w sets the width and the height is calculated from that.

