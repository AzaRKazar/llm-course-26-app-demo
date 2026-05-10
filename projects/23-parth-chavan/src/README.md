# HeartRisk AI — Source Code

The full source code lives in two repositories:

## Backend (FastAPI + ML)
**[github.com/Parthchavann/heart-disease-risk-prediction](https://github.com/Parthchavann/heart-disease-risk-prediction)**

```bash
git clone https://github.com/Parthchavann/heart-disease-risk-prediction.git
cd heart-disease-risk-prediction
pip install -r requirements.txt
cp .env.example .env        # add GEMINI_API_KEY
python run.py               # starts at http://localhost:8000
```

## Frontend (React / Vite)
**[github.com/Parthchavann/semantic-resume-ranker-pro](https://github.com/Parthchavann/semantic-resume-ranker-pro)**

```bash
git clone https://github.com/Parthchavann/semantic-resume-ranker-pro.git
cd semantic-resume-ranker-pro
npm install
npm run dev                 # starts at http://localhost:5173
```

## Stack
- **ML Model**: Stacking Ensemble (XGBoost + LightGBM + CatBoost + Random Forest + SVM) — Test AUC 0.94
- **Explainability**: SHAP feature attribution
- **LLM**: Google Gemini 1.5 Flash (text + Vision)
- **API**: FastAPI + SQLite + JWT auth
- **Frontend**: React 18, Tailwind CSS, shadcn/ui
