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

**109** channels, **1,175,322.6** hours playtime between **2023-01-17** and **2024-12-10**


### playtime per genre (top 30)

    76814.3h 6.54% Nachrichten
    53473.3h 4.55% Verkaufsshow
    49017.4h 4.17% Krimiserie
    43346.6h 3.69% Werbesendung
    36635.6h 3.12% Dokureihe
    34859.0h 2.97% Dokusoap
    34398.7h 2.93% Regionalmagazin
    30969.5h 2.63% Dokumentation
    27721.3h 2.36% *unknown*
    22035.5h 1.87% Zeichentrickserie
    21746.9h 1.85% Infomercial
    21013.4h 1.79% Animationsserie
    16721.3h 1.42% Comedyserie
    16461.4h 1.40% Morgenmagazin
    15588.8h 1.33% Talkshow
    15576.9h 1.33% Religionsmagazin
    14547.3h 1.24% Magazin
    11610.5h 0.99% E-Sport
    11323.4h 0.96% Sitcom
    10622.2h 0.90% Wetterbericht
    10401.1h 0.88% Quiz
    10371.7h 0.88% Programmende
    10346.0h 0.88% Komödie
    9054.0h  0.77% Realityshow
    8957.9h  0.76% Politikmagazin
    8809.5h  0.75% Wissensmagazin
    8655.7h  0.74% Börsenmagazin
    7851.3h  0.67% Wirtschaftsmagazin
    7787.2h  0.66% Telenovela
    7779.6h  0.66% Dramaserie
