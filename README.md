# covid19-tracker-i3blocks

This for adding a Covid 19 case and death count for UK and World Wide to the i3blocks status bar. I was made in response to this [reddit post](https://www.reddit.com/r/i3wm/comments/fjrqyh/i3blocks_idea_for_corona_virus_web_scraper/).

I took the orginal script [found here] (https://pastebin.com/tFZK5vpy) and changed it so that it no longer calculates the addititonal cases or deaths that occured over since the last refresh. (5 minutes)


i3 examples

```
$SCRIPT = path/to/script/folder/
[covid19-ww]
command=$SCRIPT/covid19-count-i3blocks/covid19stats.py ww 
interval=repeat

[covid19-uk]
command=/home/tyler/code/covid19-count-i3blocks/covid19stats.py uk UK
interval=repeat

[covid19-china]
command=/home/tyler/code/covid19-count-i3blocks/covid19stats.py china China
interval=repeat
```
