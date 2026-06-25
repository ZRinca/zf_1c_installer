# ⚙️ ZF 1C Installer

> Графический установщик для автоматизации развёртывания и настройки компонентов 1С:Предприятие.

Проект представляет собой desktop-приложение на Python с интерфейсом на `customtkinter`. Упрощает установку расширений, настройку Apache и другие рутинные задачи.

## 🚀 Быстрый старт (самый простой способ)

**запустите файл** `_init.bat` — он сам создаст виртуальное окружение, установит зависимости.
Просто **запустите файл** `run_setup.bat` — и он откроет приложение.

> Всё, что нужно — дважды кликнуть по `run_setup.bat`.

---

## 🛠 Ручная установка (если нужно)

```bash
git clone https://github.com/ZRinca/zf_1c_installer.git
cd zf_1c_installer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
