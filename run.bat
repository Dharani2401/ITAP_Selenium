@echo off
For /d %%G IN (script) do IF EXIST %%G python script.py %%G
