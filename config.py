
params = {
    "IS_TEST": "True", # True or False

    # twitter user to monitor
    "AUTHOR_ID": "44196397", # Elon's Twitter ID

    # target word to detect
    "TARGET_WORD": "#bitcoin", 
    
    # twitter API credentials: https://developer.twitter.com/en/docs/twitter-api/getting-started/guide
    "CONSUMER_KEY": '< ENTER TWITTER APP CONSUMER KEY HERE >',
    "CONSUMER_SECRET": '< ENTER TWITTER APP CONSUMER SECRET HERE >',
    "BEARER_TOKEN": '< ENTER TWITTER APP BEARER TOKEN HERE >',
    
    "CURRENCY": "btc",
    "TX_AMOUNT": 0.00001, # change to donate all bitcoins when in production
    "DEAFULT_MESSAGE_SUFFIX": ' #TweeElon',

    # bitcoin private key of sending wallets in WIF format
    "TEST_SENDING_WALLET_WIF": 'cV8Ga32esY2KncRbHjCJw84JZqt1HS722wFZVNWixHkgxyNdTJJd', 
    "SENDING_WALLET_WIF": '< ENTER SENDING WALLET WIF HERE >', # need to be decentralized so nobody can steal the coins

    # bitcoin public keys of receiving wallets
    "TEST_RECEIVING_ADDRESS": 'mhGMEHHRYyG4vTEwPgekG89boRrR3o5186',
    "RECEIVING_ADDRESS": '1FJy7Wxrcmja5pK4YB7ccW6ygW7mK4X24A' # BTC address of https://www.givedirectly.org/
    
}
