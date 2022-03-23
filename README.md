# Python-Remove-Watermark
A simple program to remove the watermark from a PDF file. 


### How?

1. convert the PDF file into images using `pdf2image`
2. convert the images to numpy array
3. find the specific pixel by watermarks' rgb values and change them into (255,255,255)
4. save the modified images


### Environment

First you need to install the dependencies:
```
$ pip install pdf2image
```
```
$ pip install scikit-image
```

Inside the repository create a directory that will receive the modified images:
```
$ mkdir jiangyi3
```
To execute:
```
$ python watermark.py
```
Don't forget to indicate the pdf's path you want to convert.


### Results
![image](./result.png)