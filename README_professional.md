<p align="center">
  <img src="assets/images/dataraflow-banner.png" alt="DataraFlow AI and Data Lab banner" width="100%">
</p>

# DataraFlow

**Data Science · Machine Learning · Explainable AI**

DataraFlow is my working portfolio for documenting a six-month learning journey through data science, analytics, and applied machine learning as part of the [DataraFlow Data Science & AI Accelerator](https://www.dataraflow.org/), Cohort 2.

This repository brings together learning exercises, exploratory analysis, data workflows, database utilities, and a proposed research capstone. It records work in progress; planned research and future milestones are labelled accordingly.

**Author:** Innocent Ekwueme  
**Programme:** DataraFlow Data Science & AI Accelerator, Cohort 2  
**Verification ID:** `DF-2026-264`  
**Repository:** [EkwuemeSpace/DataraFlow](https://github.com/EkwuemeSpace/DataraFlow)

---

## Contents

- [Objectives](#objectives)
- [Research capstone](#research-capstone)
- [Technology stack](#technology-stack)
- [Repository structure](#repository-structure)
- [Learning roadmap](#learning-roadmap)
- [Setup](#setup)
- [Working principles](#working-principles)
- [Progress](#progress)
- [Links](#links)
- [License](#license)

## Objectives

- Document weekly learning and project deliverables.
- Build reproducible data-cleaning and analysis workflows.
- Apply statistical methods and machine-learning techniques to practical questions.
- Evaluate models with appropriate metrics and communicate their limitations.
- Develop a portfolio of research-informed data-science projects.

## Research capstone

### Predicting Student Academic Attrition Risk in Nigerian Secondary Schools

**Proposed research question:** Does digital access improve the prediction of academic attrition risk among Nigerian secondary-school-age learners beyond socio-demographic factors alone?

The proposed study will compare three feature groups:

| Model | Features | Purpose |
|---|---|---|
| Baseline | Socio-demographic variables | Establish a reference performance level |
| Digital access | Digital-access indicators | Assess their predictive signal |
| Combined | Socio-demographic and digital-access variables | Estimate the additional predictive value of digital access |

### Candidate data sources

- **Nigeria General Household Survey Panel (GHSP), 2023–2024:** Primary candidate, subject to verification of relevant variables and cross-wave linkage.
- **Nigeria Multiple Indicator Cluster Survey (MICS), 2021:** Alternative candidate, subject to verification of suitable education and digital-access variables.

The final dataset and outcome definition have not yet been confirmed. They will depend on variable coverage, data availability, and whether a defensible measure of academic attrition can be constructed.

### Planned methods

| Method | Intended role |
|---|---|
| Logistic Regression | Interpretable probabilistic baseline |
| Random Forest | Model nonlinear patterns and feature interactions |
| XGBoost | Gradient-boosted modelling for tabular data |
| SHAP | Explain global feature contributions and individual predictions |

### Planned evaluation

- **Primary metric:** Precision–Recall AUC (PR-AUC), particularly if the outcome is imbalanced.
- **Additional metrics:** Recall, macro F1-score, and ROC-AUC.
- **Calibration:** Calibration curves to compare predicted risks with observed outcomes.

The modelling workflow will use suitable training, validation, and test splits. Preprocessing and any class-imbalance handling will be fitted within the training workflow to reduce the risk of data leakage. These methods describe the proposed design; results have not yet been reported.

Research reflection: [The Research Proposal That Almost Broke Me — Medium](https://medium.com/@innocentekwueme79/the-research-proposal-that-almost-broke-me-my-dataraflow-weeks-4-and-5-experience-3c48410b60b7)

## Technology stack

| Area | Tools |
|---|---|
| Programming | Python 3.10+ |
| Data manipulation | NumPy, Pandas |
| Notebooks | Jupyter Notebook, JupyterLab |
| Visualization | Matplotlib, Seaborn |
| Machine learning | scikit-learn, XGBoost |
| Explainable AI | SHAP |
| Data ingestion | BeautifulSoup, Scrapy |
| Databases | SQLite, SQL |
| Version control | Git, GitHub |
| Development environments | Virtual environments, Linux, Windows PowerShell |

## Repository structure

```text
DataraFlow/
├── assets/
│   └── images/
│       └── dataraflow-banner.png
├── data/
│   ├── cities_full.csv
│   ├── cities_mean_temp.csv
│   └── who_all.csv
├── notebooks/
│   ├── Take Home.ipynb
│   └── week6_analysis.ipynb
├── db/
│   └── dataraflow_db.py
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

### Current project artifacts

**`notebooks/Take Home.ipynb`**
- Initial data profiling and structural checks
- Data-type and whitespace checks
- Missing-value and sparsity analysis
- Summary statistics and categorical-column profiling

**`notebooks/week6_analysis.ipynb`**
- Distribution analysis and statistical testing
- Correlation and multicollinearity checks
- Outlier investigation using IQR and z-scores
- Multivariate exploratory analysis

**`db/dataraflow_db.py`**
- CSV-to-database ingestion
- Database connections and transaction handling
- Batch processing
- Parameterized SQL queries

### Dataset inventory

| File | Description / intended use |
|---|---|
| `cities_full.csv` | City-level reference data for geographic summaries and analysis |
| `cities_mean_temp.csv` | City and temperature data for climate summaries and seasonal analysis |
| `who_all.csv` | Country-level public-health indicators for cross-country analysis |

Confirm each dataset's schema and provenance in the relevant notebook before relying on these descriptions for analysis.

## Learning roadmap

| Month | Focus | Status |
|---|---|---|
| 1 | Foundations and core tooling: Python, OOP, Git, PowerShell | Completed |
| 2 | Exploratory data science: NumPy, Pandas, visualization, statistics | In progress |
| 3 | Relational systems and algorithms: SQLite, SQL, Big-O analysis | Upcoming |
| 4 | Data ingestion and regression: BeautifulSoup, Scrapy, Ridge, Lasso | Upcoming |
| 5 | Supervised machine learning and NLP | Upcoming |
| 6 | Capstone, research communication, and portfolio presentation | Upcoming |

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/EkwuemeSpace/DataraFlow.git
cd DataraFlow
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Open the notebook you want to run and verify that its dataset paths resolve from the current working directory. If a notebook expects files in a different location, adjust the paths to match the repository structure.

## Working principles

- **Reproducibility:** Track dependencies and use fixed random seeds where appropriate.
- **Data integrity:** Preserve source data and document transformations.
- **Security:** Keep credentials, API keys, and private information out of version control.
- **Validation:** Check schemas, missing values, distributions, and outliers before modelling.
- **Responsible evaluation:** Avoid data leakage and report limitations alongside performance.
- **Interpretability:** Use suitable explanation methods to investigate model behaviour.

## Progress

- [x] Establish the repository and development workflow
- [x] Create initial data-profiling and exploratory-analysis notebooks
- [ ] Complete the ongoing exploratory analysis
- [ ] Develop relational database and ingestion workflows
- [ ] Implement and compare machine-learning models
- [ ] Produce SHAP-based model explanations
- [ ] Finalize the research capstone and portfolio presentation

This checklist reflects the current project plan and should be updated as work is completed.

## Links

- **GitHub:** [EkwuemeSpace](https://github.com/EkwuemeSpace)
- **Programme:** [DataraFlow Data Science & AI Accelerator](https://www.dataraflow.org/)
- **Research reflection:** [Read the article on Medium](https://medium.com/@innocentekwueme79/the-research-proposal-that-almost-broke-me-my-dataraflow-weeks-4-and-5-experience-3c48410b60b7)

## License

This repository is distributed under the [MIT License](LICENSE). See the `LICENSE` file for the applicable terms.
