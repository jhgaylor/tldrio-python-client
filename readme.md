## To install w/ pip

    pip install git+https://github.com/jhgaylor/tldrio-python-client.git

## How to use

    from tldr import TLDRClient

    t = TLDRClient("name", "key")
    latest = t.getLatestTldrs(3)
    tldr_mainpage = t.searchByUrl("http://tldr.io")
    batch = t.searchBatch(["http://tldr.io","http://jakelevine.me/blog/2013/04/nobody-knows-that-i-use-these-apps/"])
    user = t.getUser("jhgaylor")
    user_tldrs = t.getUserData("jhgaylor")

    print latest, tldr_mainpage, batch, user, user_tldrs