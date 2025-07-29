
# NNFX Forex Signal App (Streamlit)

A simple tool that applies No-Nonsense Forex methodology indicators to generate Buy/Sell/Hold signals.

## Features
- KAMA, ROC, ATR, DI calculation
- Live currency data from Alpha Vantage
- Streamlit frontend

## Setup
1. Add your Alpha Vantage key in `.streamlit/secrets.toml`
2. Run:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud
- Push to GitHub
- Set secret `ALPHA_VANTAGE_API_KEY` under app settings
