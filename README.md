# Simply simplify language understandability score only

Inspired by https://github.com/machinelearningZH/simply-simplify-language by the [Statistisches Amt Kanton Zürich](https://www.zh.ch/de/direktion-der-justiz-und-des-innern/statistisches-amt/data.html). Many thanks for it.

I just wanted the understandability score, so I stripped everything else out and made a simple API for it.

It works on German text only - preferably Swiss High German.

## Usage

**Run the app locally**
- Create a [Conda](https://conda.io/projects/conda/en/latest/index.html) environment: `conda create -n simplify python=3.9`
- Activate environment: `conda activate simplify`
- Clone this repo.
- Change into the project directory: `cd understandability_score/`
- Install packages: `pip install -r requirements.txt`
- Install Spacy language model: `python -m spacy download de_core_news_sm`

- Start app: `uvicorn main:app --port 8005 --reload`

**Run with docker**

- docker build -t simply-understandability-score .
- docker run -p 8005:8005 simply-understandability-score

** Call the API **

```bash
curl --location 'localhost:8005/understandability' \
--header 'Content-Type: application/json' \
--data '{"text":"Die Abteilung «Data» ist zum einen Anlaufstelle für Personen, die Daten zum Kanton Zürich und seinen Regionen nutzen wollen. Sie berät Nutzende und fördert das Wissen rund um Daten. Zum anderen koordiniert sie die kantonale Data Governance und bietet Expertise im Bereich Data Science."}'
```

## How does this score work?
This is a metric that has been created and is still being tested and continuously improved during a pilot project at the administration of the Canton of Zurich. 

The index was created using a dataset of complex legal and administrative texts, as well as many samples of Einfache and Leichte Sprache (Plain and Simple Language). The authors trained a classification model to differentiate between complex and simple texts. By selecting the most significant model coefficients, they devised a formula to estimate a text's understandability (not just its [readability](https://en.wikipedia.org/wiki/Readability)). This pragmatic metric has been found useful during the mentioned pilot project and seems to work well in practice for administrative texts.

The score takes into account sentence lengths, the [readability metrix RIX](https://hlasse.github.io/TextDescriptives/readability.html) as well as the occurrence of common words. 

> [!Important]
> This package assumes the Swiss `ss` in your texts rather than the German German `ß`. You'll get somewhat worse scores, if your text contains `ß`. The difference shouldn't be substantial. Nonetheless, we want you to be aware. At the moment the score does **not** take into account other language properties that are essential for Einfache or Leichte Sprache like use of passive voice, subjunctives, complex structures in short sentences etc. Be also aware that the mapping to CEFR levels A1 to C2 should be considered as a pragmatic approach that gives an *indication* which seems to work well in practice. However, it is by no means an ‘official’ or safe measure.
