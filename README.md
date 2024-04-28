# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**102** channels, **831,348.6** hours playtime between **2023-01-17** and **2024-04-29**


### playtime per genre (top 30)

    54149.2h 6.51% Nachrichten
    39831.3h 4.79% Verkaufsshow
    33841.6h 4.07% Krimiserie
    29063.5h 3.50% Werbesendung
    26278.7h 3.16% Dokureihe
    25088.6h 3.02% Dokusoap
    24158.7h 2.91% Regionalmagazin
    21541.4h 2.59% Dokumentation
    21259.5h 2.56% *unknown*
    15268.1h 1.84% Zeichentrickserie
    15105.3h 1.82% Infomercial
    14801.3h 1.78% Animationsserie
    12569.7h 1.51% Comedyserie
    11709.1h 1.41% Morgenmagazin
    11668.7h 1.40% Magazin
    11234.2h 1.35% Religionsmagazin
    11073.9h 1.33% Talkshow
    8237.6h  0.99% E-Sport
    7730.5h  0.93% Programmende
    7643.3h  0.92% Sitcom
    7378.1h  0.89% Wetterbericht
    7305.6h  0.88% Börsenmagazin
    7173.9h  0.86% Quiz
    7111.4h  0.86% Komödie
    6156.8h  0.74% Wissensmagazin
    6081.2h  0.73% Politikmagazin
    6026.9h  0.72% Realityshow
    5940.4h  0.71% Wirtschaftsmagazin
    5930.2h  0.71% Telenovela
    5543.5h  0.67% Musikmagazin
