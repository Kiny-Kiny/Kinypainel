#!/bin/bash
#auto-updater script
rm -rf *.py
git clone https://github.com/oporadokrl/Kinypainel.git
mv ./Kinypainel/* ./
rm -rf Kinypainel 
chmod +x *
