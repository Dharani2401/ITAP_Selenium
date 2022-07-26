@echo off
For /d /R %%G IN (json) do IF EXIST %%G python script.py %%G
