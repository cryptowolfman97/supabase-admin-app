[app]

# App identity
title = Supabase Admin by SHV
package.name = supabaseadminbyshv
package.domain = online.shvertex

# Source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,wav,mp3
source.exclude_dirs = .git,__pycache__,bin,.buildozer,venv,.venv,tests

# Version
version = 1

# Requirements
# Add/remove packages here based on your actual imports in main.py
requirements = python3,kivy,requests,certifi,rsa,pyasn1

# Display
orientation = portrait
fullscreen = 0

# Optional assets
# icon.filename = assets/icon.png
# presplash.filename = assets/presplash.png

# Android
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 23
android.allow_backup = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True

# Uncomment only if you want a fixed numeric version code
# android.numeric_version = 100

[buildozer]

log_level = 2
warn_on_root = 1