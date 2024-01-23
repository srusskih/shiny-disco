#!/usr/bin/env sh
set -e
uvicorn service.main:app --host 0.0.0.0 --reload
