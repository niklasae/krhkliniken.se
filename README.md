krhkliniken.se
==============

Site code for www.krhkliniken.semkvirtualenv krh

    Should be scripted...
    rm static/generated/*
    #coffee -c -p static/dynamic/script.coffee > static/generated/script.coffee.$RANDOM.js
    lessc -x static/dynamic/style.less > static/generated/style.less.$RANDOM.css

    pip install -r requirements.txt
    python run.py build
