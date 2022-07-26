@echo off
For /d /R %%G IN (sc) do IF EXIST %%G python json/script.py %%G
