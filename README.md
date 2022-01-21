# TU Delft report

This repository contains a slightly altered version of the official TU Delft LaTeX template available on their website, which is down at the time of writing.

## Using the template

This template is designed to work with all versions of LaTeX, but if you want to adhere to the TU Delft house style, you need to use XeLaTeX, as it supports TrueType and OpenType fonts. The document can be compiled using the terminal with

  ```
  xelatex report
  bibtex report
  xelatex report
  xelatex report
  ```

This is equivalent to selecting 'XeLaTeX+BibTeX' or similar in your favorite TeX editing program.

A sample document, as well as documentation for template options, can be found in example.pdf. An example with the native LaTeX fonts, compiled using the 'nativefonts' option (or with pdflatex), can be found in example-nativefonts.pdf.

A separate example document is available which generates a cover image (front, back and spine). This document can be generated with

  ```
  xelatex cover
  xelatex cover
  ```

or simply with the 'XeLaTeX' option in TeXworks or an equivalent program.

## Installation on Windows

The TU Delft LaTeX template has been tested to work with the most recent version of MiKTeX at the time of this writing (2.9). The following packages are required on top of a basic MiKTeX installation to make full use of the template:

  > caption, fancyhdr, filehook, footmisc, fourier, l3kernel, l3packages, metalogo, mptopdf, ms, natbib, pgf, realscripts, tipa, titlesec, tocbibind, unicode-math, url, xcolor, xetex-def

Note that MiKTeX will generally automatically install these packages if they are missing from your installation.

## Installation on Linux (Debian/Ubuntu)

Recent versions of Debian, and derived distributions such as Ubuntu, use the TeX Live system. Install the following packages to make full use of the this template:

  ```
  sudo apt install texlive texlive-fonts-extra texlive-latex-extra texlive-xetex texlive-science-doc texlive-science texlive-lang-european
  ```

  You may also have to run

  ```
  sudo apt install texlive-lang-english
  ```

## Reusing the template

This repository can be used as a template for multiple reports. When set up correctly using git, any update to the template repository (this one) an be propagated to all other reports where it was used. In order to do so, follow these steps.

1. Create a new git repository for your report. You can add github's `.gitignore` template for the TeX language.

2. Clone your repository to your local system.

3. Include this repository as a submodule by calling 
  ```
  git submodule add link-to-this-repository
  ```

4. Copy `report.tex` from the template repository's subdirectory to use as the root file for your project. Similarly, you can copy `title.tex` and other example files if needed.

5. Create a symbolic link from the `.cls` and `.bst` files in the subdirectory to your project root folder. From the project root folder, run

  ```
  ln -s ./tudelft_report_template/tudelft-report.cls .
  ```

  6. Do the same for the `fonts` directory, and if needed, the `cover` directory.

  ```
  ln -s /path/to/repo/tudelft_report_template/fonts/ /path/to/repo/fonts
  ```

## Using Visual Studio Code

When using Visual Studio Code as your LaTeX editor, you can symlink the `.vscode` directory in the same way as explained in the previous section. The directory contains the recommended build order for this template using xelatex to be used in combination with the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension for Visual Studio Code. This overwrites LaTeX Workship's provided recipes and requires a reload of the window and the extension.