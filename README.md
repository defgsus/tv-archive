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

**96** channels, **355,388.2** hours playtime between **2023-01-17** and **2023-08-02**


### playtime per genre (top 30)

    23568.3h 6.63% Nachrichten
    16957.6h 4.77% Verkaufsshow
    14328.8h 4.03% Krimiserie
    11949.9h 3.36% Werbesendung
    11637.4h 3.27% Dokureihe
    10718.6h 3.02% Dokusoap
    10194.5h 2.87% Regionalmagazin
    8936.1h  2.51% Dokumentation
    8629.8h  2.43% *unknown*
    6730.2h  1.89% Zeichentrickserie
    6500.2h  1.83% Infomercial
    6276.0h  1.77% Animationsserie
    5846.1h  1.64% Comedyserie
    4975.4h  1.40% Morgenmagazin
    4720.4h  1.33% Religionsmagazin
    4697.6h  1.32% Talkshow
    4231.1h  1.19% Magazin
    4045.0h  1.14% Programmende
    3512.3h  0.99% E-Sport
    3348.7h  0.94% Sitcom
    3335.2h  0.94% Wetterbericht
    3229.3h  0.91% Börsenmagazin
    2837.2h  0.80% Quiz
    2784.8h  0.78% Musikmagazin
    2732.7h  0.77% Wirtschaftsmagazin
    2729.7h  0.77% Komödie
    2683.9h  0.76% Wissensmagazin
    2453.1h  0.69% Telenovela
    2326.0h  0.65% Sportmagazin
    2286.0h  0.64% Reportagereihe
