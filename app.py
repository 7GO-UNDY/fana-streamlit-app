import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("ファナ構造連携アプリ")

# --- 認証スコープの定義 ---
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# --- credentials.json から認証情報を読み込み ---
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# --- スプレッドシートを開く（シート名を自分のに変える！）---
SHEET_NAME = "テンプレートシート"  # 実際のシート名に置き換えてください
sheet = client.open(SHEET_NAME).sheet1

# --- スプレッドシートのデータを取得して表示 ---
records = sheet.get_all_records()

st.subheader("📖 テンプレを集める")
st.write(records)
