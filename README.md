# biomedical-data-analysis

Exploratory analysis and visualisation of a fictional biomedical dataset using Python and pandas.



\# Biomedical Data Analysis



This beginner-friendly project demonstrates exploratory analysis and visualisation of a fictional biomedical dataset using Python.



\## Project objective



The analysis compares changes in C-reactive protein (CRP) between a treatment group and a control group after eight weeks.



\## Dataset



The fictional dataset contains 20 patients and includes:



\- Patient ID

\- Age

\- Sex

\- Treatment group

\- Baseline CRP

\- Week 8 CRP

\- Treatment response



One missing follow-up measurement is included to demonstrate missing-data detection.



\## Analysis



The Python script:



\- Loads the CSV dataset with pandas

\- Displays the dataset dimensions

\- Checks for missing values

\- Calculates CRP reduction

\- Compares average CRP reduction between groups

\- Creates and saves a box plot



\## Preliminary results



The fictional treatment group had a larger average CRP reduction than the control group:



\- Treatment group: 11.34 mg/L

\- Control group: 1.63 mg/L



These results are for programming practice only and should not be interpreted as clinical evidence.



\## Visualisation



!\[CRP reduction by treatment group](figures/crp\_reduction\_by\_group.png)



\## Technologies



\- Python

\- pandas

\- Matplotlib

\- Seaborn



\## Project structure



```text

biomedical-data-analysis/

├── data/

│   └── patient\_data.csv

├── figures/

│   └── crp\_reduction\_by\_group.png

├── analysis.py

├── requirements.txt

└── README.md


\## How to run



```bash

python -m pip install -r requirements.txt

python analysis.py


## Author

Manfred Anim


