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

## RBXCRASH: OutOfMemory (swOcc_alloc failed on [x] bytes [y] alignment)
Apparently this one is an entirely different problem compared to the failed to allocate memory variant. This one freaks out during the allocation due to problems of rendering in a specific way and does not know what to do next, so it crashes before anything could be loaded into the video memory. This one isn’t NVIDIA exclusive, as confirmed by multiple people without NVIDIA hardware.

### Solution
Append the following FFlags into `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`

```
"DFFlagUseVisBugChecks": false,
"FFlagEnableVisBugChecks27": false
```

### Affected games
- [Evade](https://www.roblox.com/games/9872472334)

---

## ERROR: Wayland display connection closed by server (fatal)
Wayland basically screwed you over. It's not that stable on Sober compared to X11.

### Solution
Install flatseal and:
- Disable the wayland socket
- Enable the X11 sockets

![Turn on XWayland](../images/xwaylandforever.png)

---

## Error 71 (Protocol error) dispatching to Wayland display
GTK sometimes messes up Wayland calls for some people. Most people should be fine.

### Solution
See above.

---

## FMOD API error
FMOD freaked out because something sound-related horribly went wrong and did not know what to do, so it crashed.

### Solution
Unfortunately there isn't any that could help this problem.

### Affected games
- [Rivals](https://www.roblox.com/games/17625359962)

---

## Sober just randomly crashes
Depends on if the logs actually provided something useful. Otherwise, we cannot give a definite answer.

---

## It say Sober couldn't launch because my card does not support Vulkan
Please see [the FAQ](https://soberdocs.github.io/docs/FAQ.html) and see question 3. Otherwise, you are out of luck.

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
That's because there isn't any support for ARM devices at the moment.