@echo off
for /d /R %%G IN (script.py) do IF EXIST %%G python %%G
