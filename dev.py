import subprocess
import sys
import os
from pathlib import Path
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FrontendBuildHandler(FileSystemEventHandler):
    def __init__(self, frontend_dir):
        self.frontend_dir = frontend_dir
        self.last_build_time = 0
        self.build_cooldown = 1

    def on_modified(self, event):
        if event.is_directory:
            return

        if not str(event.src_path).startswith(str(Path(self.frontend_dir) / 'src')):
            return

        current_time = time.time()
        if current_time - self.last_build_time > self.build_cooldown:
            print(f"\n 👌 フロントエンドファイルの変更を検知しました: {event.src_path}")
            subprocess.run(["pnpm", "build"], cwd=self.frontend_dir)
            self.last_build_time = current_time

def run_servers():
    root_dir = Path(__file__).parent.absolute()
    frontend_dir = root_dir / "frontend"
    python_path = os.path.join(root_dir, ".venv", "Scripts", "python.exe")

    try:
        print("🔨 フロントエンドのビルドを行います...")
        subprocess.run(["pnpm", "build"], cwd=frontend_dir)

        event_handler = FrontendBuildHandler(frontend_dir)
        observer = Observer()
        observer.schedule(event_handler, str(frontend_dir), recursive=True)
        observer.start()
        print("🔍 フロントエンドサイドのファイル監視を開始しました。")

        django_process = subprocess.Popen(
            [python_path, "manage.py", "runserver"],
            cwd=os.path.join(root_dir, "backend"),
        )
        print("🐍 Django サーバーを http://localhost:8000 に起動しました。")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            django_process.terminate()
            print("\n🛑 サーバーを停止します...")
            observer.join()
            django_process.wait()
            print("🚧 サーバーを停止しました。")

    except Exception as e:
        print(f"Error: {e}")
        observer.stop()
        django_process.terminate()
        observer.join()
        django_process.wait()

if __name__ == "__main__":
    run_servers()