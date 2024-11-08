# Tested Linux Distros + Versions

## Point release distros
### Debian
| Tested version | Test date | Test authored by                              | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | --------------------------------------------- | ------------------------------ | --------- | ----- | ----- |
| 11             | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | VMware Workstation 17.6.1      | Yes       | No    | Able to pass GPG verification and installs, but does not launch without logs, even with OpenGL invoked |
| 12             | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | VMware Workstation 17.6.1      | Yes       | Yes   |       |

### Ubuntu
> Ubuntu has multiple flavours based on the base desktop environment installed out of the box. Reguardless, they are to be treated as one.

| Tested version | Test date | Test authored by                              | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | --------------------------------------------- | ------------------------------ | --------- | ----- | ----- |
| 20.04 LTS      | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | VMware Workstation 17.6.1      | Yes       | No    | Mesa too old to attach to X11, libEGL too old to know if screen is DRI3 capable; despite able to run barebones, unable to install (and therefore run) Roblox under these conditions |
| 22.04 LTS      | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | VMware Workstation 17.6.1      | Yes       | Yes   |       |

### Fedora Linux
> Like Ubuntu, Fedora has other versions based on the base desktop environment installed out of the box. Likewise, they are to be treated as one reguardless.

| Tested version | Test date | Test authored by                              | Test method                    | Installs? | Runs? | Notes |
| -------------- | --------- | --------------------------------------------- | ------------------------------ | --------- | ----- | ----- |
| 39             | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | VMware Workstation 17.6.1      | Yes       | Yes   | EOL version |
| 40             | 10/18/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | Phyiscal machine               | Yes       | Yes   |       |
| 41             | 11/01/24  | [kirbix (k1yrix)](https://github.com/k1yrix)  | Phyiscal machine               | Yes       | Yes   |       |

### openSUSE (Leap)
| Tested version | Test date | Test authored by                              | Method of testing      | Installs? | Runs? | Notes |
| -------------- | --------- | --------------------------------------------- | ---------------------- | --------- | ----- | ----- |
| TBA            | TBA       |                                               |                        | TBA       | TBA   |       |

## Rolling release distros
> Rolling release distros usually don't have a point release version. For this, it will be tested peridotically. On the table, the test date is the most contextical.

### Arch Linux
| Test date | Test authored by                              | Method of testing      | Installs? | Runs? | Notes |
| --------- | --------------------------------------------- | ---------------------- | --------- | ----- | ----- |
| TBA       |                                               |                        | TBA       | TBA   |       |

### openSUSE (Tumbleweed)
| Test date | Test authored by                              | Method of testing      | Installs? | Runs? | Notes |
| --------- | --------------------------------------------- | ---------------------- | --------- | ----- | ----- |
| TBA       |                                               |                        | TBA       | TBA   |       |
