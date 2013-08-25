krhkliniken.se
==============

Site code for www.krhkliniken.semkvirtualenv krh

    Should be scripted...

    # Generate files (LESS to CSS)
    rm static/generated/*
    #coffee -c -p static/dynamic/script.coffee > static/generated/script.coffee.js
    lessc -x static/dynamic/style.less > static/generated/style.less.css

    # Run Frozen Flask
    pip install -r requirements.txt
    python run.py build

    # Clean up build dir and put on gh-pages branch
    find ./build -name .git\* -type f -delete
    find build/static -name dynamic -type d -exec rm -rf {} \;

    # Make sure to have gh-pages branch checked out under ../krhkliniken.se_ghp
    # mkdir ../krhkliniken.se_ghp && cd ../krhkliniken.se_ghp/
    # git fetch && git checkout -b gh-pages origin/gh-pages
    rsync -a -r -v --remove-source-files build/ ../krhkliniken.se_ghp && rm -rf build
    cd ../krhkliniken.se-ghp && git gui && git push

    # Remove to be able to switch back...
    rm static/dynamic/*

    git checkout master

    ***Note while developing, it can be handy to use watch-lessc***
    watch-lessc -i static/dynamic/style.less -o static/generated/style.less.32228.css
