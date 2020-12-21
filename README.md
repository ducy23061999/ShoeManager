# SHOE MANAGER

## INSTALL
- Kích hoạt môi trường
```buildoutcfg
cd menv/Scripts

activate
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