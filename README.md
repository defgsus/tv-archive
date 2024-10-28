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

**109** channels, **1,112,482.2** hours playtime between **2023-01-17** and **2024-10-29**


### playtime per genre (top 30)

    72430.9h 6.51% Nachrichten
    51208.7h 4.60% Verkaufsshow
    46227.8h 4.16% Krimiserie
    40767.5h 3.66% Werbesendung
    34802.1h 3.13% Dokureihe
    33277.3h 2.99% Dokusoap
    32521.5h 2.92% Regionalmagazin
    29178.7h 2.62% Dokumentation
    26380.9h 2.37% *unknown*
    20769.4h 1.87% Zeichentrickserie
    20479.0h 1.84% Infomercial
    19892.5h 1.79% Animationsserie
    16040.5h 1.44% Comedyserie
    15560.2h 1.40% Morgenmagazin
    14967.7h 1.35% Religionsmagazin
    14715.4h 1.32% Talkshow
    14081.1h 1.27% Magazin
    11005.4h 0.99% E-Sport
    10712.1h 0.96% Sitcom
    10068.5h 0.91% Wetterbericht
    9873.5h  0.89% Programmende
    9767.1h  0.88% Quiz
    9759.0h  0.88% Komödie
    8461.9h  0.76% Realityshow
    8454.5h  0.76% Börsenmagazin
    8409.7h  0.76% Politikmagazin
    8358.8h  0.75% Wissensmagazin
    7477.5h  0.67% Wirtschaftsmagazin
    7328.2h  0.66% Telenovela
    7265.8h  0.65% Dramaserie
