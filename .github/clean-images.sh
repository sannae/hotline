#!/bin/bash

name="hotline"

# List of unique images with the same name
existing_images=$(docker images --format="{{.Repository}} {{.ID}}" | grep $name | cut -d' ' -f2 | tr ' ' '\n' | sort | uniq)

# Remove existing images
for image in $existing_images; do
    if [[ -n $image ]]; then
        docker rmi -f $image
    fi
done

# Prune dangling images
docker image prune -f