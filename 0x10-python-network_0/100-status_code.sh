#!/bin/bash
curl -sI "$1" | grep -i "HTTP" | awk '{print $2}'
