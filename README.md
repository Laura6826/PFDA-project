# Programming for Data Analytics 24-25: 4369

## This project was submitted as part of the module Programming for Data Analytics 24-25: 4369., Higher Diploma in Science, Data Analytics

## *Author: Laura Lyons*

***

This README file was written using the [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) as a guidance document
***

  &#x26a0;&#xfe0f; **DISCLAIMER**

  Microsoft Co-Pilot was used to generate ideas of the content of the following notebook. That said, the notebook is mainly my own work, as I had to re-work the code the text in generated to meet my own needs.(*The warning icon was sourced from [Stackoverflow](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)*)

## **Table of contents**

1. [Introduction.](#1-introduction).
1. [The purpose of this project.](#2-the-purpose-of-this-project)
1. [How to get started.](#3-how-to-get-started)
1. [How to get help.](#4-how-to-get-help)
Updated 1. [How to contribute.](#5-how-to-contribute)

## 1. Introduction

This project was created to fufill an assessment requirement of Programming for Data Analytics 24-25: 4369, as part of the H.Dip in Science in Data Analytics.

The aim of this project is to demonstrate an ability to perform data analysis on some data, using a number of skills learned in the previous lectures, associated with the module.

***

## 2. The purpose of this project

As noted on the [assignment instructions](https://vlegalwaymayo.atu.ie/course/view.php?id=10462#section-3),

The purpose of the module is to ensure students can demonstrate the following:

1. Programmatically create plots and other visual outputs from data.
1. Design computer algorithms to solve numerical problems.
1. Create software that incorporates and utilises standard numerical libraries.
1. Employ appropriate data structures when programming for data-intensive applications.

## 3. How to get started

### Necessary software

In order to run the included files, you will need to ensure that you have access to the correct softwear. I would recommend downloading the following applications (ensuring sufficent space on your hard drive prior to installation):

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) (if Anaconda is too large, miniconda would also suffice).
2. [Visual Studio Code](https://code.visualstudio.com/Download) (this is a code editor).

### **Additions to** *.gitignore*

A number of [additional files](https://github.com/github/gitignore/tree/main/Global) were added to my .gitignore prior to running the programmes:

  1. python.gitignore
  2. macOS..gitignore
  3. VisualStudioCode.gitignore
  4. Linux.gitignore
  5. TeX.gitignore
  6. Vim.gitignore
  7. Windows.gitignore

## How to run the Notebook

### Using Using Visual Studio Code & Anaconda

**Clone the Repository**:

```ruby
   git clone https://github.com/Laura6826/PFDA-project
```

**Install the required packages**:

For a seamless excutition, I would also recommend you have access to the below libraries prior to running the files. The libraries required to run this file (as noted below), can be installed with the following code:

```ruby
pip install -r requirements.txt
```

,or you can manually install each of the libraries below.+

```ruby
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import datetime as dt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import scipy.stats as stats
from scipy.stats import zscore
from scipy.stats import shapiro
from scipy.stats import boxcox
from sklearn.preprocessing import PowerTransformer
from windrose import WindroseAxes
```

***

### Open the notebook in Visual Studio Code

- Open Visual Studio Code.
- Open the `PFDA-project` folder.
- Open the `wind_project.ipynb` file.

## 4. How to get help

I have attached below,a number of helpful links, should you wish to extrapolate on any of the methods used within this project.

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf)
1. [Visual Studio Code](https://code.visualstudio.com/Download)
1. [w3schools](https://www.w3schools.com/)
1. [Pandas](https://pandas.pydata.org/)
1. [Numpy](https://numpy.org/)
1. [Matplotlib.py](https://matplotlib.org/)
1. [Seaborn](https://seaborn.pydata.org/)

Additionally, a number of links are embedded within the code, in areas that i found confussing/difficult, that should help should there be any difficulty.

## 5. How to contribute

As this project was created to fufill an assessment requirement of the Principles of Data Analytics, as part of the H.Dip in Science in Data Analytics, no contributions will be allowed, in order to comply with ATU Policy on [Plagiarism](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) and the [Student Code of Conduct](https://www.atu.ie/sites/default/files/2022-08/Student%20Code_Final_August_2022.pdf).

Should you find any errors or have any recommendations , please submit a pull request on Github. or just wish to contact that author, you can do so at <maxwell6826@gmail.com>.

***
