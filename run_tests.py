import subprocess
import sys

print("Запускаю BDD тесты...")
result = subprocess.run([sys.executable, '-m', 'behave'])

if result.returncode == 0:
    print("Все BDD тесты прошли успешно!")
else:
    print("Есть ошибки в BDD тестах")