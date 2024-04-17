<div align="center">
<!-- 标题 -->

<h1 align="center">
  - RPGMVP2PNG - 
</h1>

<!-- star数, fork数, pulls数, issues数, contributors数, 开源协议 -->
<a href="https://github.com/DrRyanHuang/rpgmvp2png/stargazers"><img src="https://img.shields.io/github/stars/DrRyanHuang/rpgmvp2png" alt="Stars Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/network/members"><img src="https://img.shields.io/github/forks/DrRyanHuang/rpgmvp2png" alt="Forks Badge"/></a>
<br/>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/pulls"><img src="https://img.shields.io/github/issues-pr/DrRyanHuang/rpgmvp2png" alt="Pull Requests Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/issues"><img src="https://img.shields.io/github/issues/DrRyanHuang/rpgmvp2png" alt="Issues Badge"/></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/DrRyanHuang/rpgmvp2png?color=2b9348"></a>
<a href="https://github.com/DrRyanHuang/rpgmvp2png/blob/master/LICENSE"><img src="https://img.shields.io/github/license/DrRyanHuang/rpgmvp2png?color=2b9348" alt="License Badge"/></a>





<!-- logo -->
<img alt="Xiao" src="CutIn_Furea.png" width="50%"> </img>
<br/>
<i>Loved the project? Please consider forking the project to help it improve!</i>

</div>


This README provides an introduction to the Python script and HTML file for decrypting RPG Maker MV files.

The rpgmvp2png.py script is a tool for decrypting RPG Maker MV's .rpgmvp files to .png files.

To decrypt a single file, use the following command:


```
python rpgmvp2png.py examples/Fire1.rpgmvp out.png
```
This command will decrypt the examples/Fire1.rpgmvp file and save it as out.png.

To decrypt an entire directory, use the following command:

```
python rpgmvp2png.py examples
```

This command will decrypt all .rpgmvp files in the examples directory and create a directory with the same structure as the original directory in the current directory.


The rpgmvp2png.html file is a web-based tool for decrypting .rpgmvp files.


Usage

- Choose whether to download the decrypted images as a package.
- Select one or more .rpgmvp files on the webpage.
- If the package download option is selected, a zip file containing all decrypted images will be automatically downloaded once the decryption is complete.
- If the package download option is not selected, the decrypted images will be displayed on the webpage, and each image can be saved individually.

Notes

- Ensure that the uploaded files are RPG Maker MV's .rpgmvp files. Other file formats may not be decrypted correctly.
- Decrypting a large number of files or large files may take some time. Please be patient.
- The decrypted images are temporarily stored in the browser. Closing the webpage or clearing the browser cache may result in the loss of images. Please save the required images promptly.


If you have any questions or suggestions, please don't hesitate to open an issue on the GitHub repository. Your feedback is greatly appreciated!