# Color Correction using root-polynomial regression

This repo performs color correction and texture analysis using [Colour](https://www.colour-science.org/) library. The color correction also uses opencv to automatically find color correction charts embedded in images.

To run the examples the easiest thing to do is to start with a clean virtual environment. After you clone the repo, create the virtual environment and install the requirements.

```bash
python3 -m venv new-venv
source new-venv/bin/activate
pip install -r requirements.txt
```
then start jupyter and you should be able to run the code in `correction.ipynb`.
```bash
jupyter notebook
```

# Purpose of files

Spydercheckr24.py - description of "Spydercheckr24" colour checker.
correction.ipynb - Jupyter notebook for correction photos in JPG_uncorrected using root-polynomial regression (Finlayson 2015).

# References

https://ieeexplore.ieee.org/document/7047834