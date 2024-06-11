# Simply simplify language understandability score only

Inspired by https://github.com/machinelearningZH/simply-simplify-language by the Statistisches Amt Kanton Zürich. Many thanks for it.

I just wanted the understandability score, so I stripped everything else out and made a simple API for it.

It works on German text only.

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