# SHOE MANAGER

## INSTALL
- Kích hoạt môi trường
```buildoutcfg
cd menv/Scripts

activate
```
- Cài thư viện nếu lỗi
```buildoutcfg
python -m pip install django django-seed

```
- Tạo và seed data cho database
```buildoutcfg
python manage.py makemigrations

python manage.py migrate
```

```buildoutcfg
python manage.py loaddata seed.json
```

## RUN

```buildoutcfg
python manage.py runserver
```
- Admin: http://127.0.0.1:8000/admin/
```buildoutcfg
user: admin
pass: 123456@
```
- Dump User
```buildoutcfg
user: user
pass: 123

```