import config
from twitterAPI import TwitterAPI
from bitcoinAPI import BitcoinAPI

# query twitter API and return last tweet if target word detected in it
tw = TwitterAPI(config.params["AUTHOR_ID"], config.params["TARGET_WORD"])
tweet_with_word = tw.get_last_tweet_if_word()

# execute bitcoin transaction if word detected in last tweet
if tweet_with_word:
        
    # create and execute bitcoin transaction
    bit = BitcoinAPI()
    if config.params["IS_TEST"] == "True":
        my_key = bit.load_wallet(config.params["TEST_SENDING_WALLET_WIF"], is_test = True)
        bit.execute(my_key, config.params["TEST_RECEIVING_ADDRESS"], tweet_with_word)
    else:
        my_key = bit.load_wallet(config.params["SENDING_WALLET_WIF"]) 
        bit.execute(my_key, config.params["RECEIVING_ADDRESS"], tweet_with_word)
else:
    print("'" + config.params["TARGET_WORD"] + "'" + " not present in " + config.params["AUTHOR_ID"] + "'s last tweet")