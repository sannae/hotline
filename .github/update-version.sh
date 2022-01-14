#!/bin/bash

cd ../../core

# Current stats
current_version=$(cat __init__.py | grep '__version__ = ' | cut -d"'" -f2)
current_major=$(echo $current_version | cut -d'.' -f1)
current_minor=$(echo $current_version | cut -d'.' -f2)
current_patch=$(echo $current_version | cut -d'.' -f3)

# Update patch in file
new_patch=$((current_patch + 1))
new_version="$current_major.$current_minor.$new_patch"
sed -i "s/$current_version/$new_version/" __init__.py

# Update minor

# Update major