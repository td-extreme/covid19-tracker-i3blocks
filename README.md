# covid19-tracker-i3blocks

Add a Covid 19 case and death count to the i3blocks status bar. I was made in response to this [reddit post](https://www.reddit.com/r/i3wm/comments/fjrqyh/i3blocks_idea_for_corona_virus_web_scraper/).

I took the orginal script [found here] (https://pastebin.com/tFZK5vpy) and changed it so that it no longer calculates the addititonal cases or deaths that occured since the last refresh. (5 minutes)

i3 examples

```
$SCRIPT = path/to/script/folder/
[covid19-ww]
label=World Wide
command=$SCRIPT/covid19-count-i3blocks/covid19stats.py
interval=3600

[covid19-uk]
label=U.K.
command=$SCRIPT/covid19-count-i3blocks/covid19stats.py uk
interval=3600

[covid19-usa-ny]
label=NY
command=$SCRIPT/covid19-count-i3blocks/covid19stats.py usa/new-york
interval=3600
```
