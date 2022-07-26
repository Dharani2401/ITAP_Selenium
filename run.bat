@echo off
For /d %%G IN (script.py) do IF EXIST %%G python json/script.py %%G
