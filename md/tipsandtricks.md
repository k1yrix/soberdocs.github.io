# Tips & Tricks
<hr>

#### 1. GPU doesn't support vulkan?
Run Sober with as ```flatpak run org.vinegarhq.Sober --opengl```

#### 2. Forgot to save your logs for troubleshooting?
Sober actually has a file for the logs. It's located at  ~/.var/app/org.vinegarhq.Sober/data/sober/sober_logs

There's also a symlink to the latest log in there

#### 3. Want to bring back the old oof sound? 
You can set `"bring_back_oof"` to `true` in ~/.var/app/org.vinegarhq.Sober/data/sober/state
#### 4. Want to edit FastFlags?

> **WARNING**: Modifying FastFlags here is not officialy supported. If you run into issues, you should delete your custom FastFlags first. Continue at your own Risk!

You can edit them here: ~/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json
