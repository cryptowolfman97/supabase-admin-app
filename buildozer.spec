[app]

title = Supabase Admin by SHV
package.name = supabaseadminbyshv
package.domain = com.shvertex

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,csv
version = 1.0

requirements = python3,kivy,requests,certifi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

# Keep the package lean and stable for phone-first workflows
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2

