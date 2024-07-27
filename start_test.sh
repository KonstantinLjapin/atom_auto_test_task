#!/bin/bash
# need chmod +
pytest tests/test_post.py -v
pytest tests/test_put.py -v
pytest tests/test_get.py -v