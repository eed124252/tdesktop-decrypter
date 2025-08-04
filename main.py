# main.py
import argparse
from tdesktop_decrypter.tdata_reader import TdataReader

def main():
    parser = argparse.ArgumentParser(description="Telegram tdata decrypter")
    parser.add_argument("tdata_path", help="Path to Telegram's tdata folder")
    parser.add_argument("--passcode", default="", help="Passcode for local key (if set)")

    args = parser.parse_args()

    reader = TdataReader(args.tdata_path)
    parsed = reader.read(args.passcode)

    print(f"[+] Settings: {parsed.settings}")
    print(f"[+] Accounts:")
    for idx, acc in parsed.accounts.items():
        print(f"  - Account #{idx}: User ID {acc.mtp_data.user_id}, DC {acc.mtp_data.current_dc_id}")

if __name__ == "__main__":
    main()
