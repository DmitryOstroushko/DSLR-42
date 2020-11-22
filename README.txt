https://habr.com/ru/company/io/blog/265007/

1. Libraries

    pip install -r requirements.txt

    Library versions:
     python 3.7.3
     numpy 1.16.2
     matplotlib 3.0.3
     tqdm 4.48.0
     mypy 0.790
     pylint 2.3.1
     astroid 2.2.5
     [GCC 7.3.0]

2. Data description:
    1) <dataset>:
        For TRAIN DATASET:
            Dimension: 1601 * 19
            Array of 1601 rows: header, 1600 rows with data
            Single row consists from 19 values: index, name of house, 4 columns with information about student, 13 features

            <dataset> is split on 3 part: see 2) - 4)

    2) <houses>: sorted list of names of houses (List[str])

    3) <features>: list of names of features (List[str])
        For TRAIN DATASET:
            Dimension: 14 columns: 1st name for "house name" + 13 names of features
            This structure is due to correspond <data> array

    4) <data>: two-dimensional array with values of features
        For TRAIN DATASET:
            Dimension: 1600 * 14
            Array of 1600 rows with data
            Single row consists from 14 values: name of house, 13 features

3. General bonuses:
    1) typing check
	mypy <python_file.py>
	# mypy --ignore-missing-imports <python_file.py>
    2) PEP 8 check
	pylint <python_file.py>
	3) docstring: in Google style
	https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
	python.org/dev/peps/pep-0008

4. DESCRIBE function bonuses:
    - print options: v and h
    - logging: levels DEBUG, INFO, WARNING, ERROR и CRITICAL
    - option: to include index column in features list

5. HISTOGRAM function bonuses:
    - printing histograms for all courses

6. SCATTER_PLOT function bonuses:
    - printing graphs for all courses
    - auto defining similar features

7. PAIR_PLOT:
    - Astronomy - 2
    - Herbology - 3
    - Ancient Runes - 7
    - Defense Against the Dark Arts - 4 - нет

8. LOGREG_TRAIN:
    - progress bar
    - reading numbers of features from file to train the model
    - changing parameters of the model
    - calculating of accuracy score

9. LOGREG_PREDICT
    - reading numbers of features from file to predict
