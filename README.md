# Modeling Swiss farmer's attitudes about climate change

Modeling data from [Kreft et al. 2020](https://www.sciencedirect.com/science/article/pii/S2352340920303048).


.venv\Scripts\activate


dvc stage add -n get_data -d get_data.py -o data_raw.csv python get_data.py