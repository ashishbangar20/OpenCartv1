@echo off
where python
where pytest
python --version
pytest --version
pytest -s -v .\testCases\ -m "sanity"