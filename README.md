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

**97** channels, **556,040.8** hours playtime between **2023-01-17** and **2023-11-22**


### playtime per genre (top 30)

    36592.3h 6.58% Nachrichten
    26589.1h 4.78% Verkaufsshow
    22430.0h 4.03% Krimiserie
    18862.8h 3.39% Werbesendung
    18140.6h 3.26% Dokureihe
    16836.5h 3.03% Dokusoap
    16071.6h 2.89% Regionalmagazin
    14186.3h 2.55% Dokumentation
    13536.7h 2.43% *unknown*
    10303.9h 1.85% Zeichentrickserie
    10133.8h 1.82% Infomercial
    9912.7h  1.78% Animationsserie
    8699.4h  1.56% Comedyserie
    7913.7h  1.42% Morgenmagazin
    7517.2h  1.35% Religionsmagazin
    7432.3h  1.34% Talkshow
    7088.6h  1.27% Magazin
    5595.9h  1.01% Programmende
    5440.3h  0.98% E-Sport
    5341.3h  0.96% Sitcom
    5103.9h  0.92% Wetterbericht
    5049.8h  0.91% Börsenmagazin
    4640.2h  0.83% Quiz
    4337.8h  0.78% Komödie
    4217.1h  0.76% Wissensmagazin
    4171.8h  0.75% Wirtschaftsmagazin
    4093.9h  0.74% Musikmagazin
    4016.8h  0.72% Telenovela
    3894.2h  0.70% Politikmagazin
    3855.4h  0.69% Realityshow
