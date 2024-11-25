# Tips & Tricks
---

## 1. GPU doesn't support vulkan?
Run Sober in OpenGL mode with: 
``` bash
flatpak run org.vinegarhq.Sober --opengl

```

## 2. Forgot to save your logs for troubleshooting?
Sober actually has a file for the logs. It's located at  `~/.var/app/org.vinegarhq.Sober/data/sober/sober_logs`

There's also a symlink to the latest log in there

## 3. Want to bring back the old oof sound? 
You can set `"bring_back_oof"` to `true` in `~/.var/app/org.vinegarhq.Sober/data/sober/state`
## 4. Want to edit FastFlags (FFlags)?

> **WARNING**: Modifying FastFlags here is not officially supported. If you run into issues, you should delete your custom FastFlags first. Continue at your own Risk!

You can edit them here: `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`

### Default-set FastFlags
These are the default FastFlags that are set by default on Sober as of Sober version `0.0.0-9619e88`:

``` json
{
    "DFFlagDisableDPIScale": true,
    "DFIntTaskSchedulerTargetFps": 0,
    "FFlagAdServiceEnabled": false,
    "FFlagDebugDisableTelemetryEphemeralCounter": true,
    "FFlagDebugDisableTelemetryEphemeralStat": true,
    "FFlagDebugDisableTelemetryEventIngest": true,
    "FFlagDebugDisableTelemetryPoint": true,
    "FFlagDebugDisableTelemetryV2Counter": true,
    "FFlagDebugDisableTelemetryV2Event": true,
    "FFlagDebugDisableTelemetryV2Stat": true,
    "FFlagFutureIsBrightPhase3Vulkan": true,
    "FFlagGameBasicSettingsFramerateCap5": true,
    "FFlagTextureDeduplicationByHash4": false,
    "FLogFMOD": 0
}
```