# DEBUG has to be to False in a production enrironment for security reasons
DEBUG = True
# BitGo wallet token for IP XX.XXX.XX, dispense an access token at www.bitgo.com and set it here

ACCESS_TOKEN = 'bd9fe7307b17238b5409cd2c8a6170a4b8842217249c2fbf914d341e53bacfd8'
# Secret key for generating tokens

SECRET_KEY = 'houdini'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'password')

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'casey.oneill'
MAIL_PASSWORD = 'zZ9425($@%'
ADMINS = ['casey.oneill@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

# Marketplace settings
MARKET_DATA = [{'name': 'ether',
                'prettyName': 'Ether Price Data API',
                'url': 'http://10.244.165.43:8080/ether',
                'price': '5000'}]

## Set your 'up' marketplace endpoint https://github.com/weex/up, uncomment the one below to test out our default
MARKETPLACE_API='http://10.244.165.43:8080/ether' #http://10.244.34.100:21411/up-premium'

# Bitcoin Tutorials
TUTORIALS = [{'url': 'https://contextformdigital.bandcamp.com/album/nightvisions',
              'name': 'Nightvisions',
              'prettyName': 'Desire Lines: Nightvisions',
              'img': 'https://f4.bcbits.com/img/a0473663819_10.jpg',
              'img_hover': 'https://f4.bcbits.com/img/a0473663819_10.jpg',
              'description': 'The brand new EP from Desire Lines and the 11th release on Context + Form Digital.'
             },
             {'url': 'https://contextformdigital.bandcamp.com/album/moments',
              'name': 'Moments',
              'prettyName': 'Desire Lines: Moments',
              'img': 'https://f4.bcbits.com/img/a0067019093_16.jpg',
              'img_hover': 'https://f4.bcbits.com/img/a0067019093_16.jpg',
              'description': 'The 10th release from Context + Form Digital featuring the single "Summerlove."'
             },
             {'url': 'https://contextformdigital.bandcamp.com/album/distant-echoes',
              'name': 'Distant Echoes',
              'prettyName': 'Desire Lines: Distance Echoes',
              'img': 'https://f4.bcbits.com/img/a4027973247_16.jpg',
              'img_hover': 'https://f4.bcbits.com/img/a4027973247_16.jpg',
              'description': 'The ninth release on Context + Form Digital featuring "Passing Between Us" and "There is Always Hope." '
             },
             {'url': 'https://gist.github.com/pkrasam/2befdb9c9b692ef12078',
              'name': 'gist.04_A Bitcoin-Payable_API.md',
              'prettyName': 'A Bitcoin-Payable API',
              'img': 'https://assets.21.co/learn/content/topics/bitcoin-payable-api/bitcoin-payable-api-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/bitcoin-payable-api/bitcoin-payable-api-400-hover.jpg',
              'description': 'Learn how to create a bitcoin-payable API server with Flask. Your server will take a text file and some bitcoin, and return a spoken rendering of that text.'              
             },
             {'url': 'https://gist.github.com/pkrasam/92949b1e9dadf7910bf9',
              'name': 'gist.05_A_Bitcoin_Mashup.md',
              'prettyName': 'A Bitcoin Mashup',
              'img': 'https://assets.21.co/learn/content/topics/bitcoin-mashup/bitcoin-mashup-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/bitcoin-mashup/bitcoin-mashup-400-hover.jpg',
              'description': 'Compose two bitcoin-payable APIs set up by different users to get a sense for what a bitcoin-payable digital supply chain might look like.'              
             },
             {'url': 'https://gist.github.com/pkrasam/b9b36f897d7d35483599',
              'name': 'gist.06_Sell_or_License_Any_File_for_Bitcoin.md',
              'prettyName': 'Sell or License Any File for Bitcoin',
              'img': 'https://assets.21.co/learn/content/topics/sell-or-license-any-file-for-bitcoin/sell-or-license-any-file-for-bitcoin-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/sell-or-license-any-file-for-bitcoin/sell-or-license-any-file-for-bitcoin-400-hover.jpg',
              'description': 'Are you a designer, musician, or author? Use this sample code to turn any directory full of digital assets into your own personal iTunes-like store.'              
             },
             {'url': 'https://gist.github.com/pkrasam/e79f93a7f7d90a0877bb',
              'name': 'gist.07_Bitcoin-Accelerated_Computing.md',
              'prettyName': 'Bitcoin-Accelerated Computing',
              'img': 'https://assets.21.co/learn/content/topics/bitcoin-accelerated-computing/bitcoin-accelerated-computing-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/bitcoin-accelerated-computing/bitcoin-accelerated-computing-400-hover.jpg',
              'description': 'Learn how to outsource computations for bitcoin by paying a remote server for an API call. This illustrates how to use bitcoin as a new kind of system resource.'
             },
             {'url': 'https://gist.github.com/pkrasam/5e010712056c2bdef9e4',
              'name': 'gist.08_Intelligent_Agents_with_Bitcoin.md',
              'prettyName': 'Intelligent Agents with Bitcoin',
              'img': 'https://assets.21.co/learn/content/topics/intelligent-agents-with-bitcoin/intelligent-agents-with-bitcoin-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/intelligent-agents-with-bitcoin/intelligent-agents-with-bitcoin-400-hover.jpg',
              'description': 'Create a simple bitcoin-powered intelligent agent that finds and purchases the digital service with the lowest price in bitcoin.'
             },
             {'url': 'https://gist.github.com/pkrasam/faef101460cae1d6d669',
              'name': 'gist.09_A_Bitcoin-Payable_Notary_Public.md',
              'prettyName': 'A Bitcoin-Payable Notary Public',
              'img': 'https://assets.21.co/learn/content/topics/bitcoin-notary-public/bitcoin-notary-public-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/bitcoin-notary-public/bitcoin-notary-public-400-hover.jpg',
              'description': 'This tutorial will show you how to set up a notary public service. Any user can pay bitcoin to write a message to the blockchain to be stored forever.'
             },
             {'url': 'https://gist.github.com/pkrasam/9bc7b91048a27884e93d',
              'name': 'gist.10_A_Crawler_for_the_Machine-Payable_Web.md',
              'prettyName': 'A Crawler for the Machine-Payable-Web',
              'img': 'https://assets.21.co/learn/content/topics/crawl-the-machine-payable-web/crawl-the-machine-payable-web-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/crawl-the-machine-payable-web/crawl-the-machine-payable-web-400-hover.jpg',
              'description': 'Set up a crawler service on your 21 Bitcoin Computer that checks the status of 402 endpoints.'
             },
             {'url': 'https://gist.github.com/pkrasam/0725515d72bb61c023fb',
              'name': 'gist.11_Monetize_the_Command_Line_with_Bitcoin.md',
              'prettyName': 'Monetize the Command Line with Bitcoin',
              'img': 'https://assets.21.co/learn/content/topics/monetize-the-command-line-with-bitcoin/monetize-the-command-line-with-bitcoin-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/monetize-the-command-line-with-bitcoin/monetize-the-command-line-with-bitcoin-400-hover.jpg',
              'description': 'This tutorial will teach you how to build a bitcoin-payable command line SAAS tool that converts an address to geographic coordinates.'
             },
             {'url': 'https://gist.github.com/pkrasam/d4ab02b91f7d2f6fa83d',
              'name': 'gist.12_Translate_English_to_Chinese_for_Bitcoin.md',
              'prettyName': 'Translate English to Chinese for Bitcoin',
              'img': 'https://assets.21.co/learn/content/topics/bitcoin-translation/bitcoin-translation-400.jpg',
              'img_hover': 'https://assets.21.co/learn/content/topics/bitcoin-translation/bitcoin-translation-400-hover.jpg',
              'description': 'This tutorial will teach you how to set up a simple bitcoin-payable translation API on your 21 Bitcoin Computer.'
             }]
