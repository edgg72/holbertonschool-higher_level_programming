#!/bin/bash
curl -sI "$1" | grep Content-Length | cut -c 17,18,19
