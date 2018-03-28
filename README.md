# GitBot
A Q/A bot for Git FAQ build with Microsoft Bot Builder [SDK]("https://github.com/Microsoft/botbuilder-python/wiki")

`{"question":"What's the difference between fetch and pull?"}`

`{
    "answers": [
        {
            "answer": "The short definition is: Fetch: Download (new) objects and a head from another repository. Pull: Fetch (as defined above), and then merge what was downloaded with the current development.   See the [git-fetch(1)](http://www.kernel.org/pub/software/scm/git/docs/git-fetch.html) and [git-pull(1)](http://www.kernel.org/pub/software/scm/git/docs/git-pull.html) man pages or the tutorials for more details.",
            "questions": [
                "What&#39;s the difference between fetch and pull?"
            ],
            "score": 99
        }
    ]
}`


## Usage
You will need a python 3.6.4 and [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator) to run this in your local machine

`git clone https://github.com/ledrui/GitBot.git`

run `main.py`

Open your [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator) and enter the your endpoint:
`localhost:9000/api/message`. update the port number to your local serving port, in my case it is 9000 yours might be different
