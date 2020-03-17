# covid19-tracker-i3blocks

This for adding a Covid 19 case and death count for UK and World Wide to the i3blocks status bar. I was made in response to this [reddit post](https://www.reddit.com/r/i3wm/comments/fjrqyh/i3blocks_idea_for_corona_virus_web_scraper/).

I took the orginal script [found here] (https://pastebin.com/tFZK5vpy) and changed it so the updates are written to a file.  

To use this add this to your i3blocks file and the covid19status.py script to your startup

```
[covid19]
command=inotifywait -qq -e close_write ~/Temp/covid19-count-i3blocks/log.txt; echo $(tail -1 ~/Temp/covid19-count-i3blocks/log.txt)
interval=repeat
```





