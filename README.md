DESCRIPTION
------------------
Tool to automatically adjust rgb-values of an image-file. 


REQUIREMENTS
------------------

* Python 3.7
* Pygame 1.9.6


USAGE
-------------------
* Load your image file via the "Load Image" button.
* Enter the threshold r,b anf g values and the adjustment r,g and b values in the corresponding text fields.
* Hit "Start" and enter your dired output-filename.
* The program will adjust each pixel with r < Red threshold and g < Green threshold and b < Blue threshold by
increasing r by Red adjust, g by Green adjust and b by Blue adjust. 
* Resulting values > 255 will we set to 255, whilebresulting values < 0 will be set to 0.  
* The checkbox "Use Threshold greater than" reverses the thresholds (r > Red threshold and so on...).

LEGAL
--------------------
<a href=http://www.pygame.org>Pygame</a> is licensed under the <a href=http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>LGPLv2.1</a>.
