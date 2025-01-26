name: Test Gemini

on:
  push:
    paths:
      - "src/tests/test_gemini.py"  # test_gemini.pyが変更されたときのみトリガー
  pull_request:
    paths:
      - "src/tests/test_gemini.py"

jobs:
  test-gemini:
    runs-on: ubuntu-latest

    env:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Install src as a module
      run: |
        pip install -e src

    - name: Run gemini tests
      run: |
        python src/tests/test_gemini.py
