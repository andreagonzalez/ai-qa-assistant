from pathlib import Path
import sys

from ai_qa_assistant.app import load_user_stories_from_file, run_analysis


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("examples/multiple-user-stories.txt")
    output_dir = Path("reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}")
        return 1

    user_stories = load_user_stories_from_file(str(input_path))

    for idx, story in enumerate(user_stories, start=1):
        result = run_analysis(story)
        report_path = output_dir / f"report_{idx:02d}.md"
        report_path.write_text(result["report"], encoding="utf-8")
        print(f"Wrote {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
