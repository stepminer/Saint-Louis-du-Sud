import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMS_DIR = os.path.join(BASE_DIR, "forms")
DIST_DIR = os.path.join(BASE_DIR, "dist")
os.makedirs(DIST_DIR, exist_ok=True)

def build_xlsform(prefix: str, out_name: str):
    survey_path = os.path.join(FORMS_DIR, f"{prefix}_survey.csv")
    choices_path = os.path.join(FORMS_DIR, f"{prefix}_choices.csv")
    settings_path = os.path.join(FORMS_DIR, f"{prefix}_settings.csv")
    out_path = os.path.join(DIST_DIR, out_name)

    survey = pd.read_csv(survey_path, dtype=str).fillna("")
    choices = pd.read_csv(choices_path, dtype=str).fillna("")
    settings = pd.read_csv(settings_path, dtype=str).fillna("")

    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        survey.to_excel(writer, sheet_name="survey", index=False)
        choices.to_excel(writer, sheet_name="choices", index=False)
        settings.to_excel(writer, sheet_name="settings", index=False)

    print(f"Wrote {out_path}")

def main():
    build_xlsform("menage", "Menage.xlsx")
    build_xlsform("commerce", "Commerce.xlsx")

if __name__ == "__main__":
    main()