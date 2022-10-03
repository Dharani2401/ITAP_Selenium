@echo off
for /d /R %%G IN (script.py) do (
IF EXIST %%G (
echo  Test Case Started %%G
python %%G
echo Test Case Ended
)
)
