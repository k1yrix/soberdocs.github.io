# Common issues

---

## RBXCRASH: OutOfMemory (Failed to allocate memory. size = [x], alignment = [y])

That means your graphics card ran out of video memory that Sober is trying to load on. This is especially problematic for NVIDIA users because the drivers have terrible written Linux drivers for VRAM handling. (There has been reports of Intel Haswell and earlier iGPU users facing issues like this too)

The main culprit behind this is basically due to textures being loaded at the highest quality possible, which is the default setting.

### Solution
Append the following FFlags into `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`

```
"DFIntTextureQualityOverride": 2,
"DFFlagTextureQualityOverrideEnabled": true
```

If it doesn't work, set the `"DFIntTextureQualityOverride"` FFlag to `1` instead. Otherwise, you might be out of luck.

> Essentially, to avoid this problem without downscaling textures, you would need an NVIDIA GPU that has 4 GB or greater VRAM. Alternatively, you could also use a Mesa capable GPU (AMD/Intel).

---

## ERROR: Wayland display connection closed by server (fatal)
Wayland basically screwed you over. It's not that stable on Sober compared to X11.

### Solution
Run ```flatpak override --user --socket=x11 --nosocket=wayland org.vinegarhq.Sober```

OR

Install flatseal and:
- Disable the wayland socket
- Enable the X11 sockets

![Turn on XWayland](../images/xwaylandforever.png)

> This problem should be fixed in Sober version `0.0.0-9619e88`. If there is an issue, you should report it on VinegarHQ's Discord server.

---

## Error 71 (Protocol error) dispatching to Wayland display
GTK sometimes messes up Wayland calls for some people. Most people should be fine.

### Solution
See above.

> This problem should be fixed in Sober version `0.0.0-9619e88`. If there is an issue, you should report it on VinegarHQ's Discord server.

---

## FMOD API error
Roblox uses FMOD improperly, resulting in FMOD errors sometimes being spammed into the FLog. These errors happen on real Android devices as well, and are usually not a problem.

### Affected games
- [Rivals](https://www.roblox.com/games/17625359962)
- [a dusty trip](https://www.roblox.com/games/16389395869)

---

## Sober just randomly crashes
Depends on if the logs actually provided something useful. Otherwise, we cannot give a definite answer.

---

## It says Sober couldn't launch because my card does not support Vulkan
Please see [the FAQ](https://soberdocs.github.io/docs/FAQ.html) and see question 3. Otherwise, you will have to use OpenGL.

---

## Sober does not launch on my outdated system
Sober only supports Linux kernel version 5.11 and above. If you are on an outdated version of your distro, your kernel might be too outdated to run Sober.

### Solution
Update your distro to a newer version by following a distro-specific guide.

---

## Sober does not launch to my dedicated GPU
GPUs using Mesa should be fine as long as it's recent. If you're using an NVIDIA card, the driver version installed on your system must match with the Flatpak NVIDIA drivers that is installed on the system. (For example, the installed 560 system drivers cannot run with NVIDIA Flatpak 555 drivers)

### Solution
You can update by typing `flatpak update` on your terminal.

---

## I'm running a virtual machine, but I cannot launch Sober!
Virtual machines are not generally supported. Unless you can passthrough the GPU, it's advised against so to try and run Sober on a virtual machine.

> It kinda does have support, depending if the VM host you're running has OpenGL support, but you're going to get terrible performance out of it.

---

## I cannot install Sober on an ARM64 machine
That's because there isn't any support for ARM devices at the moment. There is no solution to this at the moment, but you're free to try [box64](https://github.com/ptitSeb/box64) and see if that works.

---

## I launched Sober through the browser. It says I cannot join a game because I don't have the permission to do so! (Error 524)
If you haven't logged into Sober, you should do it now. Afterwards you will be able to join from the browser for future sessions. (Please see question #4 on [the FAQ](https://soberdocs.github.io/docs/FAQ.html#q-i-cant-log-in-to-roblox) for more information) Otherwise, it could be just a generic 524.

> Sober does not launch the same way as it usually does on Windows or macOS. Sober will only carry over the join game request, not including login.

---

## No shift lock or camera sensitivity options in the ingame settings
Roblox sometimes forgets you have a mouse and removes the options.

### Solution
Move your mouse while joining a game.

---

## It says Roblox is out of date (Error 280), but Sober isn't updating!
It means that the Roblox build Sober is in has reached it's end of the lifespan. If you are reading this, and Sober hasn't been updated, please wait until they do. Otherwise, you will have to run `flatpak update`.

> This is actually an uncommon issue, since it only happens once every approximate month if Sober is left without an update to a newer Roblox build, but this is just here in case it happens.
> Sober uses a fixed-point release system, which means only one Roblox build is supported at a time per Sober update and there are no automatic updates to the next build. Manually attempting to update Roblox will not work since it requires a specific build version in order to install.

---

## Automatic download isn't working (Long hang time; falls back to manual install)
Three out of ten chances is that your ISP is blocking access to Google Play's APIs, which is what Sober is attempting to contact in order to download the correct APK file. Otherwise, either you should check your internet connection or the API is down.

> There have also been reports of being unable to copy the apk to a directory

### Solution
Use a VPN

---

## Attempting to manually install the Roblox APK goes straight to "Invalid Bundle" screen
Sober wasn't able to find or open a file picker because it was invalid and does not know what to do, so it displays "Invalid Bundle" without prompting to choose an APK file. This is sometimes problematic for several DEs that don't come with their own file pickers.

### DEs affected
- Hyprland

### Solution
Make sure that the file picker for your DE is installed and set correctly.