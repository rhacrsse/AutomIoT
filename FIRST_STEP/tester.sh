#!/bin/bash

ANDROID_SDK="${HOME}/Library/Android/sdk"
PROJECT_PATH="${HOME}/AndroidStudioProjects/TemplateTest1/"

cd "${PROJECT_PATH}"; ./gradlew assembleDebug
cd app/build/outputs/apk/debug
adb install app-debug.apk
adb shell am instrument -w -e class 'com.example.templatetest1.ExampleInstrumentedTest' com.example.templatetest1/androidx.test.runner.AndroidJUnitRunner
