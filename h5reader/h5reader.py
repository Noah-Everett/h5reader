import h5py
import argparse
import os
import readline
import rlcompleter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm

# A simple completer for paths in the HDF5 file
class HDF5PathCompleter:
    def __init__(self, f, current_path='/'):
        self.f = f
        self.current_path = current_path

    def complete(self, text, state):
        # Normalize the path to be relative to the current directory
        if not text.startswith('/'):
            path = os.path.normpath(os.path.join(self.current_path, text))
        else:
            path = text

        # Try to complete directories or datasets
        try:
            dirname, partial_key = os.path.split(path)
            if dirname == '':
                dirname = '/'
            group = self.f[dirname]

            # Find matches in the group for partial keys
            matches = [key for key in group.keys() if key.startswith(partial_key)]
            matches.sort()

            if state < len(matches):
                completion = matches[state]
                return completion
            else:
                return None
        except KeyError:
            return None

# ls command to list the contents of a directory
def ls(f, path):
    try:
        for key in f[path].keys():
            print(f[path][key].name)
    except KeyError:
        print(f"No such directory: {path}")

# cd command to change directories
def cd(f, current_path, new_path):
    # Normalize the path with os.path.join and handle relative paths
    if new_path == '.':
        return current_path
    elif new_path == '..':
        # Move up one directory, but ensure we don't leave the root '/'
        if current_path != '/':
            return os.path.dirname(current_path.rstrip('/')) or '/'
        return current_path
    else:
        combined_path = os.path.normpath(os.path.join(current_path, new_path))
        # Check if the new path is a directory
        if combined_path in f:
            if isinstance(f[combined_path], h5py.Group):
                return combined_path
            else:
                print(f"{combined_path} is not a directory")
                return current_path
        else:
            print(f"No such directory: {new_path}")
            return current_path

# cat command to print the data of a dataset
def cat(f, path):
    try:
        print(f[path][:])
    except KeyError:
        print(f"No such dataset: {path}")
    except Exception as e:
        print(e)

# size command to print the size of a dataset
def size(f, path):
    try:
        print(f[path].shape)
    except KeyError:
        print(f"No such dataset: {path}")
    except Exception as e:
        print(e)

# plot command to plot the data of a dataset
def plot(f, path):
    try:
        s = f[path].shape
        if len(s) == 1:
            plt.plot(f[path][:])
        elif len(s) == 2:
            plt.imshow(f[path][:])
        elif len(s) == 3:
            # make a gif
            fig = plt.figure()
            ims = []
            for i in tqdm(range(s[0]), ncols=100):
                im = plt.imshow(f[path][i])
                ims.append([im])
            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
        plt.show()
    except KeyError:
        print(f"No such dataset: {path}")

# prints the complete layout of the hdf5 file
def tree(f, path='/', indent='', last=True, printOpt=None):
    try:
        keys = list(f[path].keys())
        for i, key in enumerate(keys):
            is_last = (i == len(keys) - 1)
            if is_last:
                connector = '└── '
            else:
                connector = '├── '

            if printOpt and printOpt is not cat:
                print(indent + connector + key, end=' ')
            else:
                print(indent + connector + key)

            if isinstance(f[path][key], h5py.Group):
                new_indent = indent + ('    ' if is_last else '│   ')
                tree(f, f[path][key].name, new_indent, is_last, printOpt)
            elif printOpt:
                printOpt(f, f[path][key].name)
    except KeyError:
        print(f"No such directory: {path}")

# Help function to display available commands
def help():
    print('Use `exit`, `quit`, or `q` to quit the interactive mode')
    print('Use `ls` to list the contents of the current directory')
    print('Use `cd <directory>` to change directories')
    print('Use `cat <dataset>` to print the data of a dataset')
    print('Use `size <dataset>` to print the size of a dataset')
    print('Use `plot <dataset>` to plot the data of a dataset')
    print('Use `tree` to print the complete layout of the HDF5 file')
    print('Use `help` to print this message again')
    print('Press tab to autocomplete paths')

# Interactive loop for the user to explore the HDF5 file
def interactiveLoop(f, verbose=False):
    path = '/'
    completer = HDF5PathCompleter(f, path)

    # Activate tab completion
    readline.set_completer(completer.complete)
    readline.parse_and_bind("tab: complete")

    if verbose:
        help()

    while True:
        try:
            command = input(f'{path} % ').strip().split()
            if not command:
                continue

            cmd = command[0]
            if cmd in ['exit', 'quit', 'q']:
                break
            elif cmd == 'ls':
                ls(f, path)
            elif cmd == 'cd':
                if len(command) > 1:
                    path = cd(f, path, command[1])
                    completer.current_path = path  # Update completer's path
                else:
                    print("Usage: cd <directory>")
            elif cmd == 'cat':
                if len(command) > 1:
                    cat(f, os.path.normpath(os.path.join(path, command[1])))
                else:
                    print("Usage: cat <dataset>")
            elif cmd == 'size':
                if len(command) > 1:
                    size(f, os.path.normpath(os.path.join(path, command[1])))
                else:
                    print("Usage: size <dataset>")
            elif cmd == 'plot':
                if len(command) > 1:
                    plot(f, os.path.normpath(os.path.join(path, command[1])))
                else:
                    print("Usage: plot <dataset>")
            elif cmd == 'tree':
                tree(f, path)
            elif cmd == 'help':
                help()
            else:
                print(f"Unknown command: {cmd}")
        except Exception as e:
            print(e)

def main():
    parser = argparse.ArgumentParser(description='HDF5 File Explorer')
    parser.add_argument('path', type=str, help='Path to the HDF5 file')
    parser.add_argument('-t', '--tree', help='Print the complete layout of the HDF5 file', action='store_true')
    parser.add_argument('-s', '--size', help='Print the size of each dataset', action='store_true')
    parser.add_argument('-d', '--data', help='Print the data of each dataset', action='store_true')
    parser.add_argument('-i', '--interactive', help='Interactive mode', action='store_true')
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    args = parser.parse_args()

    path = args.path

    with h5py.File(path, 'r') as f:
        if args.tree or args.size or args.data or not args.interactive:
            if args.size:
                tree(f, printOpt=size)
            elif args.data:
                tree(f, printOpt=cat)
            else:
                tree(f)

        if (args.tree or args.size or args.data) and args.interactive:
            print('\nEntering interactive mode...')
        
        if args.interactive:
            interactiveLoop(f, args.verbose)

if __name__ == '__main__':
    main()