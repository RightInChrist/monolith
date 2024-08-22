# Search public YouTube data.

The `VideoSpider` uses the `data/ric_formatted/channels.json` to extract video data.

The `TranscriptionSpider` uses the `data/ric_formatted/videos.json` to extract the transcription data.

The Spider should place API responses into the `data/raw/{SpiderName}` location and check if the response already exists and is cached before making the API request to YouTube.

Ultimately we end up with data in `data/index` which can be used for searching.

