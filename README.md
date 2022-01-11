# Integration between Thoth and Wikidata

## Summary

Thoth (https://thoth.pub/) is an open metadata management and dissemination system produced as part of the COPIM project (https://copim.ac.uk/). Thoth is used for metadata management for open-access books and for metadata dissemination to digital repositories, libraries, and vendors.

This code is an experimental integration between Thoth's API client (https://github.com/thoth-pub/thoth-client) and Wikidata's MediaWiki API (https://www.wikidata.org/wiki/Wikidata:Data_access) to send metadata about publications in Thoth to Wikidata. The program retrieves bibliographic data for a publication from Thoth, translates it into the quasi-FRBRised form that Wikidata uses for books (i.e. distinguishing between 'works' and 'editions' as outlined in https://www.wikidata.org/wiki/Wikidata:WikiProject_Books), and submits the data to Wikidata by creating new entities and updating data statements for those entities.

## Usage

The main program runs from main.py with Thoth API options defined in thoth.py (i.e. limiting the API return to one publication rather than lots of publications). Run:

`docker exec -it python python main.py`

to run this main script.

There's an additional script to read data from the Thoth API for testing and parsing data. This runs with:

`docker exec -it python python thoth_read_data.py`

## Parameters

Config for API keys and Wikidata properties is in a config.env.dev or config.env.prod file. This is brought up as an environment file for the Docker environment and specifies MediaWiki API variables as well as property values for Wikidata or test Wikidata.

MediaWiki API variables include the URL of either test or production Wikidata and a username and password for the user running the program. The user needs to have a MediaWiki account and should set a bot password (https://www.mediawiki.org/wiki/Special:BotPasswords) to allow the script to perform tasks like 'high-volume editing', 'edit existing pages', 'create, edit, and move pages'.

Properties of books on Wikidata such as 'title' are specified using property values (e.g. title is 'P1476'). But these property values differ between test.wikidata.org and wikidata.org. 'title' in test.wikidata.org is 'P77107' compared to 'P1476' in production. So the environment files specify the property values for whichever version of Wikidata you're using the script against.
