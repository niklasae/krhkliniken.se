krhkliniken.se
==============

Site code for www.krhkliniken.semkvirtualenv krh

    Should be scripted...

    # Generate files (LESS to CSS)
    rm static/generated/*
    #coffee -c -p static/dynamic/script.coffee > static/generated/script.coffee.$RANDOM.js
    lessc -x static/dynamic/style.less > static/generated/style.less.$RANDOM.css

    # Run Frozen Flask
    pip install -r requirements.txt
    python run.py build

    # Clean up build dir and put on gh-pages branch
    find ./build -name .git\* -type f -delete
    find build/static -name dynamic -type d -exec rm -rf {} \;

    git checkout gh-pages
    rsync -a -r -v --remoce-source-files build/ ./
    rm -rf build

    # Remove to be able to switch back...
    rm static/dynamic/*

    git checkout master
