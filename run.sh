#!/bin/bash
gunicorn -w 1 test:app