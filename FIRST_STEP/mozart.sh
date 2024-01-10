#!/bin/bash

ANDROID_SDK="${HOME}/Library/Android/sdk"
PROJECT_PATH="${HOME}/AndroidStudioProjects/MyApplication/"

cd "${PROJECT_PATH}"; ./gradlew :app:connectedDebugAndroidTest

# adb shell ls -lah /storage/emulated/0/Documents/
# adb shell cat /storage/emulated/0/Documents/test_di_scrittura.txt
# adb pull /storage/emulated/0/Documents/test_di_scrittura.txt .
