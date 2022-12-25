#!/bin/bash
alias serve='sh serve.sh'
# source venv/Scripts/activate
start "http://localhost:8000"
uvicorn main:app --reload