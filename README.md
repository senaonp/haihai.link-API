# haihai.link-API
programmatically access [haihai.link](https://haihai.link)

-----

## includes example API applications

### generate website files from public profile data
- https://github.com/senaonp/haihai.link-API/tree/main/sample_api_applications/static_website_generator

<img src="./static_website_generator/img/preview.JPG" width="100%" height="auto">

### get raw public profile data
- https://github.com/senaonp/haihai.link-API/tree/main/sample_api_applications/raw_data_file_generator

<img src="./raw_data_file_generator/img/preview.JPG" width="100%" height="auto">

### get stats on public profile data
- https://github.com/senaonp/haihai.link-API/tree/main/sample_api_applications/profile_stats_generator

<img src="./profile_stats_generator/img/preview.JPG" width="100%" height="auto">

-----

## configuration:
[only required if accessing all data for a specified user] - to setup account configuration for API access, set credentials in [api_config.py](https://github.com/senaonp/haihai.link-API/blob/main/api_config.py#L3-L4)

-----

## how to use:

The API is accessed through [script.py](https://github.com/senaonp/haihai.link-API/blob/main/script.py); several examples have been provided for reference

There are 2 ways to access data in the API:
### - public access
  - does not require credentials to be setup in `api_config.py`
  - provides access to publicly available information for user accounts and widget data
### - user account access
  - requires credentials to be setup in `api_config.py`
  - allows access to all data belonging to the configured user account
  - steps to properly start and end an API session:
    - call `initializeSession()` to start an API session
    - do stuff
    - call `endSession()` to end the API session

-----

## examples:

get public info of user 'isomer': `getUserPublic("isomer")`

```
{'valid': True, 'name': 'isomer', 'description': 'self-studies in technical fields', 'status': 'studying 📚', 'collections': 
[{'name': '💻 Computer Science', 'description': 'Computer science online articles', 'urls': [{'urlName': 'Nature', 'url': 
'https://www.nature.com/subjects/computer-science/nature', 'urlDescription': ''}, {'urlName': 'arXiv CS', 'url': 'https://arxiv.org/list/cs/new', 
'urlDescription': ''}, {'urlName': 'Google AI Blog', 'url': 'https://ai.googleblog.com/', 'urlDescription': ''}, {'urlName': 'Amazon Science', 
'url': 'https://www.amazon.science/publications', 'urlDescription': ''}], 'public': True, 'idx': 0}, {'name': '🉑️ Languages', 'description': 
'Language study resources', 'urls': [{'urlName': 'Anki', 'url': 'https://apps.ankiweb.net/', 'urlDescription': 'flashcards application for 
memorization'}, {'urlName': 'Tatoeba', 'url': 'https://tatoeba.org', 'urlDescription': 'database with example sentence translations'}, 
{'urlName': 'Duolingo', 'url': 'https://www.duolingo.com/', 'urlDescription': 'application to learn languages through lessons with skill 
trees'}], 'public': True, 'idx': 1}, {'name': '⚙️ Systems Design', 'description': 'Resources for designing systems architecture', 'urls': 
[{'urlName': 'What is a CDN? | How do CDNs work?', 'url': 'https://www.cloudflare.com/learning/cdn/what-is-a-cdn/', 'urlDescription': ''}, 
{'urlName': 'DNS server types', 'url': 'https://www.cloudflare.com/learning/dns/dns-server-types/', 'urlDescription': ''}, {'urlName': 'Caching 
Overview', 'url': 'https://aws.amazon.com/caching/', 'urlDescription': ''}, {'urlName': 'What Is Load Balancing?', 'url': 
'https://www.nginx.com/resources/glossary/load-balancing/', 'urlDescription': ''}, {'urlName': 'CI/CD concepts', 'url': 
'https://docs.gitlab.com/ee/ci/introduction/', 'urlDescription': ''}, {'urlName': 'What Are Distributed Systems?', 'url': 
'https://www.splunk.com/en_us/data-insider/what-are-distributed-systems.html', 'urlDescription': ''}, {'urlName': 'What are Microservices?', 
'url': 'https://aws.amazon.com/microservices/', 'urlDescription': ''}, {'urlName': 'What is a web server?', 'url': 
'https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server', 'urlDescription': ''}, {'urlName': 
'RESTful web API design', 'url': 'https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design', 'urlDescription': ''}, 
{'urlName': 'The WebSocket API (WebSockets)', 'url': 'https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API', 'urlDescription': ''}, 
{'urlName': 'SOLID', 'url': 'https://en.wikipedia.org/wiki/SOLID', 'urlDescription': ''}, {'urlName': 'Comparison of programming paradigms', 
'url': 'https://en.wikipedia.org/wiki/Comparison_of_programming_paradigms', 'urlDescription': ''}, {'urlName': 'What is Network Monitoring?', 
'url': 'https://www.whatsupgold.com/what-is-network-monitoring', 'urlDescription': ''}, {'urlName': 'Introduction to metrics', 'url': 
'https://docs.splunk.com/Observability/metrics-and-metadata/metrics.html', 'urlDescription': ''}], 'public': True, 'idx': 2}]}
```

-----

get public info of user 'haihai': `getUserPublic("haihai")`

```
{'valid': True, 'name': 'haihai', 'description': 'haihai.link system account', 'collections': [{'name': 'haihai.link', 'description': 
'📑 haihai.link resources', 'urls': [{'urlName': 'haihai kanban items', 'url': 'http://greentea.moe/data/kanban/haihai/', 'urlDescription': 
'this kanban has statuses on tasks for this website; these include new features, infra changes, error reports, etc'}, {'urlName': 'about', 
'url': 'haihai.link/info/about/', 'urlDescription': 'information about the website'}, {'urlName': 'website policy', 'url': 
'haihai.link/info/policy/', 'urlDescription': 'policy on web application usage and management'}, {'urlName': 'contact', 'url': 
'haihai.link/info/contact/', 'urlDescription': 'place to provide feedback or report an issue'}, {'urlName': 'FAQ', 'url': 'haihai.link/info/faq/', 
'urlDescription': 'information on frequently asked questions'}, {'urlName': 'dashboard', 'url': 'haihai.link', 'urlDescription': 'dashboard with 
widgets on website information'}, {'urlName': 'API', 'url': 'https://github.com/senaonp/haihai.link-API', 'urlDescription': 'programmatically 
access haihai.link'}], 'public': True, 'idx': 0}, {'name': 'admin users', 'description': 'haihai.link admin users', 'urls': [{'urlName': 'senaonp', 
'url': 'haihai.link/viewUser/senaonp', 'urlDescription': 'webmaster'}, {'urlName': 'haihai', 'url': 'haihai.link/viewUser/haihai', 'urlDescription': 
'system account'}], 'public': True, 'idx': 1}]}
```

-----

get the data of latest publicly updated URL collections: `getWidgetDataLatestCollections()`

```
{'valid': True, 'data': [{'name': 'goals', 'description': '📈 long-term stuff to do', 'user': 'senaonp'}, {'name': 'events', 'description': 
'🎫 some events to consider attending', 'user': 'senaonp'}, {'name': '⚙️ Systems Design', 'description': 'Resources for designing systems architecture', 
'user': 'isomer'}, {'name': 'video channel', 'description': '🖥️ videos on personal website channel (categories: gaming, unboxing, hobby, programming, 
other)', 'user': 'senaonp'}, {'name': 'video games', 'description': '🎮 video games that i play and any available account ids; feel free to add me!', 
'user': 'senaonp'}, {'name': 'figure wishlist', 'description': '🔖 current anime/game figure wishlist', 'user': 'senaonp'}, {'name': 'haihai.link 
admin accounts', 'description': 'haihai.link admin accounts', 'user': 'admin'}, {'name': '🉑️ Languages', 'description': 'Language study resources', 
'user': 'isomer'}, {'name': 'shopping wishlist', 'description': '🛒 items that would be nice to have but not necessary', 'user': 'senaonp'}, {'name': 
'ニコニコ', 'description': '📺 favorite videos on nicovideo', 'user': 'senaonp'}, {'name': '哔哩哔哩', 'description': '📺 favorite videos on bilibili', 
'user': 'senaonp'}, {'name': 'Test URL Collection', 'description': 'Hello', 'user': 'Cherry'}, {'name': 'pixiv favorites', 'description': '❤️ ️favorited 
artwork on pixiv.net', 'user': 'senaonp'}, {'name': 'music', 'description': '🎵 music collection', 'user': 'senaonp'}, {'name': 'pixiv bookmarks 2022', 
'description': '⭐ bookmarked artworks in 2022', 'user': 'senaonp'}, {'name': '💻 Computer Science', 'description': 'Computer science online articles', 
'user': 'isomer'}, {'name': 'my websites', 'description': '🌐 websites that i maintain', 'user': 'senaonp'}, {'name': 'admin users', 'description': 
'haihai.link admin users', 'user': 'haihai'}, {'name': 'haihai.link', 'description': '📑 haihai.link resources', 'user': 'haihai'}, {'name': 'online 
accounts', 'description': 'online accounts that i use', 'user': 'senaonp'}]}
```

-----

get the data of latest contributors: `getWidgetDataLatestContributors()`

```
{'valid': True, 'data': [{'user': 'senaonp'}, {'user': 'haihai'}, {'user': 'isomer'}, {'user': 'HelloKupo'}, {'user': 'Cherry'}, {'user': 'admin'}, 
{'user': 'planete29'}, {'user': 'stemS'}]}
```

-----

get the urls of the latest contributors: `getWidgetUrlsLatestContributors()`

```
['https://haihai.link/viewUser/senaonp', 'https://haihai.link/viewUser/haihai', 'https://haihai.link/viewUser/isomer', 'https://haihai.link/viewUser/HelloKupo', 
'https://haihai.link/viewUser/Cherry', 'https://haihai.link/viewUser/admin', 'https://haihai.link/viewUser/planete29', 'https://haihai.link/viewUser/stemS']
```

-----

get the urls of the latest publicly updated URL collections: `getWidgetUrlsLatestCollections()`

```
['https://haihai.link/viewCollection/senaonp/goals', 'https://haihai.link/viewCollection/senaonp/events', 'https://haihai.link/viewCollection/isomer/⚙️_Systems_Design', 
'https://haihai.link/viewCollection/senaonp/video_channel', 'https://haihai.link/viewCollection/senaonp/video_games', 'https://haihai.link/viewCollection/senaonp/figure_wishlist', 
'https://haihai.link/viewCollection/admin/haihai.link_admin_accounts', 'https://haihai.link/viewCollection/isomer/🉑️_Languages', 'https://haihai.link/viewCollection/senaonp/shopping_wishlist', 
'https://haihai.link/viewCollection/senaonp/ニコニコ', 'https://haihai.link/viewCollection/senaonp/哔哩哔哩', 'https://haihai.link/viewCollection/Cherry/Test_URL_Collection', 
'https://haihai.link/viewCollection/senaonp/pixiv_favorites', 'https://haihai.link/viewCollection/senaonp/music', 'https://haihai.link/viewCollection/senaonp/pixiv_bookmarks_2022', 
'https://haihai.link/viewCollection/isomer/💻_Computer_Science', 'https://haihai.link/viewCollection/senaonp/my_websites', 'https://haihai.link/viewCollection/haihai/admin_users', 
'https://haihai.link/viewCollection/haihai/haihai.link', 'https://haihai.link/viewCollection/senaonp/online_accounts']
```
