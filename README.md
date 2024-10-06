# HDF5 File Explorer

## Overview

`h5reader.py` is a simple Python script designed for exploring and interacting with HDF5 files. It offers basic file navigation, dataset inspection, and visualization capabilities, either in a command-line or interactive mode. It supports several useful commands such as listing contents, changing directories, printing dataset data, checking dataset sizes, and plotting data.

## Features

- **Interactive Mode**: Allows users to explore an HDF5 file interactively with commands like `ls`, `cd`, `cat`, `size`, and `plot`.
- **Tab Completion**: Provides tab-completion for paths within the HDF5 file.
- **Dataset Visualization**: Supports plotting of 1D, 2D, and 3D datasets using `matplotlib`.
- **Command Line Options**: Supports various command-line options for non-interactive exploration.

## Installation

To use this script, ensure you have the following Python libraries installed:

```bash
pip install h5py matplotlib tqdm readline
```

or

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Mode

You can run the script directly from the command line with various options:

```bash
python h5reader.py <path_to_hdf5_file> [options]
```

or 

```bash
h5reader <path_to_hdf5_file> [options]
```

where `<path_to_hdf5_file>` is the path to the HDF5 file you want to explore.
This second command is available if you have installed the script by running `python setup.py install`.

**Options:**

- `-s`, `--size`: Print the size of each dataset.
- `-d`, `--data`: Print the data of each dataset.
- `-i`, `--interactive`: Start the interactive mode.

### Example Command-Line Usage

To print the size of all datasets in the file:

```bash
python h5reader.py myfile.h5 -s
```

To print the data of all datasets:

```bash
python h5reader.py myfile.h5 -d
```

### Interactive Mode

Interactive mode allows you to explore the HDF5 file structure using commands similar to a shell. To enter interactive mode, use:

```bash
python h5reader.py myfile.h5 -i
```

Once inside the interactive mode, you can use the following commands:

- `ls`: List the contents of the current directory.
- `cd <directory>`: Change to a specific directory.
- `cat <dataset>`: Print the data of the specified dataset.
- `size <dataset>`: Print the size of the specified dataset.
- `plot <dataset>`: Plot the data of the specified dataset. 1D, 2D, and 3D datasets are supported (2D datasets will be displayed as images, 3D datasets as animations).
- `tree`: Print the directory structure of the HDF5 file.
- `help`: Show a list of available commands.
- `exit`, `quit`, `q`: Exit the interactive mode.

**Exit Interactive Mode**: Use `exit`, `quit`, or `q` to leave the interactive mode.

### Example Interactive Usage

```bash
$ python h5reader.py myfile.h5 -i
/ % ls
/dataset1
/dataset2
/ % size dataset1
(100, 100)
/ % plot dataset1
```

## Known Issues & Limitations

- **3D Datasets**: When plotting 3D datasets, the script generates an animation (GIF-like) using `matplotlib`. It might take some time to generate the animation for large datasets.
- **Tab Completion**: The tab completion feature may not work on all terminals, especially on Windows.

## License

This script is licensed under the MIT License. Feel free to use, modify, and distribute it.
If you have any questions or suggestions, please feel free to contact me.
I would especially appreciate any feedback or contributions to improve this script!
Feel free to create an issue or submit a pull request on GitHub.

---

Enjoy exploring your HDF5 files with `h5reader.py`!