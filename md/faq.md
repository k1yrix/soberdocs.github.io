# FAQ (Frequently Asked Questions)
<hr>

## Q: Why Does this exist?
A: Because people on Linux still want to be able to play Roblox easily.

## Q: Is the [GPU here] compatible?
A: If it was made in the last 8 years or so and has Vulkan support either in Mesa or Nvidia drivers, then yes. If you're not sure, check [GPUInfo](https://vulkan.gpuinfo.org/) and search your graphics card. If it doesn't support Vulkan 1.1 or higher, you can try the `--opengl` argument when launching Sober to force OpenGL, if it still doesn't work, you're out of luck.

![Vulkan Supported](/images/vulkaninfo.png)

## Q: I can't log in to Roblox!
A: If it didn't say explicitly you have a wrong password or something like that, reopen Sober and check if it logged you in. If that didn't work, try **"Login with Another Device"** on the login page.

## Q: Studio suport?
A: Last time I checked Roblox on Android doesn't have a studio app. Use [Vinegar](https://vinegarhq.org/) for Roblox Studio which uses the Windows version of Roblox Studio with Wine.

## Q: Why is this closed source?
A: From what we know, it's partially so Roblox can't find how to block it easily and so 9 year old script kiddies aren't annoying in pull requests.

## Q: Roblox is crashing after around 5-10 minutes in game!
If you're on Wayland it's because Wayland support isn't great at the moment so you'll want to turn off Wayland support with [Flatseal](https://flathub.org/apps/com.github.tchx84.Flatseal). And if you're on X11, don't know how to help you.

![Turn on XWayland](/images/xwaylandforever.png)

## Q: ARM64 support?
A: Maybe eventually, but right now there are too many issues to deal with to add support right now.