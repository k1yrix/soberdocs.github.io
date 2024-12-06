# Tips & Tricks
---

## 1. GPU doesn't support vulkan?
You can set `"use_opengl"` to `true` in `~/.var/app/org.vinegarhq.Sober/data/sober/config.json`

## 2. Forgot to save your logs for troubleshooting?
Sober actually has a file for the logs. It's located at  `~/.var/app/org.vinegarhq.Sober/data/sober/sober_logs`

There's also a symlink to the latest log in there

## 3. Want to bring back the old oof sound? 
You can set `"bring_back_oof"` to `true` in `~/.var/app/org.vinegarhq.Sober/data/sober/config.json`

## 4. Want to edit FastFlags (FFlags)?

> **WARNING**: Modifying FastFlags here is not officially supported. If you run into issues, you should delete your custom FastFlags first. Continue at your own Risk!

You can edit them under the `"fflags"` section at `~/.var/app/org.vinegarhq.Sober/config/sober/config.json`

### Default-set FastFlags
There are no set default FastFlags in Sober's configuration file. However, in `~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json`, there are set FastFlags to ensure operability.

> Editing FastFlags on `ClientAppSettings.json` is now deprecated in favor of Sober's config file. To ensure operability, you should check this file for any discrepancies.

These are the default FastFlags that are set by default on Sober as of Sober version `0.0.0-1e0cc40`:

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