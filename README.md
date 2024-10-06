# HDF5/H5 File Explorer

## Overview

`h5reader` is a Python tool designed to explore and interact with **HDF5 (.hdf5)** and **H5 (.h5)** files. It provides both command-line and interactive modes, allowing you to navigate the file structure, inspect datasets, and visualize data. The interactive mode offers Unix shell-like commands for intuitive file exploration.

## Features

- **Interactive Shell**: Navigate HDF5/H5 files using commands like `ls`, `cd`, `cat`, `size`, and `plot`.
- **Tab Completion**: Autocomplete paths within HDF5/H5 files for easier navigation.
- **Data Visualization**: Plot 1D, 2D, and 3D datasets using `matplotlib`.
- **Command-Line Options**: Perform non-interactive exploration with a variety of command-line options.
- **Tree View**: Display the entire structure of the HDF5/H5 file.
- **Cross-Platform Compatibility**: Works on Unix-like systems. **Note**: Windows compatibility has **not been tested**, and the script may not work at all on Windows.

## Installation

### Prerequisites

Ensure you have **Python 3.7** or higher installed.

### Installing via `requirements.txt`

You can install all the necessary packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install the following dependencies:
- `h5py`
- `matplotlib`
- `tqdm`
- `readline` (for Unix-like systems)
- `pyreadline3` (for Windows systems, though Windows support has not been tested)

### Installing `h5reader`

You can install `h5reader` as a command-line tool using the `setup.py` script:

```bash
python setup.py install
```

This will make the `h5reader` command available globally, allowing you to run it directly from any terminal.

## Usage

### Command-Line Mode

Run `h5reader` directly from the command line with various options:

```bash
h5reader <path_to_hdf5_or_h5_file> [options]
```

**Options:**

- `-t`, `--tree`: Display the entire structure of the HDF5/H5 file.
- `-s`, `--size`: Print the shape of each dataset.
- `-d`, `--data`: Print the data of each dataset.
- `-i`, `--interactive`: Start the interactive mode.
- `-v`, `--verbose`: Increase output verbosity.

#### Example Commands

To display the structure of an HDF5 or H5 file:

```bash
h5reader myfile.h5 -t
```

To print the sizes of all datasets:

```bash
h5reader myfile.hdf5 -s
```

To print the data of all datasets:

```bash
h5reader myfile.h5 -d
```

### Interactive Mode

Launch the interactive shell to explore the file:

```bash
h5reader myfile.h5 -i
```

#### Available Commands

- `ls`: List the contents of the current directory.
- `cd <directory>`: Change directory.
- `cat <dataset>`: Print the data of a dataset.
- `size <dataset>`: Print the shape of a dataset.
- `plot <dataset>`: Plot the data of a dataset (supports 1D, 2D, and 3D).
- `tree`: Display the directory structure.
- `help`: Show a list of available commands.
- `exit`, `quit`, `q`: Exit interactive mode.

**Tab Completion**: Use the `Tab` key to autocomplete paths in the HDF5/H5 file.

#### Example Interactive Session

```bash
$ h5reader myfile.h5 -i
/ % ls
/dataset1
/group1
/ % cd group1
/group1 % ls
/dataset2
/group1 % size dataset2
(100, 200)
/group1 % plot dataset2
```

### Using `setup.py`

The `setup.py` script simplifies the installation of `h5reader` as a command-line tool. It handles dependency management and creates a console entry point for easy usage.

#### Setup Instructions

1. Clone the repository or download the files.
2. Run the following command to install `h5reader`:

   ```bash
   python setup.py install
   ```

After installation, you can use the `h5reader` command directly from your terminal.

## Known Issues & Limitations

- **Windows Compatibility**: The script has **not been tested on Windows**, and it may not work at all on Windows systems.
- **3D Dataset Visualization**: Large datasets may slow down the generation of animations.
- **Tab Completion on Windows**: May not work on all terminals; installing `pyreadline3` may help, but it is untested.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on GitHub.

## Contact

For questions or suggestions, reach out to the author.

---

Enjoy exploring your HDF5/H5 files with `h5reader`!