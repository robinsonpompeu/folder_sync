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