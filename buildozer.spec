[app]
source.dir = .
title = BirthdayApp
package.name = birthdayapp
package.domain = org.example
source.include_exts = py,png,mp3
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
entrypoint = main.py
android.api = 34
android.build_tools_version = 34.0.0
android.permissions = INTERNET
android.minapi = 21
presplash.filename = cake.png
copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 0