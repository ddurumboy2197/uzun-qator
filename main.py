class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def salom(self):
        print(f"Salom, men {self.ism} yoshim {self.yosh}!")
```

```python
# Shaxs klassidan foydalanish misoli
shaxs = Shaxs("Ali", 25)
shaxs.salom()
```

Kodni ishlatish uchun quyidagicha qilishingiz mumkin:

1. Klassni yaratish:
   ```python
shaxs = Shaxs("Ali", 25)
```

2. `salom()` metodi yordamida salomlash:
   ```python
shaxs.salom()
```

Natijada, quyidagicha chiqadi:
```
Salom, men Ali yoshim 25!
