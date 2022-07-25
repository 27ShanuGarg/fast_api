#!/bin/sh
python3 -m uvicorn app.__init__:app --reload
