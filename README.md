# Color Correction using root-polynomial regression

This repo performs color correction using hyperspectral photos to generate photos in camera color space and photos in XYZ color space. The color correction is performed using the root polynomial expension of image in camera color space. Target values is image in XYZ color space. 

Also in the process of execution hyperspectral photographs converted into photos in the space of a standard observer are saved to a folder /gen_img/. For example, /gen_img/xyz-2019-08-27_046-h5.jpeg


To run this repo you can use:

```bash
git clone https://github.com/yavnolib/root_polynomial_color_correction.git
jupyter notebook iitp-cc-notebook.ipynb
```


# References

Hyperspectral photographs are taken from the KAUST dataset https://repository.kaust.edu.sa/handle/10754/670368

RPCC algorithm (Finlayson 2015): https://ieeexplore.ieee.org/document/7047834
