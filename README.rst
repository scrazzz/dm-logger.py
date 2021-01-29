``dm-logger.py``
==========
A Python script that logs Discord DMs on a user account.

``ToS``
==========
Yes, this is against Discord's ToS and Discord can detect you using this.

``Getting started``
==========
Clone this repository:

.. code:: sh
    
    git clone https://github.com/scrazzz/dm-logger.py
    cd dm-logger.py
    python3 -m pip install -r requirements.txt

Now go to ``logger.py`` file and then edit the **URL** and **TOKEN** inside the code.

After that run the code:

.. code:: sh
    
    python3 logger.py

``Changelog``
==========
- ``v0.1.0``: Initial commit.
- ``v0.2.0``: Code fix.
- ``v0.3.0``: Removed Webhook.Async since it's not a huge problem of it being sync.
- ``v0.3.1``: Code fix and logging attachments.
- ``v0.4.0``: Log images and gifs ONLY properly.
- ``v0.4.1``: Add missing import and no_help command.
