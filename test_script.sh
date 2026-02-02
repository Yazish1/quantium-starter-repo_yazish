#!/usr/bin/env bash
source venv/Scripts/activate
python -m pytest test_dom.py

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "Test Passed!"
    exit 0
else
    echo "Test failed"
    exit 1
fi

