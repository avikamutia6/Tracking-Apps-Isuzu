import gspread
from google.oauth2 import service_account

# Ganti dengan ID spreadsheet Anda
SPREADSHEET_ID = "1O6Bq9nmNRicX-_n-P15x_fNAJ6FtOGYm"

def test_connection():
    try:
        print("1. Menginisialisasi koneksi...")
        credentials = service_account.Credentials.from_service_account_file(
            'credentials.json',
            scopes=[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        
        gc = gspread.authorize(credentials)
        print("✅ Berhasil mengotorisasi")
        
        print("\n2. Membuka spreadsheet...")
        spreadsheet = gc.open_by_key(SPREADSHEET_ID)
        print(f"✅ Spreadsheet ditemukan: {spreadsheet.title}")
        
        print("\n3. Mendapatkan worksheets...")
        worksheets = spreadsheet.worksheets()
        print(f"✅ Jumlah worksheets: {len(worksheets)}")
        
        for i, ws in enumerate(worksheets):
            print(f"   Worksheet {i}: {ws.title} - {ws.row_count} rows x {ws.col_count} cols")
        
        print("\n4. Menguji akses data...")
        if worksheets:
            ws = worksheets[0]
            print(f"   Mengakses worksheet: {ws.title}")
            
            # Coba baca header
            headers = ws.row_values(1)
            print(f"   Header: {headers}")
            
            # Cek total baris
            all_values = ws.get_all_values()
            print(f"   Total baris data: {len(all_values) - 1}")
            
            if len(all_values) > 1:
                print("   Data pertama:")
                for i in range(min(3, len(all_values))):
                    print(f"   Baris {i+1}: {all_values[i]}")
        
        print("\n✅ Semua test berhasil!")
        
    except FileNotFoundError:
        print("❌ ERROR: File credentials.json tidak ditemukan")
    except gspread.SpreadsheetNotFound:
        print(f"❌ ERROR: Spreadsheet dengan ID {SPREADSHEET_ID} tidak ditemukan")
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    test_connection()