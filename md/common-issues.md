# RBXCRASH: OutOfMemory (Failed to allocate memory. size = [x], alignment = [y])

That means your graphics card ran out of video memory that Sober is trying to load on. This is especially problematic for NVIDIA users because they have terrible written Linux drivers for VRAM handling. (There has also been reports of Intel Haswell and earlier iGPU users facing issues like this too)

The main culprit behind this is basically due to textures being loaded at the highest quality possible, which is the default setting.

## Solution
Append the following FFlags into `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`

```
"DFIntTextureQualityOverride": "2",
"DFFlagTextureQualityOverrideEnabled": "True"
```

# RBXCRASH: OutOfMemory (swOcc_alloc failed on [x] bytes [y] alignment)
Apparently this one is an entirely different problem compared to the failed to allocate memory variant. This one freaks out during the allocation for some reason and does not know what to do next, so it crashes before anything could be loaded into the video memory. This one isn’t NVIDIA exclusive, as confirmed by multiple witnesses.

## Solution
Append the following FFlags into `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`

```
"DFFlagUseVisBugChecks": false,
"FFlagEnableVisBugChecks27": false
```

## Affected games
Evade

# ERROR: Wayland display connection closed by server (fatal)
Wayland basically screwed you over. It's not that stable on Sober compared to X11.

## Solution
Install flatseal and:
- Disable the wayland socket
- Enable the X11 sockets

![Turn on XWayland](../images/xwaylandforever.png)

# Error 71 (Protocol error) dispatching to Wayland display
GTK sometimes messes up Wayland calls for some people. Most people should be fine.

## Solution
See above.

# FMOD API error
FMOD freaked out because something sound-related horribly went wrong and did not know what to do, so it crashed.

## Solution
Unfortunately there isn't that could help this problem.

# Sober just randomly crashes
Depends on if the logs actually provided something useful. Otherwise, we cannot give a definite answer.

# It say Sober couldn't launch because my card does not support Vulkan.
Please see [the FAQ](https://soberdocs.github.io/docs/FAQ.html) and see question 3. Otherwise, you are out of luck.