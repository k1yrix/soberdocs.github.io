# Tested Linux Distros + Versions

## Debian
| Tested version | Test date | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | ------------------------------ | --------- | ----- | ----- |
| 11             | 10/18/24  |                                | Yes       | No    | Able to pass GPG verification and installs, but does not launch without logs, even with OpenGL invoked |
| 12             | 10/18/24  |                                | Yes       | Yes   |       |

## Ubuntu
| Tested version | Test date | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | ------------------------------ | --------- | ----- | ----- |
| 20.04 LTS      | 10/18/24  |                                | Yes       | No    | Mesa too old to attach to X11, libEGL too old to know if screen is DRI3 capable; despite able to run barebones, unable to install (and therefore run) Roblox under these conditions |
| 22.04 LTS      | 10/18/24  |                                | Yes       | Yes   |       |

## Fedora Linux
| Tested version | Test date | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | ------------------------------ | --------- | ----- | ----- |
| 39             | 10/18/24  | VMware Workstation 17.6.1      | Yes       | Yes   | EOL Version      |
| 40             | 10/18/24  | Physical machine               | Yes       | Yes   |       |
| 41             | 11/01/24  | Phyiscal machine               | Yes       | Yes   |       |