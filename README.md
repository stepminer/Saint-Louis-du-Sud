# Build ready-to-upload XLSForms (Kobo/ODK)

This bundle generates two XLSForms:
- dist/Menage.xlsx
- dist/Commerce.xlsx

They include the required sheets (survey, choices, settings) and are ready to upload to Kobo/ODK.

Quick start
1) Install dependencies:
   pip install -r requirements.txt
2) Build XLSForms:
   python scripts/build_xlsforms.py
3) Upload:
   - Upload dist/Menage.xlsx to Kobo/ODK (default language: fr)
   - Upload dist/Commerce.xlsx to Kobo/ODK (default language: fr)

Notes
- GPS capture is mandatory in both forms.
- Consent is required; phone is optional and only for QA callbacks.
- Labels are bilingual (French and Haitian Creole where provided).

Repository contents
- forms/: CSVs for survey, choices, settings for each form
- scripts/: build script to generate .xlsx
- docs/: KII guides, skip-logic diagrams, enumerator briefs
- dist/: generated .xlsx (created by the build script)
