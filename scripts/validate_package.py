"""Dependency-free static checks; does not evaluate agent behavior or full YAML syntax."""
from pathlib import Path
import re
import sys


def validate(root: Path) -> list[str]:
    errors = []
    skill = root / "skills" / "amazon-market-research"
    required = [
        root / "README.md", skill / "SKILL.md", skill / "agents/openai.yaml",
        skill / "references/traffic-analysis.md", skill / "references/profit-model.md",
        root / "docs/product-design.md", root / "docs/evaluation.md",
        root / "docs/publishing.md", root / "examples/walkthrough.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(root)}")
    entry = skill / "SKILL.md"
    if entry.is_file():
        content = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not match:
            errors.append("Missing skill frontmatter")
        else:
            frontmatter = match.group(1)
            if not re.search(r"^name: amazon-market-research$", frontmatter, re.M):
                errors.append("Unexpected skill name")
            if not re.search(r"^description: \S", frontmatter, re.M):
                errors.append("Missing skill description")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if re.match(r"[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("PASS: required files, skill identity and relative Markdown links.")
    print("Agent behavior, factual accuracy and business outcomes were not tested.")
