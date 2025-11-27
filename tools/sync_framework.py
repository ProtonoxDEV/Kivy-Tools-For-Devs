#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = ROOT / "framework"
ENV_PREFIX = "PROTONOX_"


def repo_env(key: str, default: str) -> str:
    return os.environ.get(f"{ENV_PREFIX}{key}", default)


def run(command: List[str], cwd: Optional[Path] = None) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )
    return result.stdout.strip()


def clear_directory(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        return
    for entry in path.iterdir():
        if entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()


def copy_contents(src: Path, dest: Path) -> None:
    for item in src.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def remove_git_artifacts(path: Path) -> None:
    git_dir = path / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)
    gitmodules = path / ".gitmodules"
    if gitmodules.exists():
        gitmodules.unlink()


def write_version(path: Path, ref: str) -> None:
    path.write_text(f"{ref}\n", encoding="utf-8")


@dataclass
class Component:
    name: str
    repo: str
    ref: str
    dest: Path
    version_file: Optional[Path] = None
    remove_paths: Optional[Iterable[str]] = None

    def sync(self) -> None:
        print(f"Syncing {self.name} from {self.repo}@{self.ref}")
        clear_directory(self.dest)
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            try:
                run(["git", "clone", "--depth", "1", "--branch", self.ref, self.repo, str(tmp_dir)])
            except subprocess.CalledProcessError as exc:
                raise RuntimeError(
                    "Failed to clone upstream repository. Ensure network access is available "
                    "and credentials are configured if needed."
                ) from exc
            ref_value = run(["git", "rev-parse", "HEAD"], cwd=tmp_dir)
            for unwanted in self.remove_paths or []:
                candidate = tmp_dir / unwanted
                if candidate.exists():
                    if candidate.is_dir():
                        shutil.rmtree(candidate)
                    else:
                        candidate.unlink()
            remove_git_artifacts(tmp_dir)
            copy_contents(tmp_dir, self.dest)
        write_version(self.version_file or (self.dest / "VERSION.txt"), ref_value)


def components() -> List[Component]:
    cython_ref = repo_env("CYTHON_REF", "0.29.37")
    return [
        Component(
            name="python-for-android",
            repo=repo_env("P4A_REPO", "https://github.com/kivy/python-for-android.git"),
            ref=repo_env("P4A_REF", "master"),
            dest=FRAMEWORK_ROOT / "python-for-android",
        ),
        Component(
            name="kivy",
            repo=repo_env("KIVY_REPO", "https://github.com/kivy/kivy.git"),
            ref=repo_env("KIVY_REF", "master"),
            dest=FRAMEWORK_ROOT / "kivy-2.3.1-protonox",
            remove_paths=["examples", "tests"],
        ),
        Component(
            name="pyjnius",
            repo=repo_env("PYJNIUS_REPO", "https://github.com/kivy/pyjnius.git"),
            ref=repo_env("PYJNIUS_REF", "master"),
            dest=FRAMEWORK_ROOT / "pyjnius-protonox",
        ),
        Component(
            name="cython",
            repo=repo_env("CYTHON_REPO", "https://github.com/cython/cython.git"),
            ref=cython_ref,
            dest=FRAMEWORK_ROOT / "cython-protonox",
        ),
        Component(
            name="buildozer",
            repo=repo_env("BUILDOZER_REPO", "https://github.com/kivy/buildozer.git"),
            ref=repo_env("BUILDOZER_REF", "master"),
            dest=FRAMEWORK_ROOT / "buildozer",
        ),
    ]


def main() -> None:
    all_components = components()
    for component in all_components:
        component.sync()
    print("Done. Upstream libraries synced into framework/.")


if __name__ == "__main__":
    main()
