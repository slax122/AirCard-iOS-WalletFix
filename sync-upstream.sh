#!/bin/bash
set -euo pipefail
rm -rf AirCard-iOS-upstream
git clone --depth 1 https://github.com/Mak5er/AirCard-iOS.git AirCard-iOS-upstream
printf '\nSynced to AirCard-iOS-upstream/\n'
