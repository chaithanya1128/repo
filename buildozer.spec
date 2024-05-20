[app]

# Title of your application
title = My Application

# Package name
package.name = myapp

# Package domain (needed for android/ios packaging)
package.domain = org.test

# Source code where the main.py live
source.dir = app.py


# Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# Application versioning
version = 0.1

# Application requirements
requirements = python3,kivy

# Supported orientations
orientation = portrait

# Android specific settings
fullscreen = 0
archs = arm64-v8a, armeabi-v7a
allow_backup = True

#
# iOS specific settings
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]

# Log level
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1

