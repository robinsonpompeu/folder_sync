# Folder Sync

Folder Sync is a small project based on Python and developed to provide a solution for real-time monitoring and synchronization of local folders, ensuring that files and directories in a source folder are automatically mirrored to a destination folder, maintaining consistency between the two locations.

# Description

Folder Sync is a Python-based utility for real-time monitoring and synchronization of local directories. It ensures consistency between source and destination folders by automatically detecting and replicating file changes — including creations, modifications, and deletions — through a hash-based verification system.

At its core lies a custom-developed change detection module combined with hash verifications. It allows unidirectional synchronization, strictly mirroring source content to a target location. A standout feature is its integrated testing daemon, which simulates dynamic folder changes to validate synchronization behavior under controlled stress conditions, eliminating the need for manual testing. Every operation generates timestamped logs, providing detailed audit trails for both performance review and troubleshooting.

# Features

- **Real-time Monitoring**: Detects file changes (create, modify, delete) using hash digests.

- **Unidirectional Sync**: Supports one-way synchronization.

- **Logging**: Logs synchronization activities for auditing and debugging.

- **Simulation**: Includes a daemon to emulate folder changes to test synchronization in dynamic conditions.

# Prerequisites

The following requirements must be satisfied prior to a local installation and execution:

## System Requirements (Linux)

- Git (version control)
- Python 3.12 or higher.

# Installation and Usage

Follow this step-by-step guide for a local installation of the package.

## Linux

On a new terminal session run the following commands to clone the repository, where `proj_dir` is the installation path:

```console
user@ubuntu:~$ git clone https://github.com/robinsonpompeu/folder_sync proj_dir
user@ubuntu:~$ cd proj_dir
```

Then make the `setup.sh` script executable and run it:

```console
user@ubuntu:~/proj_dir$ chmod +x ./setup.sh
user@ubuntu:~/proj_dir$ ./setup.sh
```

During the setup one may choose to perform unit tests before starting the folder sync. When prompted type `y` (default answer) to perform such tests, or `n` to proceed with the project configuration.

```console
 3. Run unit tests [Y/n]:
```

In order to correctly configure the folder synchronization, the absolute paths of source and replica dir must be informed. Note that trailing slashes are required for both. The absolute path of log file must be informed as well:

```console
 4. Configuration

    Enter the absolute paths of

    Source dir (with trailing slash):
    
    Replica dir (with trailing slash):
    
    Log file: 
```

The last parameter of the configuration process requires the synchronization interval in seconds:

```console
    Enter the synchronization interval (in seconds):
```

As an optional feature, enable automated testing by the background daemon that simulate folder changes and test folders synchronization in real-time.

```console
 5. Run random folder modifications by a bot user [Y/n]:
```

# Removal

On a new terminal session change to the parent folder of `proj_dir` and run the following commands:

```console
user@ubuntu:~$ sudo rm proj_dir/ -r
```

This will remove the project folder and the virtual environment created to run the application.

# Future Improvements

## High Priority

- [ ] Write unit tests for dir_monitor module
- [ ] Conclude unit tests of vol_manager module
- [ ] Create changelog with commit messages
- [ ] Fix loggging bot removing big file directly after creating it

## Medium Priority
- [ ] Perform unit and integration tests on MacOS and Windows
- [ ] Implement remote directories synchronization 
- [ ] Extend synchronization mode with merging directories
- [ ] Create hash wrapper function for MD5 and other algorithms
- [ ] Add bidirectional synchronization
- [ ] Benchmark performance
- [ ] Use pandoc to generate README.md

## Low Priority
- [ ] Refactor argparse in main.py and usr_sim.py
- [ ] Manage trailing slashes in user inputs
- [ ] Create link to module documentation

# Change Log

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.1.0] - 2025-03-30
 
### Added

# Author

Robinson Pompeu 

[LinkedIn](https://www.linkedin.com/in/robinsonpompeu/) 

[GitHub](https://github.com/robinsonpompeu)