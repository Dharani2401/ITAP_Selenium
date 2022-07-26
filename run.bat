@echo off
For /d /R %%G IN (script.py) do IF EXIST %%G python script.py %%G
