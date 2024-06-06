# Mencoba addons field_encryption

## Instalasi
1. Unduh addon field_encryption di https://github.com/ShahAlamSumon/field_encryption

2. Install pustaka cryptography

        pip install cryptography

3. Install addon field_encryption.
4. Buat encryption_key dengan cara sbb.
    1. Buka terminal command line
    2. Jalankan: ```python3```
    3. Copy paste 2 baris di bawah ini lalu tekan Enter.

            from cryptography.fernet import Fernet
            Fernet.generate_key().decode()

5. Tambahkan encryption_key dan server_wide_module di file konfigurasi Odoo.

        encryption_key=<YOUR_KEY>
        server_wide_modules = web,field_encryption

6. Restart Odoo.
7. Install addon ini.
