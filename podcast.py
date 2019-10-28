from feedgen.feed import FeedGenerator
import urllib
import datetime as dt
import locale
import pytz

# Just to avoid locale problems
def day(i):
    if i==0:
        return "lun"
    elif i==1:
        return "mar"
    elif i==2:
        return "mer"
    elif i==3:
        return "gio"
    elif i==4:
        return "ven"
    elif i==5:
        return "sab"
    else:
        return "dom"


def podcast():
    #locale.setlocale(locale.LC_ALL, "it_IT.utf8")

    base_url = "https://podcast02.unitedradio.it/virginradio.it//NEW/upload/uploadedContent/repliche/drfeelgood/"
    base_url_2="_drfeelgood.mp3"


    today= dt.datetime.today().replace(hour=9,minute=0, second=0)

    days=[today+dt.timedelta(days=i) for i in range(-6,1)]
    days=list(filter(lambda x: (x.weekday()<5), days))

    urls=[ base_url+day(d.weekday())+d.strftime("_%d%m%Y")+base_url_2 for d in days]

    fg=FeedGenerator()
    fg.load_extension("podcast")
    fg.title("Rock and Talk")
    fg.description("Last episodes from Virgin Radio Rock and Talk")
    fg.link(href="https://www.virginradio.it/sezioni/1154/rock-talk")



    fg.podcast.itunes_author("Virgin Radio")
    fg.podcast.itunes_category("Speech", "Rock")
    fg.podcast.itunes_explicit("no")
    fg.podcast.itunes_complete("no")
    fg.podcast.itunes_new_feed_url("http://example.com/new-feed.rss")
    fg.podcast.itunes_summary("Last episodes from Virgin Radio Rock and Talk")

    fg.logo(logo="https://www.virginradio.it/resizer/628/355/true/1548173388720.png--.png?1548173388000")
    fg.image(url="https://www.virginradio.it/resizer/628/355/true/1548173388720.png--.png?1548173388000", title="Rock and talk")
    fg.podcast.itunes_image("https://www.virginradio.it/resizer/628/355/true/1548173388720.png--.png?1548173388000")



    for d,u in zip(days,urls):
        fe = fg.add_entry()
        fe.id(u)
        gg=d.strftime("%A %d %B")
        fe.title(gg)
        fe.description(gg)
        fe.summary(gg)
        #fe.link(href=u, rel="alternate")
        fe.link(href="https://www.virginradio.it/sezioni/1154/rock-talk", rel="alternate") 
        fe.enclosure(u, 0, "audio/mpeg")
        fe.published(pytz.utc.localize(d))

    #fg.rss_file("podcast.xml")

    return fg.rss_str(pretty=True)
