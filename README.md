# DailDebates
Downloading and cleaning transcripts of debates in the Irish Parliament, 1922-2018

[Official site](https://www.oireachtas.ie/en/debates)

For replication, run in this order:

1. `IE_debates_download.R` -- Generates links to all pages that link to debate records
2. `download_level2_pages.py` -- Downloads all search results pages and saves pages as `.html` files.
3. `combined_download.py` -- Downloads the debates text from `.html` files and saves `.json` file for each day on which at least one debate was held. 

`dail_download_support_functions.py` contains helper functions for `download_level2_pages.py` and `combined_download.py`.