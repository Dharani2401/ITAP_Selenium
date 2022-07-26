@echo off
For /d %%G IN (json) do IF EXIST %%G python script.py %%G
