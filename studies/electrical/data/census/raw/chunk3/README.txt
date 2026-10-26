Raw data for census chunk 3 (pulled 2026-10-26).
loader/: yt.py output per channel (<id>_latest.json 2 pages, _popular.json 3 pages, _oldest.json 1 page; _latest8.json deeper loads for 5 channels); loader/video/: yt.py video for first uploads of channels started in the last 24 months.
about/: YouTube about-panel scrape (same fields NexLev youtube_channel_about returns: description, links, joined, views; checked identical on Everyday Home Repairs).
nexlev/: batchNN.csv = get_batch_channel_metrics_v2 results (batch01/02 also as JSON); nichefinder_lookups.csv = search_niche_finder_channels lookups (hit only when ytChannelId matched).
thumbs/: 3 thumbnails per channel (Popular top 2 long-form + newest) and the contact sheets used to judge channel type (thumbplan.json maps channel index to video IDs).
loader_summary_work.json: per-channel summary built from the loader files (index order = chunk3.csv order).
