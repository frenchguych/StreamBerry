#!/bin/bash

export -n SESSION_MANAGER
mkdir -p ${XDG_RUNTIME_DIR}

/usr/bin/env python3 ${SNAP}/${SNAP_NAME}.py
