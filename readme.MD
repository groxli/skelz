# skelz
![Image of Skelz Icond](http://groxli.com/wp-content/uploads/2018/01/skelz_icon.png)

image source: https://downloadicons.net/

Utility for generating skeleton Python code of commonly used functions.

[![Skelz demo screencast](https://i.vimeocdn.com/video/705255959.webp?mw=1100&mh=585)](https://vimeo.com/273455312 "Simple Skelz Demo - Click to Watch")

## Getting Started

After the project has been installed as described below, the easiest way to use the file is to change directories into the cloned directory and run:

```
python skelz.py
```

You will be prompted for the file directory to output the skeleton code, readme.MD and (if applicable) and stub configuration file.

### Prerequisites

This code does not require any special or exotic Python packages.

### Installing

1) Clone the project to a path where you keep your github projects. For example:

```
cd ~/git_projects/
git clone https://github.com/groxli/skelz.git
```

For convenience, you can add a command alias to your .bash_profile (or similar) file. Assuming the project path is as listed above, add the following in .bashrc:

```
alias skelz="~/git_projects/skelz/skelz.py"
```

Don't forget to re-source your bash file:

```
source ~/.bash_profile
```

## Authors

* **Nate Jensen** - *Initial work* - [groxli](https://github.com/groxli)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details