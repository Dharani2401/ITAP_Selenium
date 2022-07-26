@echo off
For /d /R %G%G IN (script.py) do IF EXIST %%G python json/script.py %%G
For /d /R %G%G IN (script.py) do IF EXIST %%G python script/script.py %%G
